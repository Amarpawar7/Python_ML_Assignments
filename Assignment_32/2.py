import sys
import os
import hashlib
from FileModule import CheckDirectory,WriteLog

def CalculateCheckSum(FileName):

    fobj = open(FileName,"rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):

        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirName):

    try:
        if(CheckDirectory(DirName)==False):
            return

        Duplicate ={}

        for FolderName,SubFolder,FileNames in os.walk(DirName):
            for Fname in FileNames:
                Fname = os.path.join(FolderName,Fname)
                Checksum = CalculateCheckSum(Fname)

                if Checksum in Duplicate:
                    WriteLog("Duplicate file : " +Fname)
                
                else:
                    Duplicate[Checksum]=Fname

    except Exception:
        WriteLog("Exception occurred in 2.py file")

def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid number of arguments")
        return

    FindDuplicate(sys.argv[1])

if __name__ =="__main__" :
    main()