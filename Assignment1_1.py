#1. Write a program which contains one function named as fun().That function should display "Hello From fun" on consol.

def DisplayR(Value):
    global i
    if(No >= 1):
        print(Value)
        Value = Value - 1
        DisplayR(Value)

def main():
    print("Enter Your Number : ")
    No = int(input())
    DisplayR(No)

if __name__ == "__main__":
    main()

def Fun():
    print("Hello from Fun")


def main():
    Fun()


if __name__ == "__main__":
    main()