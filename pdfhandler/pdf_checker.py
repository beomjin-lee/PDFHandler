"""
PDF Checker

Description
-----------
This program checks whether a PDF document can be parsed, or not.

Sample Usage
------------
>>> import pdf_checker
>>> one_document("/home/brian_lee/Desktop/PDF/pagerank.PDF")
1

Author
------
Beom Jin Lee <cluesbj@berkeley.edu>
"""
import io
import re
import glob
import time
import PyPDF2
from interruptingcow import timeout


def one_document(path, waittime = 2, DEBUG = False):
    """ Update status on whether a single PDF document can be parsed.

    Variables
    ---------
    path: the path of
    waittime: time before program times out, set to 2s by default
    DEBUG: debug option that prints out success, set to False by default

    Return
    ------
    1: extractable
    0: needs to be OCR'd
    -1: Timeout error
    -2: Errors out somewhere else
    """
    try:
        with timeout(waittime, exception=RuntimeError):
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
