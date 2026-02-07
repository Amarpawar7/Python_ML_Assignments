import sys
import os
import hashlib
import time
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

def RemoveDuplicate(FileName):
    starttime =time.ctime()

    try:
        if(CheckDirectory(FileName) == False):
            return

        Duplicate = {}

        for FolderName,SubFolder,FileNames in os.walk(FileName):
            for fname in FileNames:
                fname = os.path.join(FolderName,fname)
                Checksum = CalculateCheckSum(fname)

                if Checksum in Duplicate:
                    os.remove(fname)
                    WriteLog("Deleted duplicate file : " + fname)
                else:
                    Duplicate[Checksum] = fname

        endtime =time.ctime()
        WriteLog("Execution time : " + str(endtime-starttime))

    except Exception:
        WriteLog("Exception occurred in 4.py file")

def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid number of arguments")
        return

    RemoveDuplicate(sys.argv[1])

if __name__ =="__main__" : 
    main()
