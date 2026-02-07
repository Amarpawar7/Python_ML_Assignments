import os

def CheckDirectory(DirName):
    if not os.path.exists(DirName):
        return False
    
    if not os.path.isdir(DirName):
        return False
    
    return True
