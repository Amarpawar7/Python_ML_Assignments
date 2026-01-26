import threading

def ChkPrime(No):
    if(No <= 1):
        return False
    for i in range(2 ,No):
        if(No%i == 0):
            return False
    return True

def Prime(Data):
    print("Prime Numbers : ")
    for i in Data:
        if ChkPrime(i):
            print(i,end=" ")
    print()

def NonPrime(Data):
    print("Non-Prime Numbers : ")
    for i in Data:
        if not ChkPrime(i):
            print(i,end=" ")
    print()

def main():
    Data=[]
    No =int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    T1 = threading.Thread(target=Prime , args=(Data,) , name="Prime")
    T2 = threading.Thread(target=NonPrime , args=(Data,) , name="NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
