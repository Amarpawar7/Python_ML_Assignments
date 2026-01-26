import threading

def Maximum(Data):
    Max =Data[0]
    for i in Data:
        if(i>Max):
            Max=i
    print("Maximum element : ",Max)

def Minimum(Data):
    Min =Data[0]
    for i in Data:
        if(i<Min):
            Min=i
    print("Minimum element : ",Min)

def main():
    Data = []
    No = int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    T1 = threading.Thread(target=Maximum , args=(Data,) , name="Maximum")
    T2 = threading.Thread(target=Minimum , args=(Data,) , name="Minimum")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
