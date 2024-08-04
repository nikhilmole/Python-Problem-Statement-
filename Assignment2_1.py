# creat on module named as Arithematic which contains 4 function as Add() for additon,Sub()
# for substraction, Mult() for multiplicatiion and Div() for division. All function accept 
# two parameters as number and perform the operation. Write on python program which call all 
# the function from Arithematic module by accepting the parameters form user. 
import Arithematic
def main():
    print("Enter first number :")
    No1 = int(input())
    print("Enter second number :")
    No2 = int(input())
    Result = 0

    Result = Arithematic.Add(No1, No2)
    print("Addition is :", Result)

    Result = Arithematic.Sub(No1, No2)
    print("Substraction is :", Result)

    Result = Arithematic.Mult(No1, No2)
    print("Multiplication is :", Result)

    Result = Arithematic.Div(No1, No2)
    print("Division is :", Result)

if __name__ == "__main__":
    main()