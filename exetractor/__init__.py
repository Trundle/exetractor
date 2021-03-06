# -*- coding: utf-8 -*-

"""
    exetractor
    ~~~~~~~~~~

    A far from complete unpacker for packed Python executables.

    :copyright: (c) 2009 by Andreas Stührk
    :license: modified BSD, see LICENSE for more details.
"""

from __future__ import with_statement

import sys


__version__ = '0.1'
__license__ = 'modified BSD'


def main(args=sys.argv[1:]):
    from exetractor import py2exe, pyinstaller
    if len(args) != 1:
        print >> sys.stderr, 'Usage: exetract <path to exe>'
        return 1
    with open(args[0], 'rb') as exe_file:
        exe_data = exe_file.read()
    if py2exe.is_valid_data(exe_data):
        py2exe.unpack(exe_data)
    elif pyinstaller.is_valid_data(exe_data):
        pyinstaller.unpack(exe_data)
    else:
        print >> sys.stderr, 'unsupported file type'
        return 1
    return 0


if __name__ == '__main__':
    main()
