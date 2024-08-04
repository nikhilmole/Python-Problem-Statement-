# Accept file name and one string from user and return the frequency of that string from file
import os
import sys

def StringFreq(file_name, target_string):
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        content = file.read()
        freq = content.count(target_string)
        print(f"The frequency of '{target_string}' in {file_name} is: {freq}")
    else:
        print(f"The file '{file_name}' does not exist.")

def main():
    if len(sys.argv) != 3:
        return
    else:
        file_name = sys.argv[1]
        target_string = sys.argv[2]
        StringFreq(file_name, target_string)

if __name__ == "__main__":
    main()
