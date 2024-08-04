# Write a program which contains ine function named as ChkNum() which accept thwo numbers
# from user and return addition of that two numbers ?
#         Algorithm
#   START
#       Accept two number as no1 and no2
#       Perform the Addition of two numbers
#       Display Addithion
#   STOP


#############################################
#    Function name : Add
#    Description : Perform Addition of 11 & 5
#    Input : Integer
#   Output : Integer 
#    Author Name :
#    Date :  
###############################################
def Add(Value1, Value2):
    Result = 0
    Result = Value1 + Value2
    return Result

def main():
    Ans = 0
    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ans = Add(No1, No2)
    print('Addition of two Number is :', Ans)

if __name__ == "__main__":
    main()