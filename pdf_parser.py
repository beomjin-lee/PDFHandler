"""
PDF Parser

This program parses through a PDF and returns a txt file of the parsed PDF
if the program is parseable, based on pdf_checker.py

convert_pdf_to_txt will convert ONE PDF file, while convert_directory_to_txt
will convert an entire directory of PDF files.

@author Beom Jin Lee <cluesbj@berkeley.edu>
"""

import io
import re
import glob
import time
import pdf_checker
import pdfminer

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.pdfparser import PDFParser
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

def write_to_txt(txt, filename):
    """
    This function writes string to TXT file

    txt : string to write
    filename : Name of the file / directory the file should be placed
    """
    with open(filename, 'w') as file:
        file.write(txt)

def convert_pdf_to_txt(path, password = ""):
    """
    This function converts a PDF to TXT file

    path : path of the file to convert to TXT
    password : if the PDF file is locked, and needs to be unlocked, use this variable. Set to None by default
    """
    if one_document(path):
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        maxpages = 0
        caching = True
        pagenos=set()

        for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages = maxpages,
                                      password = password,
                                      caching = caching,
                                      check_extractable = True):
            interpreter.process_page(page)

        fp.close()
        device.close()
        extracted = retstr.getvalue()
        retstr.close()

        write_to_txt(extracted, "{}.txt".format(path))

def convert_directory_to_txt(directory):
    """
    This function converts an entire directory of PDF to TXT file

    directory : directory in which many PDFs are placed
    """
    for filename in glob.iglob('{}*.pdf'.format(directory)):
        convert_pdf_to_txt(filename)
