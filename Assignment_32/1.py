import sys
import os
import hashlib
from FileModule import CheckDirectory, WriteLog

def CalculateCheckSum(FileName):

    fobj = open(FileName,"rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):

        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryChecksum(DirName):

    try:
        if(CheckDirectory(DirName) == False):
            return

        WriteLog("--------------- Checksum Completed ---------------")

        for FolderName, SubFolder, FileNames in os.walk(DirName):
            for Fname in FileNames:
                path = os.path.join(FolderName,Fname)

                if(os.path.isfile(path)):
                    checksum = CalculateCheckSum(path)
                    WriteLog(path + " : "+checksum)

        WriteLog("--------------- Checksum Completed ---------------")

    except Exception as e:
        WriteLog("Exception occurred in 1.py file")

def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid number of arguments")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ =="__main__" :
    main()