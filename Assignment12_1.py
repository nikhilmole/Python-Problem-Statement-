import psutil

def ProcInfo():
    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)
        
def main():
    print("Usage : List of running process")
    print("-------------------------------------------------")

    ProcInfo()

    print("-------------------------------------------------")
if __name__ == "__main__":
    main()