import sys
import os
from FileModule import CheckDirectory

def DirectoryCopy(Src,Dest):
    try:
        if(CheckDirectory(Src) ==False):
            return

        if(os.path.exists(Dest) ==False):
            os.mkdir(Dest)

        for Foldername,Subfolderr,Filenames in os.walk(Src):
            for file in Filenames:
                source_path =os.path.join(Foldername,file)
                destination_path = os.path.join(Dest,file)

                if os.path.isfile(source_path):
                    fd_src= open(source_path,"rb")
                    fd_dest= open(destination_path,"wb")

                    data =fd_src.read()
                    fd_dest.write(data)

                    fd_src.close()
                    fd_dest.close()

                    print(file," is copied")

    except Exception:
        print("Exception occurred")

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()