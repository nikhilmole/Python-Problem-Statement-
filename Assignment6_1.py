#Design python application which creates two thread named as even or odd.
#Even thread display first 10 even numbers and odd thread will display first 10 
#odd numbers.

import threading

def EvenDisplay(iNo):
    print("Even numbers are :")
    for i in range(1, iNo + 1):
        if (i % 2 == 0):
            print(i)

def OddDisplay(iNo):
    print("Odd numbers are :")
    for i in range(1, iNo + 1):
        if (i % 2 != 0):
            print(i)

def main():
    iValue = 10
    even = threading.Thread(target=EvenDisplay, args=(iValue,))
    odd = threading.Thread(target=OddDisplay, args=(iValue,))

    even.start()
    even.join()

    odd.start()
    odd.join()

    print("Exit main")

if __name__ == "__main__":
    main()
