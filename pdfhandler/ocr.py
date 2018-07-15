"""
PDF OCR

Description
-----------
This program optically recognizes characters on a PDF document

Author
------
Beom Jin Lee <cluesbj@berkeley.edu>
"""

import io
import os

from PIL import Image
import pytesseract
import subprocess


def pdf_converter(input_path, output_path=None):
    """Converts PDF to JPG images.

    Variables
    ---------
    input_path: path of the input PDF file
    output_path: path of the output JPG file.

    Source
    ------
    http://stackoverflow.com/a/36113000/4855984
    """
    if not output_path:
        # sets output path to the current directory
        output_path = input_path.split("/")[:-1]

    args = ["gs",
            "-dSafer",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE = jpeg",
            "-r144",
            "-sOutputFile = " + output_path,
            input_path]
    subprocess.call(args)


def ocr_pdf(path):
    """ Runs OCR on an input path

    Variables
    ---------
    path: path of the input JPG file (converted by pdf_converter)
    """
    image_pdf = Image(filename=path, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')
    full_text = ""
    page, total_pages = 0, len(image_jpeg.sequence)
    for img in image_jpeg.sequence:
        page += 1
        print("Processing page {} of {}".format(page, total_pages))
        img_page = Image(image=img).make_blob('jpeg')
        text = pytesseract.image_to_string(Image.open(img_page))
        full_text += text

    directory, doc = os.path.split(path)
    doc_name = os.path.splitext(doc)[0]
    f = open("{}/{}-ocr.txt".format(directory, doc_name), 'w')
    f.write(full_text)
    f.close()
    print("Successful OCR: {}".format(path))
