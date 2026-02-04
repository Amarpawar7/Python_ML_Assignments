import os

def main():
    FileName = input("Enter the name of the file : ")
    Word = input("Enter the word to search : ")

    if os.path.exists(FileName):
        fobj = open(FileName ,"r")
        Data =fobj.read()

        if Word in Data:
            print(Word ,"is found in ",FileName)
        else:
            print(Word ,"is not found in ",FileName)

        fobj.close()
    else:
        print("File does not exist")

if __name__=="__main__" :
    main()
