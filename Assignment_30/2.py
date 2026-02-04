import os

def main():
    FileName =input("Enter the name of the file : ")

    if os.path.exists(FileName):
        fobj=open(FileName, "r")

        Data =fobj.read()
        Words =Data.split()

        print("Total number of words are : ",len(Words))

        fobj.close()
    else:
        print("File does not exist")

if __name__=="__main__" :
    main()
