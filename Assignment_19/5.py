from functools import reduce

def ChkPrime(No):
    if(No <= 1):
        return False

    for i in range(2,No):
        if ((No%i) == 0):
            return False
    return True


def main():
    Data =[]
    No =int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    FData =list(filter(ChkPrime,Data))
    print("List after filter : ", FData)

    MData =list(map(lambda x : x*2 ,FData))
    print("List after map : ", MData)

    RData =reduce(lambda x,y : x if(x>y) else y ,MData)
    print("Output of reduce : ",RData)

if __name__ =="__main__" :
    main()
