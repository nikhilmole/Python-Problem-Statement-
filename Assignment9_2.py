# 2.write a program which accept file name from user and open that file and display the contents
# of that file on screen

import os

def main():
    print("Enter the file name you want to open for reading purpose :")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"r")
        print("File is successfully open in read mode")

        Data = fobj.read()

        print(Data)

        fobj.close()

    else:
        print("Unable to open file is not present in the current directory")

if __name__ == "__main__":
    main()