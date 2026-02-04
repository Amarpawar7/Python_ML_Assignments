import os

def main():
    FileName =input("Enter the name of the file : ")

    if os.path.exists(FileName):
        fobj =open(FileName,"r")

        Count =0
        for line in fobj:
            Count = Count+1

        print("Total number of lines are : ",Count)

        fobj.close()
    else:
        print("File does not exist")

if __name__=="__main__" :
    main()
