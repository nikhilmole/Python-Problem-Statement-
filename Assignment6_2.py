#Design python application which creates two threads as evenfactor and oddfactor.Both the thread accept one parameter as integer.
#evenfactor thread will display adition of even factors of given number and oddfactor will display additon of odd factors of given number 
#After execution of both the thread gets completed main thread should display message as "exit from main".

import threading
def EvenFactorSum(iNo):
    ESum = 0
    print("Even Factors")
    for i in range(1,iNo,1):
        if(iNo % i == 0):
            print(i)
            ESum = ESum + i
    print("Summation of Evenfactor are :", ESum)

def OddFactorSum(iNo):
    FSum = 0
    print("Odd Factors")
    for i in range(1, iNo,1):
        if(iNo %  i != 0):
            print(i)
            FSum = FSum + i
    print("Sumation of oddfactor are :", FSum)

def main():
    iValue = 0
    print("Enter Number")
    iValue = int(input())

    evenfactor = threading.Thread(target = EvenFactorSum, args =(iValue,))
    oddfactor = threading.Thread(target = OddFactorSum, args =(iValue,))

    evenfactor.start()
    oddfactor.start()
    evenfactor.join()
    oddfactor.join()

    print("Exit from main")
if __name__ == "__main__":
    main()