# Write a program which accept one number from user and return its factorial ?

def main():
    print("Please enter number :")
    Fact = int(input())
    f = 1
    i = 1
    for i in range(1 , Fact + 1):
        f = f*i
    print("Factorial :", f)
if __name__ == "__main__":
    main()