import psutil
import sys

def ProcInfo(ProName):
    found = False
    for proc in psutil.process_iter(['name', 'pid', 'username']):
        if proc.info['name'] == ProName:
            print(proc.info)
            found = True
    if not found:
        print("Process is not running")

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
        ProcInfo(sys.argv[1])

if __name__ == "__main__":
    main()
