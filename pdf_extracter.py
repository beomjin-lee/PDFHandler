"""
PDF Extracter
-------------

Description
-----------
Combines the features of pdf_parser and ocr, to create a global PDF extracter

Author
------
Beom Jin Lee <cluesbj@berkeley.edu>
"""
import sys
import os

import pdf_checker
import ocr
import pdf_parser


def extract_file(path):


def extract_directory(path):


def main(path):
    if os.isfile(directory):
        extract_file(directory)
    elif os.isdir(directory):
        extract_directory(path)


if __name__ == '__main__':
    path = sys.argv[0]
    main(path)
