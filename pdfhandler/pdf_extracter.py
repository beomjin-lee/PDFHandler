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

########################
# INITIALIZE VARIABLES #
########################

path = sys.argv[0]

##############
# EXTRACTION #
##############

def extract_file(path):
    """ Extracts a PDF file into a TXT file

    Variables
    ---------
    path: path of the PDF file to be extracted 
    """


def extract_directory(path):


########
# MAIN #
########

def main(path):
    if os.isfile(directory):
        extract_file(directory)
    elif os.isdir(directory):
        extract_directory(path)


if __name__ == '__main__':
    main(path)
