import threading

SumResult =0
ProductResult =1

def SumList(Data):
    global SumResult
    for i in Data:
        SumResult =SumResult+i

def ProductList(Data):
    global ProductResult
    for i in Data:
        ProductResult =ProductResult*i

def main():
    global SumResult,ProductResult

    Data=[]
    No =int(input("Enter number of elements : "))

    for i in range(No):
        Data.append(int(input()))

    t1 = threading.Thread(target=SumList,args=(Data,),name="SumThread")
    t2 = threading.Thread(target=ProductList,args=(Data,),name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements : ",SumResult)
    print("Product of elements : ",ProductResult)

if __name__ == "__main__":
    main()
