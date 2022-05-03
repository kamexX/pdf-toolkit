==Explanation==

You would like to split a PDF File or a Ebook into several subfiles? But you dont want to waste your time to use "print to pdf" ? 

Then you should use the CLI Utility PDF Splitter, to split the PDF without bunch of work.

Just note the pagenumber of the chapters and the offset (these sites which are not included in your pdf page if you want to skip a part at the beginning)  

Then the script splits the pdf and stores the subfiles into a new folder, called like the pdfs filename.

==Installation==

pip install git+https://github.com/kamexx/pdf_splitter.git@main

==Usage==

* Move to the folder where your pdf is
cd folder/where/your/pdf/is

* call the python3 interpreter and the script name, with the parameters
/bin/python3 pdf_split.py --filename --offset --chapter

* Parameter to specify:
--filename: the name of the pdf file
--offset: the pages you want to skip until chapter 1
--chapter: list of pagenumbers where the chapter starts

* Example
cd my_pdf_collection/
/bin/python3 pdf_split.py --filename myscript.pdf --offset 18 --chapter 1 9 35 53 71 93 117 127 139 153 169


