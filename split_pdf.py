from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

import argparse
import os

if __name__ == "__main__":

    # adding a argument parser for CLI 
    parser = argparse.ArgumentParser()
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--filename", type=str, required=True)
    parser.add_argument("--chapters", type=int, nargs="+", required=True)
    args = parser.parse_args()

    # parse the CLI Arguments
    chapters = args.chapters
    offset = args.offset
    filename = args.filename

    # generate the output file name located in subfolder as Chapter_Index
    outputFolder= str(filename.split(".")[0])
    outputFilepath =  outputFolder + "/Chapter_{}.pdf"

    # read the pdf file
    infile = PdfFileReader(filename)

    # create new pdf directory
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # starts from 0 to set of 
    for chapterIndex in range(len(chapters)):

        start = chapters[ chapterIndex ] + offset
        
        # check if index is out of range
        if chapterIndex != len(chapters) -1:
            end = chapters[ chapterIndex+1 ] + offset - 1

        # set end index to the end of the book
        else:
            end = infile.getNumPages()

        # reinitialize he pdf writer, since the pages are stil stored 
        pdfwriter = PdfFileWriter()

        # walkthorugh pages and append to the pdf writer
        for pagenumber in range(start-1, end):
            pdfwriter.addPage(infile.getPage(pagenumber))

        # write to the output file
        with Path(outputFilepath.format( chapterIndex+1 )).open("wb") as out:
            pdfwriter.write(out)
