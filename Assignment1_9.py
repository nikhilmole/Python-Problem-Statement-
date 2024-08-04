# Write a program which display first 10 numbers on screen ?

def main():
    print("Even numbers in 1 to 20 are :")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end = ' ')


if __name__ == "__main__":
    main()