import os
import sys
import shutil

def Copy(source, destination):
    try:
        os.makedirs(destination, exist_ok=True)
    
        shutil.copy(source, destination)
        
        print("File copied successfully.")
    except Exception as eobj:
        

def main():
    
    if len(sys.argv) != 3:
        return

    source_file = sys.argv[1]
    destination_dir = sys.argv[2]

    Copy(source_file, destination_dir)

if __name__ == "__main__":
    main()
