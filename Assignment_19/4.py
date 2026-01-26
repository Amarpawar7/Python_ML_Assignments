from functools import reduce

def main():
    Data =[]
    No =int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    FData =list(filter(lambda x :x%2 == 0 ,Data))
    print("List after filter : ", FData)

    MData =list(map(lambda x : x*x ,FData))
    print("List after map : ", MData)

    RData =reduce(lambda x, y : x+y,MData)
    print("Output of reduce : ",RData)

if __name__ =="__main__" :
    main()
