#Design python application which creates two thread as evenlist and oddlist. Both the threads accept list of integers as pameter
#Evenlist thread add all even elements from input list and display the addition.
#oddlist thread add all odd element from input list and display the addition
import threading

def EvenSum(iNo, iSize):
    EvenSum = 0
    print("Even numbers: ", end = '  ')
    for i in range(iSize):
        if((iNo[i] % 2) == 0):
            print(iNo[i],end = '  ')
            EvenSum = EvenSum + iNo[i]
    print("Sum of even numbers:", EvenSum)

def OddSum(iNo, iSize):
    OddSum = 0
    print("Odd numbers :" ,end = '  ')
    for i in range(iSize):
        if((iNo[i] % 2) != 0):
            print(iNo[i],end = '  ')
            OddSum = OddSum + iNo[i]
    print("Sum of odd numbers:", OddSum)

def main():
    Size = 0
    List = []
    No = 0
    print("Enter Frequency")
    Size = int(input())

    print("Enter Numbers")
    for i in range(Size):
        No = int(input())
        List.append(No)
    print("List:", List)

    evenlist = threading.Thread(target=EvenSum, args=(List, Size,))
    oddlist = threading.Thread(target=OddSum, args=(List, Size,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

if __name__ == "__main__":
    main()
