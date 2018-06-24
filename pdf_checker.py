"""
PDF Checker

This program checks whether a PDF document can be parsed, or not.

@author Beom Jin Lee <cluesbj@berkeley.edu>
"""

import io
import re
import glob
import time
import PyPDF2
from interruptingcow import timeout

class PDFText:
    def __init__(self, directory):
        """
        Initializes class PDFText.

        Sets extractable_num = 0
        Sets non_extractable_num = 0
        These will be used to differentiate multiple PDF files
        """
        self.raw_extract = ""
        self.directory = directory
        self.extractable_num = 0
        self.non_extractable_num = 0

    def convert_pdf_to_txt(self, path):
        """
        This function takes in a file path and returns:
            1. Text of PDF if PDF can be parsed
            2. False if PDF cannot be parsed
        """
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        pdf = PyPDF2.PdfFileReader(open(path, "rb"))
        num_of_pages = pdf.getNumPages()
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
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

        if len(extracted) / num_of_pages < 200:
            self.raw_extract = extracted
            self.non_extractable_num += 1
            return False

        else:
            self.raw_extract = extracted
            self.extractable_num += 1
            return True

    def write_to_txt(self, txt, file_name):
        """
        Writes string to .txt file
        """
        with open(file_name, 'w') as file:
            file.write(txt)

    def turn_directory(self):
        """
        Turns entire directory of .pdf to .txt
        """
        for filename in glob.iglob('{}*.pdf'.format(self.directory)):
            extractable = self.convert_pdf_to_txt(filename)
            if extractable:
                self.write_to_txt(self.raw_extract, "extractable{}.txt".format(self.extractable_num))
            else:
                self.write_to_txt("Not extractable \n {}".format(self.raw_extract), "non-extractable{}.txt".format(self.non_extractable_num))

def one_document(path, waittime = 2, DEBUG = False):
    """
    This function will update status on whether a SINGLE PDF document can be parsedself.

    path : the path of
    waittime : time before program times out, set to 2 by default
    DEBUG : debug option that prints out success, set to False by default

    @return
        1: extractable
        0: needs to be OCR'd
        -1: Timeout error
        -2: Errors out somewhere else
    """
    try:
        with timeout(waittime, exception = RuntimeError):
            pdf = PyPDF2.PdfFileReader(open(path, "rb"))
            num_of_pages = pdf.getNumPages()
            current_page = 1

            while current_page < num_of_pages and current_page < 5:
                page_object = pdf.getPage(current_page)
                extracted = page_object.extractText()
                if len(extracted) < 200:
                    continue
                else:
                    if DEBUG:
                        print("Page is extractable")
                    return 1
                    break

            if DEBUG:
                print("Page is not extractable")
            return 0
    except RuntimeError:
        return -1
    except Exception:
        return -2
