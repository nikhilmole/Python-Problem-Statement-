# Write a program which accept number from user and return of digits in that numbers ?
def main():
    print("Please enter numbers to sum of digits")
    Add = input()
    Total = 0
    for i in range(0, len(Add)):
        Total = Total + int(Add[i])
    print(Total)

if __name__ == "__main__":
    main()