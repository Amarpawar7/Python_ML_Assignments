from functools import reduce

def main():
    Data =[]
    No =int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    FData =list(filter(lambda x : x>=70 and x<=90 ,Data))
    print("List after filter : ", FData)

    MData =list(map(lambda x : x+10 ,FData))
    print("List after map : ", MData)

    RData =reduce(lambda x, y : x*y ,MData)
    print("Output of reduce : ",RData)

if __name__ =="__main__" :
    main()
