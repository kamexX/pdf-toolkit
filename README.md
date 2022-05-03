# Explanation

You would like to split a PDF File or an eBook into several subfiles? But you don't want to waste your time to use "print to pdf"? 

Then you should use the CLI Utility pdfsplit, to split the PDF without bunch of work.

Just note the pagenumber of each chapters and the offset (these sites which are not included in your pdf page if you want to skip a part at the beginning)

Then the script splits the pdf and stores the subfiles into a new folder, called like the pdfs filename.

# Installation

/bin/python3 -m pip install git+https://github.com/kamexx/pdf_splitter.git@main

# Usage

1. cd folder/where/your/pdf/is

2. /bin/python3 -m pdfsplit.pdfsplit --filename "str" --offset int --chapter int int int int int int

3. Parameter to specify:
- filename: the name of the pdf file
- offset: the pages you want to skip until chapter 1
- chapter: list of pagenumbers where the chapter starts

4. optional you can add the python package to your PATH folder, so you can run it without /bin/python3 -m pdfsplit.pdfsplit 

# Example
- cd my_pdf_collection/
- /bin/python3 -m pdfsplit.pdfsplit --filename myscript.pdf --offset 18 --chapter 1 9 35 53 71 93 117 127 139 153 169


