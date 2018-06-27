# PDF Handler

Author: Beom Jin Lee

This package allows parsing through a PDF document.

Prerequisites :
1. PyPDF2
2. pdfminer
3. interruptingcow
4. pytesseract

#### Sample Usage
```
>>> import pdf_checker
>>> one_document("/home/brian_lee/Desktop/PDF/pagerank.PDF")
1
```

#### Recommended Approach to Using PDFHandler
1. Inside the current directory, make a new directory where you can store your finished files. In Bash / Terminal, `cd` to your current directory and type:

    ```mkdir  <Name of Directory to Place Output Files>```

    The reason is that these functions, unless specifically defined, will output a TXT file with the same name, making it difficult to work through the files.
