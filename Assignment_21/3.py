import threading

iCnt =0
lobj =threading.Lock()

def Update():
    global iCnt
    for i in range(10):
        lobj.acquire()
        iCnt =iCnt + 1
        lobj.release()

def main():
    global iCnt

    T1 =threading.Thread(target=Update)
    T2 =threading.Thread(target=Update)
    T3 =threading.Thread(target=Update)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final value of counter : ",iCnt)

if __name__ == "__main__":
    main()
