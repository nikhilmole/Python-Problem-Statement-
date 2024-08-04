import psutil
import sys

def CreatLog(Foldername = "Demo"):

    if no os.path.exist(FolderName):
        os.makdir(FolderName)

    FilName = os.path.join(FolderName,"Demo.txt")

    fd = open(FileName,"a")
    separator = "-" * 70

    fd.write(Separator + "\n")
    fd.write("Demo Process Log" + "\n")
    fd.write(separator + "'\n")

    Arr = ProcInfo()

    for data in Arr:
        fd.write("%s \n" %data)

    fd.write(separator = "\n")
    fd.close()
    
def procInfo():
    listprocess = []
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)

    return listprocess


def main():
    print("Application name:", sys.argv[0])

    if len(sys.argv) != 2:
        print("Use option --h to get the help and use --u to get the usage of this application")
        exit()
    
    if sys.argv[1] == "--h" or sys.argv[1] == "--H":
        print("This script is used to display running processes")
        exit()
    elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
        print("Usage: ApplicationName Running_Processes")
        exit()
    else:
        ProcInfo()

if __name__ == "__main__":
    main()
