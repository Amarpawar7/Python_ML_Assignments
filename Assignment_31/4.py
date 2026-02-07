import sys
import os
from FileModule import CheckDirectory

def DirectoryCopyExt(Src,Dest,Extension):
    try:
        if(CheckDirectory(Src)==False):
            return

        if(os.path.exists(Dest)==False):
            os.mkdir(Dest)
        found = False

        for Foldername,Subfolderr,Filenames in os.walk(Src):
            for file in Filenames:
                if(file.endswith(Extension)):
                    source_path = os.path.join(Foldername, file)
                    destination_path = os.path.join(Dest,file)

                    fd1 = open(source_path,"rb")
                    fd2 = open(destination_path,"wb")

                    data = fd1.read()
                    fd2.write(data)

                    fd1.close()
                    fd2.close()

                    print(file," is copied")
            if(found == False):
                print("No such files found")

    except Exception:
        print("Exception occurred")

def main():
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return

    DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ =="__main__" :
    main()