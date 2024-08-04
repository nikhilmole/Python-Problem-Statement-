#Design python application which contains two thread named as thread1 and thread2.
#thread 1 display 1 to 50  in reverse order on screen . After execution 
#of thread gets completed then sheduled thread2
import threading

def Display(iNo):
    for i in range(1, iNo , 1):
        print(i)

def DisplayRev(iNo):
    for i in range(iNo, 0, -1):
        print(i)

def main():
    print("Enter a number:")
    iValue = int(input())

    thread1 = threading.Thread(target=Display, args=(iValue,))
    thread2 = threading.Thread(target=DisplayRev, args=(iValue,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
   

if __name__ == "__main__":
    main()
