import sys
import os
from FileModule import CheckDirectory

def DirectoryRename(DirName, Ext1,Ext2):
    try:
        if CheckDirectory(DirName) == False:
            return

        for Foldername, Subfolderr, Filenames in os.walk(DirName):
            for file in Filenames:
                if file.endswith(Ext1):
                    oldname= os.path.join(Foldername,file)
                    newname= oldname.replace(Ext1,Ext2)
                    os.rename(oldname, newname)
                    print(file,"is renamed")


    except Exception:
        print("Exception occurred")

def main():
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return

    DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ =="__main__" :
    main()