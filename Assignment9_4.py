# write a program which accept two number from user and compare contents of both the files. is both the files
# contains same contents then display sccess otherwise display failure.
import sys
import os

def compare_files(file1, file2):
    try:
        if os.path.exists(file1):
            f1 = open(file1,'r')
            f2 = open(file2,'r')

            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                print("Both files contain the same contents.")
            else:
                print("Contents of the files are different.")
    except FileNotFoundError:
        print("One or both of the files does not exist.")

def main():
    if len(sys.argv) != 3:
        return
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        print(f"Comparing contents of {file1} and {file2}")
        compare_files(file1, file2)

if __name__ == "__main__":
    main()
