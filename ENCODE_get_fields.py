#!/usr/bin/env python
# -*- coding: latin-1 -*-
''' BASIC REPORTER SCRIPT
'''
import os.path
import argparse
import encodedcc


def getArgs():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument('--infile',
                        default='obList',
                        help="File containing a list of ENCSRs as a column")
    parser.add_argument('--outfile',
                        default='fields.tsv',
                        help="TSV file with fields, first line is column headings")
    parser.add_argument('--query',
                        help="A custom query to get accessions.")
    parser.add_argument('--key',
                        default='default',
                        help="The keypair identifier from the keyfile.  \
                        Default is --key=default")
    parser.add_argument('--keyfile',
                        default=os.path.expanduser("~/keypairs.json"),
                        help="The keypair file.  Default is --keyfile=%s" % (os.path.expanduser("~/keypairs.json")))
    parser.add_argument('--debug',
                        default=False,
                        action='store_true',
                        help="Print debug messages.  Default is False.")
    parser.add_argument('--fields',
                        help="File of fieldnames as column")
    args = parser.parse_args()
    return args


def main():
    args = getArgs()
    key = encodedcc.ENC_Key(args.keyfile, args.key)
    connection = encodedcc.ENC_Connection(key)
    encodedcc.get_fields(args, connection)

if __name__ == '__main__':
    main()
