# file-checker-py
Checks a given file, or all files within a given directory or set of files/directories, for tab characters as well as lines exceeding a given length (80 characters by default). Hidden files/subdirectories (i.e., starting with '.') are ignored by default. Additional functionality might be added...eventually.

Usage: `file_checker.py target [target2 ...] [--maxlen=n | --no-len-check | --no-tab-check | --check-hidden-files | --check-hidden-dirs]`

Written in Python by [David C. Drake](https://davidcdrake.com).
