import os

def WriteLog(Message):
    fd = open("Log.txt","a")
    fd.write(Message+"\n")
    fd.close()

def CheckDirectory(DirName):
    if(os.path.exists(DirName) == False):
        WriteLog("Directory not found")
        return False

    if(os.path.isdir(DirName) == False):
        WriteLog("It is not a directory")
        return False

    return True