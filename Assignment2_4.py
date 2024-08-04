iSum = 0
def main():
    print("Please enter number :")
    Fact = int(input())
    global iSum

    for i in range(1, Fact, 1):
        if Fact % i == 0:
            iSum = iSum + i
    print(iSum, end = " ")
            

if __name__ == "__main__":
    main()