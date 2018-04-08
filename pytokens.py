# This file encapsulates all python keywords and inbuilt functions in a list

PYKEYWORDS = [
            # keywords
            "False",
            "class",
            "finally",
            "is",
            "return",
            "None",
            "continue",
            "for",
            "lambda",
            "try",
            "True",
            "def",
            "from",
            "nonlocal",
            "while",
            "and",
            "del",
            "global",
            "not",
            "with",
            "as",
            "elif",
            "if",
            "or",
            "yield",
            "assert",
            "else",
            "import",
            "pass",
            "break",
            "except",
            "in",
            "raise",
            # inbuilt functions
            "abs",
            "dict",
            "help",
            "min",
            "setattr",
            "all",
            "dir",
            "hex",
            "next",
            "slice",
            "any",
            "divmod",
            "id",
            "object",
            "sorted",
            "ascii",
            "enumerate",
            "input",
            "oct",
            "staticmethod",
            "bin",
            "eval",
            "int",
            "open",
            "str",
            "bool",
            "exec",
            "isinstance",
            "ord",
            "sum",
            "bytearray",
            "filter",
            "issubclass",
            "pow",
            "super",
            "bytes",
            "float",
            "iter",
            "print",
            "tuple",
            "callable",
            "format",
            "len",
            "property",
            "type",
            "chr",
            "frozenset",
            "list",
            "range",
            "vars",
            "classmethod",
            "getattr",
            "locals",
            "repr",
            "zip",
            "compile",
            "globals",
            "map",
            "reversed",
            "__import__",
            "complex",
            "hasattr",
            "max",
            "round",
            "delattr",
            "hash",
            "memoryview",
            "set"]
            # builtin type (int, long, ) functions
            #"__abs__",
            #"__add__",
            #"__and__",
            #"__class__",
            #"__cmp__",
            #"__coerce__",
            #"__contains__",
            #"__delattr__",
            #"__delitem__",
            #"__delslice__",
            #"__div__",
            #"__divmod__",
            #"__doc__",
            #"__eq__",
            #"__float__",
            #"__floordiv__",
            #"__format__",
            #"__ge__",
            #"__getattribute__",
            #"__getformat__",
            #"__getitem__",
            #"__getnewargs__",
            #"__getslice__",
            #"__gt__",
            #"__hash__",
            #"__hex__",
            #"__iadd__",
            #"__iand__",
            #"__imul__",
            #"__index__",
            #"__init__",
            #"__int__",
            #"__invert__",
            #"__ior__",
            #"__isub__",
            #"__iter__",
            #"__ixor__",
            #"__le__",
            #"__len__",
            #"__long__",
            #"__lshift__",
            #"__lt__",
            #"__mod__",
            #"__mul__",
            #"__ne__",
            #"__neg__",
            #"__new__",
            #"__nonzero__",
            #"__oct__",
            #"__or__",
            #"__pos__",
            #"__pow__",
            #"__radd__",
            #"__rand__",
            #"__rdiv__",
            #"__rdivmod__",
            #"__reduce__",
            #"__reduce_ex__",
            #"__repr__",
            #"__reversed__",
            #"__rfloordiv__",
            #"__rlshift__",
            #"__rmod__",
            #"__rmul__",
            #"__ror__",
            #"__rpow__",
            #"__rrshift__",
            #"__rshift__",
            #"__rsub__",
            #"__rtruediv__",
            #"__rxor__",
            #"__setattr__",
            #"__setformat__",
            #"__setitem__",
            #"__setslice__",
            #"__sizeof__",
            #"__str__",
            #"__sub__",
            #"__subclasshook__",
            #"__truediv__",
            #"__trunc__",
            #"__xor__",
            #"_formatter_field_name_split",
            #"_formatter_parser",
            #"add",
            #"append",
            #"as_integer_ratio",
            #"bit_length",
            #"capitalize",
            #"center",
            #"clear",
            #"conjugate",
            #"copy",
            #"count",
            #"decode",
            #"denominator",
            #"difference",
            #"difference_update",
            #"discard",
            #"encode",
            #"endswith",
            #"expandtabs",
            #"extend",
            #"find",
            #"format",
            #"fromhex",
            #"fromkeys",
            #"get",
            #"has_key",
            #"hex",
            #"imag",
            #"index",
            #"insert",
            #"intersection",
            #"intersection_update",
            #"is_integer",
            #"isalnum",
            #"isalpha",
            #"isdigit",
            #"isdisjoint",
            #"islower",
            #"isspace",
            #"issubset",
            #"issuperset",
            #"istitle",
            #"isupper",
            #"items",
            #"iteritems",
            #"iterkeys",
            #"itervalues",
            #"join",
            #"keys",
            #"ljust",
            #"lower",
            #"lstrip",
            #"numerator",
            #"partition",
            #"pop",
            #"popitem",
            #"real",
            #"remove",
            #"replace",
            #"reverse",
            #"rfind",
            #"rindex",
            #"rjust",
            #"rpartition",
            #"rsplit",
            #"rstrip",
            #"setdefault",
            #"sort",
            #"split",
            #"splitlines",
            #"startswith",
            #"strip",
            #"swapcase",
            #"symmetric_difference",
            #"symmetric_difference_update",
            #"title",
            #"translate",
            #"union",
            #"update",
            #"upper",
            #"values",
            #"viewitems",
            #"viewkeys",
            #"viewvalues",
            #"zfill",
            ## builtin modules
            #"BaseHTTPServer",
            #"_weakrefset",
            #"grp",
            #"requests",
            #"Bastion",
            #"CDROM",
            #"CGIHTTPServer",
            #"Canvas",
            #"ConfigParser",
            #"Cookie",
            #"DLFCN",
            #"Dialog",
            #"DocXMLRPCServer",
            #"FileDialog",
            #"FixTk",
            #"HTMLParser",
            #"IN",
            #"Image",
            #"ImageChops",
            #"ImageColor",
            #"ImageCrackCode",
            #"ImageDraw",
            #"ImageEnhance",
            #"ImageFile",
            #"ImageFileIO",
            #"ImageFilter",
            #"ImageFont",
            #"ImageGL",
            #"ImageGrab",
            #"ImageMath",
            #"ImageOps",
            #"ImagePalette",
            #"ImagePath",
            #"ImageQt",
            #"ImageSequence",
            #"ImageStat",
            #"ImageTk",
            #"ImageWin",
            #"MimeWriter",
            #"PIL",
            #"PSDraw",
            #"PngImagePlugin",
            #"PyKate4",
            #"Queue",
            #"ScrolledText",
            #"SimpleDialog",
            #"SimpleHTTPServer",
            #"SimpleXMLRPCServer",
            #"SocketServer",
            #"StringIO",
            #"TYPES",
            #"Tix",
            #"Tkconstants",
            #"Tkdnd",
            #"Tkinter",
            #"UserDict",
            #"UserList",
            #"UserString",
            #"_LWPCookieJar",
            #"_MozillaCookieJar",
            #"__builtin__",
            #"__future__",
            #"_abcoll",
            #"_ast",
            #"_bisect",
            #"_bsddb",
            #"_codecs",
            #"_codecs_cn",
            #"_codecs_hk",
            #"_codecs_iso2022",
            #"_codecs_jp",
            #"_codecs_kr",
            #"_codecs_tw",
            #"_collections",
            #"_csv",
            #"_ctypes",
            #"_ctypes_test",
            #"_curses",
            #"_curses_panel",
            #"_dbus_bindings",
            #"_dbus_glib_bindings",
            #"_elementtree",
            #"_functools",
            #"_hashlib",
            #"_heapq",
            #"_hotshot",
            #"_io",
            #"_json",
            #"_locale",
            #"_lsprof",
            #"_md5",
            #"_multibytecodec",
            #"_multiprocessing",
            #"_osx_support",
            #"_posixsubprocess",
            #"_pyio",
            #"_random",
            #"_sha",
            #"_sha256",
            #"_sha512",
            #"_socket",
            #"_sqlite3",
            #"_sre",
            #"_ssl",
            #"_strptime",
            #"_struct",
            #"_symtable",
            #"_sysconfigdata",
            #"_sysconfigdata_nd",
            #"_testcapi",
            #"_threading_local",
            #"_tkinter",
            #"_warnings",
            #"zlib",
            #"_weakref",
            #"repr",
            #"abc",
            #"absl",
            #"aifc",
            #"antigravity",
            #"anydbm",
            #"appdirs",
            #"argparse",
            #"array",
            #"ast",
            #"astor",
            #"astunparse",
            #"asynchat",
            #"asyncore",
            #"atexit",
            #"atk",
            #"audiodev",
            #"audioop",
            #"backports",
            #"baron",
            #"base64",
            #"bdb",
            #"bin",
            #"binascii",
            #"binhex",
            #"bisect",
            #"bleach",
            #"bs4",
            #"bsddb",
            #"bz2",
            #"cPickle",
            #"cProfile",
            #"cStringIO",
            #"cairo",
            #"calendar",
            #"certifi",
            #"cgi",
            #"cgitb",
            #"chardet",
            #"chunk",
            #"cmath",
            #"cmd",
            #"code",
            #"codecs",
            #"codegen",
            #"codeop",
            #"collections",
            #"colorsys",
            #"commands",
            #"compileall",
            #"compiler",
            #"concurrent",
            #"configparser",
            #"contextlib",
            #"cookielib",
            #"copy",
            #"copy_reg",
            #"crypt",
            #"csv",
            #"ctypes",
            #"curses",
            #"cycler",
            #"datetime",
            #"dateutil",
            #"dbhash",
            #"dbm",
            #"dbus",
            #"debconf",
            #"decimal",
            #"decorator",
            #"difflib",
            #"dircache",
            #"dis",
            #"distutils",
            #"doctest",
            #"dsextras",
            #"dumbdbm",
            #"dummy_thread",
            #"dummy_threading",
            #"easy_install",
            #"email",
            #"encodings",
            #"ensurepip",
            #"enum",
            #"errno",
            #"exceptions",
            #"external",
            #"fcntl",
            #"filecmp",
            #"fileinput",
            #"fnmatch",
            #"formatter",
            #"fpectl",
            #"fpformat",
            #"fractions",
            #"ftplib",
            #"funcsigs",
            #"functools",
            #"functools32",
            #"future_builtins",
            #"gast",
            #"gc",
            #"genericpath",
            #"getopt",
            #"getpass",
            #"gettext",
            #"gi",
            #"gio",
            #"glib",
            #"glob",
            #"gobject",
            #"",
            #"grpc",
            #"gtk",
            #"gtkunixprint",
            #"gzip",
            #"h5py",
            #"hashlib",
            #"heapq",
            #"hmac",
            #"hotshot",
            #"html5lib",
            #"htmlentitydefs",
            #"htmllib",
            #"httplib",
            #"idna",
            #"ihooks",
            #"imaplib",
            #"imghdr",
            #"imp",
            #"importlib",
            #"imputil",
            #"inspect",
            #"io",
            #"itertools",
            #"json",
            #"keras",
            #"keyword",
            #"lib2to3",
            #"linecache",
            #"linuxaudiodev",
            #"locale",
            #"logging",
            #"lsb_release",
            #"lxml",
            #"macpath",
            #"macurl2path",
            #"mailbox",
            #"mailcap",
            #"markdown",
            #"markupbase",
            #"marshal",
            #"math",
            #"matplotlib",
            #"md5",
            #"mhlib",
            #"mimetools",
            #"mimetypes",
            #"mimify",
            #"mmap",
            #"mock",
            #"modulefinder",
            #"multifile",
            #"multiprocessing",
            #"mutex",
            #"netrc",
            #"networkx",
            #"new",
            #"nis",
            #"nltk",
            #"nntplib",
            #"nose",
            #"ntpath",
            #"nturl2path",
            #"numbers",
            #"numpy",
            #"opcode",
            #"operator",
            #"optparse",
            #"os",
            #"os2emxpath",
            #"ossaudiodev",
            #"pango",
            #"pangocairo",
            #"parser",
            #"pbr",
            #"pdb",
            #"pickle",
            #"pickletools",
            #"pip",
            #"pipes",
            #"pkg_resources",
            #"pkgutil",
            #"platform",
            #"plistlib",
            #"popen2",
            #"poplib",
            #"posix",
            #"posixfile",
            #"posixpath",
            #"pprint",
            #"profile",
            #"pstats",
            #"psutil",
            #"pty",
            #"pwd",
            #"py_compile",
            #"pyclbr",
            #"pydoc",
            #"pydoc_data",
            #"pyexpat",
            #"pygtk",
            #"pygtkcompat",
            #"pylab",
            #"pyparsing",
            #"pytz",
            #"quopri",
            #"random",
            #"re",
            #"readline",
            #"redbaron",
            #"resource",
            #"rexec",
            #"rfc822",
            #"rlcompleter",
            #"robotparser",
            #"rply",
            #"runpy",
            #"sched",
            #"scipy",
            #"select",
            #"sets",
            #"setuptools",
            #"setuputils",
            #"sgmllib",
            #"sha",
            #"shelve",
            #"shlex",
            #"shutil",
            #"signal",
            #"site",
            #"sitecustomize",
            #"six",
            #"sklearn",
            #"smtpd",
            #"smtplib",
            #"sndhdr",
            #"socket",
            #"spwd",
            #"sqlite3",
            #"sre",
            #"sre_compile",
            #"sre_constants",
            #"sre_parse",
            #"ssl",
            #"stat",
            #"statvfs",
            #"string",
            #"stringold",
            #"stringprep",
            #"strop",
            #"struct",
            #"subprocess",
            #"subprocess32",
            #"sunau",
            #"sunaudio",
            #"symbol",
            #"symtable",
            #"sys",
            #"sysconfig",
            #"syslog",
            #"tabnanny",
            #"talloc",
            #"tarfile",
            #"telnetlib",
            #"tempfile",
            #"tensorboard",
            #"tensorflow",
            #"termcolor",
            #"termios",
            #"test",
            #"textwrap",
            #"theano",
            #"this",
            #"thread",
            #"threading",
            #"time",
            #"timeit",
            #"tkColorChooser",
            #"tkCommonDialog",
            #"tkFileDialog",
            #"tkFont",
            #"tkMessageBox",
            #"tkSimpleDialog",
            #"toaiff",
            #"token",
            #"tokenize",
            #"trace",
            #"traceback",
            #"ttk",
            #"tty",
            #"turtle",
            #"types",
            #"unicodedata",
            #"unittest",
            #"urllib",
            #"urllib2",
            #"urllib3",
            #"urlparse",
            #"user",
            #"uu",
            #"uuid",
            #"vprof",
            #"warnings",
            #"wave",
            #"weakref",
            #"webbrowser",
            #"werkzeug",
            #"wheel",
            #"whichdb",
            #"wsgiref",
            #"xdrlib",
            #"xml",
            #"xmllib",
            #"xmlrpclib",
            #"xxsubtype",
            #"yaml",
            #"zipfile",
            #"zipimport"]