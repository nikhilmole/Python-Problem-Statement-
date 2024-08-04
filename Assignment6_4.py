#Design puython application which creates three threads as small,capital,digits.
#All the threads accept string as parameter.Small thread display number of small charecters,
#capital thread display number of capital charecters and digits thread display number of digits.Display id and name of each thread
import threading

def CapitalCharNum(Let):
    UpCount = 0
    print("ID of CapitalCharNum :", threading.get_ident())
    UpCount = sum(1 for char in Let if char.isupper())
    print("Number of capital characters:", UpCount)
    

def SmallCharNum(Let):
    SmCount = 0
    print("ID of SmallCharNum :", threading.get_ident())
    SmCount = sum(1 for char in Let if char.islower())
    print("Number of small characters:", SmCount)
    

def DigitsNum(Let):
    LetCount = 0
    print("ID of DigitNum :", threading.get_ident())
    LetCount = sum(1 for char in Let if char.isdigit())
    print("Number of digits:", LetCount)
    

def main():
    String = '\0'
    print("Enter Word")
    String = (str(input()))
    capital = threading.Thread(target=CapitalCharNum, args=(String,))
    small = threading.Thread(target=SmallCharNum, args=(String,))
    digits = threading.Thread(target=DigitsNum, args=(String,))
    
    capital.start()
    small.start()
    digits.start()

    capital.join()
    small.join()
    digits.join()

    print()
if __name__ == "__main__":
    main()
