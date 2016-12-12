# -*- coding: UTF-8 -*-
from __future__ import division
import string
from nn.utils.io_utils import serialize_to_file

from lang.ifttt.grammar import IFTTTGrammar
from parse import ifttt_ast_to_parse_tree
from lang.grammar import Grammar
import logging
from itertools import chain

from nn.utils.generic_utils import init_logging

from dataset import gen_vocab, DataSet, DataEntry, Action, APPLY_RULE, GEN_TOKEN, COPY_TOKEN, GEN_COPY_TOKEN

def load_examples(data_file):
    f = open(data_file)
    next(f)
    examples = []
    for line in f:
        d = line.strip().split('\t')
        description = d[4]
        code = d[9]
        parse_tree = ifttt_ast_to_parse_tree(code)

        examples.append({'description': description, 'parse_tree': parse_tree, 'code': code})

    return examples


def analyze_ifttt_dataset():
    data_file = '/Users/yinpengcheng/Research/SemanticParsing/ifttt/recipe_summaries.all.tsv'
    examples = load_examples(data_file)

    rule_num = 0.
    max_rule_num = -1
    example_with_max_rule_num = -1

    for idx, example in enumerate(examples):
        parse_tree = example['parse_tree']
        rules, _ = parse_tree.get_productions(include_value_node=True)

        rule_num += len(rules)
        if max_rule_num < len(rules):
            max_rule_num = len(rules)
            example_with_max_rule_num = idx

    logging.info('avg. num. of rules: %f', rule_num / len(examples))
    logging.info('max_rule_num: %d', max_rule_num)
    logging.info('example_with_max_rule_num: %d', example_with_max_rule_num)


def canonicalize_ifttt_example(annot, code):
    parse_tree = ifttt_ast_to_parse_tree(code, attach_func_to_channel=False)
    clean_code = str(parse_tree)
    clean_query_tokens = annot.split()
    clean_query_tokens = [t.lower() for t in clean_query_tokens]

    return clean_query_tokens, clean_code, parse_tree


def preprocess_ifttt_dataset(annot_file, code_file):
    f = open('ifttt_dataset.examples.txt', 'w')

    examples = []

    for idx, (annot, code) in enumerate(zip(open(annot_file), open(code_file))):
        annot = annot.strip()
        code = code.strip()

        clean_query_tokens, clean_code, parse_tree = canonicalize_ifttt_example(annot, code)
        example = {'id': idx, 'query_tokens': clean_query_tokens, 'code': clean_code, 'parse_tree': parse_tree,
                   'str_map': None, 'raw_code': code}
        examples.append(example)

        f.write('*' * 50 + '\n')
        f.write('example# %d\n' % idx)
        f.write(' '.join(clean_query_tokens) + '\n')
        f.write('\n')
        f.write(clean_code + '\n')
        f.write('*' * 50 + '\n')

        idx += 1

    f.close()

    print 'preprocess_dataset: cleaned example num: %d' % len(examples)

    return examples


def get_grammar(parse_trees):
    rules = set()

    for parse_tree in parse_trees:
        parse_tree_rules, rule_parents = parse_tree.get_productions()
        for rule in parse_tree_rules:
            rules.add(rule)

    rules = list(sorted(rules, key=lambda x: x.__repr__()))
    grammar = IFTTTGrammar(rules)

    logging.info('num. rules: %d', len(rules))

    with open('grammar.txt', 'w') as f:
        for rule in grammar:
            str = rule.__repr__()
            f.write(str + '\n')

    with open('parse_trees.txt', 'w') as f:
        for tree in parse_trees:
            f.write(tree.__repr__() + '\n')

    return grammar


def parse_ifttt_dataset():
    WORD_FREQ_CUT_OFF = 3

    annot_file = '/Users/yinpengcheng/Research/SemanticParsing/ifttt/Data/lang.all.txt'
    code_file = '/Users/yinpengcheng/Research/SemanticParsing/ifttt/Data/code.all.txt'

    data = preprocess_ifttt_dataset(annot_file, code_file)

    # build the grammar
    grammar = get_grammar([e['parse_tree'] for e in data])

    annot_tokens = list(chain(*[e['query_tokens'] for e in data]))
    annot_vocab = gen_vocab(annot_tokens, vocab_size=5000, freq_cutoff=WORD_FREQ_CUT_OFF)

    logging.info('annot vocab. size: %d', annot_vocab.size)

    # we have no terminal tokens in ifttt
    all_terminal_tokens = []
    terminal_vocab = gen_vocab(all_terminal_tokens, vocab_size=4000, freq_cutoff=WORD_FREQ_CUT_OFF)

    # now generate the dataset!

    train_data = DataSet(annot_vocab, terminal_vocab, grammar, 'ifttt.train_data')
    dev_data = DataSet(annot_vocab, terminal_vocab, grammar, 'ifttt.dev_data')
    test_data = DataSet(annot_vocab, terminal_vocab, grammar, 'ifttt.test_data')

    all_examples = []

    can_fully_reconstructed_examples_num = 0
    examples_with_empty_actions_num = 0

    for entry in data:
        idx = entry['id']
        query_tokens = entry['query_tokens']
        code = entry['code']
        parse_tree = entry['parse_tree']

        # check if query tokens are valid
        query_token_ids = [annot_vocab[token] for token in query_tokens if token not in string.punctuation]
        valid_query_tokens_ids = [tid for tid in query_token_ids if tid != annot_vocab.unk]

        if len(valid_query_tokens_ids) == 0:
            continue

        rule_list, rule_parents = parse_tree.get_productions(include_value_node=True)

        actions = []
        can_fully_reconstructed = True
        rule_pos_map = dict()

        for rule_count, rule in enumerate(rule_list):
            if not grammar.is_value_node(rule.parent):
                assert rule.value is None
                parent_rule = rule_parents[(rule_count, rule)][0]
                if parent_rule:
                    parent_t = rule_pos_map[parent_rule]
                else:
                    parent_t = 0

                rule_pos_map[rule] = len(actions)

                d = {'rule': rule, 'parent_t': parent_t, 'parent_rule': parent_rule}
                action = Action(APPLY_RULE, d)

                actions.append(action)
            else:
                raise RuntimeError('no terminals should be in ifttt dataset!')

        if len(actions) == 0:
            examples_with_empty_actions_num += 1
            continue

        example = DataEntry(idx, query_tokens, parse_tree, code, actions,
                            {'str_map': None, 'raw_code': entry['raw_code']})

        if can_fully_reconstructed:
            can_fully_reconstructed_examples_num += 1

        # train, valid, test splits
        if 0 <= idx < 77495:
            train_data.add(example)
        elif idx < 77495 + 5171:
            dev_data.add(example)
        else:
            test_data.add(example)

        all_examples.append(example)

    # print statistics
    max_query_len = max(len(e.query) for e in all_examples)
    max_actions_len = max(len(e.actions) for e in all_examples)

    # serialize_to_file([len(e.query) for e in all_examples], 'query.len')
    # serialize_to_file([len(e.actions) for e in all_examples], 'actions.len')

    logging.info('train_data examples: %d', train_data.count)
    logging.info('dev_data examples: %d', dev_data.count)
    logging.info('test_data examples: %d', test_data.count)

    logging.info('examples that can be fully reconstructed: %d/%d=%f',
                 can_fully_reconstructed_examples_num, len(all_examples),
                 can_fully_reconstructed_examples_num / len(all_examples))
    logging.info('empty_actions_count: %d', examples_with_empty_actions_num)

    logging.info('max_query_len: %d', max_query_len)
    logging.info('max_actions_len: %d', max_actions_len)

    train_data.init_data_matrices()
    dev_data.init_data_matrices()
    test_data.init_data_matrices()

    serialize_to_file((train_data, dev_data, test_data),
                      'data/ifttt.freq{WORD_FREQ_CUT_OFF}.bin'.format(WORD_FREQ_CUT_OFF=WORD_FREQ_CUT_OFF))

    return train_data, dev_data, test_data


if __name__ == '__main__':
    init_logging('ifttt.log')
    parse_ifttt_dataset()
    # analyze_ifttt_dataset()
