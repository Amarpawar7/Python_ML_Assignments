# Copying content by taking user input

import os

def main():
    SourceFile =input("Enter the source file name : ")
    DestFile =input("Enter the destination file name : ") # if not created it will be created

    if os.path.exists(SourceFile):
        fobj1 = open(SourceFile ,"r")
        fobj2 =open(DestFile ,"w")

        fobj2.write(fobj1.read())

        print("Contents copied successfully")

        fobj1.close()
        fobj2.close()

    else:
        print("File does not exist")

if __name__ =="__main__" :
    main()
