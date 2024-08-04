import sys
import os
import glob

def files(file_name):
    print("File name is:", file_name)
    if os.path.exists(file_name):
        print("All file with .txt extension are :")
        for file in glob.glob("*.txt"):
            print(file)
    else:
        print(f"'{file_name}'does not exist in current Directory")

def main():
    if len(sys.argv) != 3:
        files(sys.argv[1])

if __name__ == "__main__":
    main()
