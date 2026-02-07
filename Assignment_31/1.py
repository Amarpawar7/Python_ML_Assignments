import sys
import os
from FileModule import CheckDirectory

def DirectoryFileSearch(DirName, Extension):
    try:
        if CheckDirectory(DirName) == False:
            return

        print("Files with extension", Extension, "are :")

        for Foldername, Subfolderr, Filenames in os.walk(DirName):
            for file in Filenames:
                if file.endswith(Extension):
                    print(file)

    except Exception:
        print("Error while searching files")

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return

    DirectoryFileSearch(sys.argv[1],sys.argv[2])

if __name__ =="__main__" :
    main()