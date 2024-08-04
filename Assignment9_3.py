#3.Write a program which accept file name from user and creat new file named as Demo.txt and copy all content from existing
# file.Accept file name through command line arguments.
# inputs : ABC.txt
# Creat bew file as Demo.txt and copy contents of ABC.txt in Demo.txt  
import os

def main():
    
    f1 = open("Demo.txt",'r')
    f2 = open('ABC.txt','w') 

    data = f1.readlines()
    for line in data:
        f2.write(line)

    f1.close()
    f2.close()

if __name__ == "__main__":
    main()
