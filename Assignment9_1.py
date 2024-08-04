# 1.Write a program which accept file name from user and check whether that file exists in
# current directory or not
import os

def main():
    print("Enter the name of the file you want to open:")
    Fname = input()

    if os.path.exists(Fname):
        print("File is available in this directory.")
    else:
        print("does not exist in the directory.")

if __name__ == "__main__":
    main()
