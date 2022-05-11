from fileinput import filename
import os

filenames = os.listdir(".")

if not os.path.exists("content.txt"):
    exit("Please create a file with content.txt")

content = open("content.txt").read().split("\n")

for filename in filenames:
    if "Chapter" in filename:
        # extract chapter number from name
        chapterIdx = int(filename.split("_")[1].split(".")[0])
        
        # replace a space with an underscore
        chapterName = content[chapterIdx - 1].replace(" ", "_")

        # build the new filename
        newFilename = str(chapterIdx) + "_" + chapterName + ".pdf"

        print(filename, newFilename)

        os.rename(filename, newFilename)