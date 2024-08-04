import os
import sys

def Rename(Rename_file):
    print("Current file name is :", Rename_file) 

    if os.path.exists(Rename_file): 
        new_file_name = 'Demo.doc' 
        os.rename(Rename_file, new_file_name) 
        print(f"File '{Rename_file}' renamed to '{new_file_name}'.")
    else:
        print("File does not exist.")

def main():
    if len(sys.argv) != 2:
        return
    Current_file = sys.argv[1]
    Rename(Current_file)

if __name__ == "__main__":
    main()
