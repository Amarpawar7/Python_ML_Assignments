import os

def main():
    FileName =input("Enter the name of the file : ")

    if os.path.exists(FileName):
        fobj =open(FileName, "r")

        for line in fobj:
            print(line,end=" ")

        fobj.close()
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()
