# Write a program which accept N numbers from user and store it into list.Return additon of all prime numbers from that list.Main python file accept N numbers from user and pass each
#number to Chkprime() function with is part of our user defined module named as MarvellousNum.Name of 
#the main function from main python file shoulf be listprime()
import MrvellousNum

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    primes = []

    for i in range(n):
        num = int(input("Enter number {}: ".format(i+1)))
        numbers.append(num)

    for num in numbers:
        if MrvellousNum.ChkPrime(num):
            primes.append(num)

    print("Prime numbers:", primes)

if __name__ == "__main__":
    main()
