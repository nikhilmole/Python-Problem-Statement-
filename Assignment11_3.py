import sys
import hashlib
import os

def hashfile(path, blocksize=1024):
    with open(path, 'rb') as fd:
        hasher = hashlib.md5()
        buf = fd.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = fd.read(blocksize)
    return hasher.hexdigest()

def FindDuplicate(path):
    if not os.path.isabs(path):
        path = os.path.abspath(path)
    
    if not os.path.isdir(path):
        print("Error: Provided path is not a directory")
        return {}

    dups = {}
    for foldername, subfoldername, filenames in os.walk(path):
        for name in filenames:
            filepath = os.path.join(foldername, name)
            file_hash = hashfile(filepath)
            if file_hash in dups:
                dups[file_hash].append(filepath)
            else:
                dups[file_hash] = [filepath]
    return dups

def CreateLog(Dubli, FolderName="Marvellous"):
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    FileName = os.path.join(FolderName, "Log.txt")

    with open(FileName, "a") as fd:
        separator = "-" * 70

        fd.write(separator + "\n")
        fd.write("Duplicate file log\n")
        fd.write(separator + "\n")

        for file_hash, file_list in Dubli.items():
            if len(file_list) > 1:
                fd.write(f"Hash: {file_hash}\n")
                for filepath in file_list:
                    fd.write(f"{filepath}\n")
                fd.write(separator + "\n")

def DeleteDublicates(clone):
    results = list(filter(lambda x: len(x) > 1, clone.values()))

    if len(results) > 0:
        for result in results:
            for subresult in result[1:]:
                try:
                    os.remove(subresult)
                    print(f"Deleted: {subresult}")
                except Exception as e:
                    print("Error deleting subresult: ".e)
    else:
        print("No duplicate files found")

def main():
    print("Application name:", sys.argv[0])

    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        exit()

    if (sys.argv[1] == '__h' or sys.argv[1] == "--H"):
        print("This script is used to traverse a specific directory and find duplicate files.")
        exit()

    if (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage: Provide a directory path to find and remove duplicate files, logging the deletions.")
        exit()

    try:
        duplicates = FindDuplicate(sys.argv[1])
        CreateLog(duplicates)
        DeleteDublicates(duplicates)
    except ValueError:
        print("Error: Invalid datatype of input")
    except Exception as e:
        print("An error occurred: ",e)

if __name__ == "__main__":
    main()
