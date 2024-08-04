import os
from sys import *
import hashlib
import sys

def filehash(path, blocksize=124):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)

    if(flag == False):
        os.path.abspath(path)

    exist = os.path.isdir(path)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(path):
            print("Current folder is: ",foldername)
            for name in filename:
                filepath = os.path.join(foldername,name)
                file_hash = filehash(filepath)
                print(filepath)
                print(file_hash)
                print(' ')


def main():

    print("Application name:",sys.argv[0])

    if(len(sys.argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("This script is used to traverse specific directory and display checksum")
        exit()

    if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage: display all files checksum which is available inside the current directory")
        exit()

    try:
        DisplayCheckSum(argv[1])
    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input:",E)
    

if __name__ == "__main__":
    main()