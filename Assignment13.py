import os
import sys
import hashlib
import time
import schedule
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import urllib.request as urllib2

def is_connected():
    try:
        urllib2.urlopen('http://www.google.com', timeout=5)
        return True
    except urllib2.URLError as err:
        print("URL Error:", err)
        return False

def MailSender(filename, time_str):
    try:
        fromaddr = "nikhilmole3@gmail.com"
        toaddr = "niikhilmole26y@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystem.
        Please find attached document which contains duplicate file deletion.
        Log file is created at : %s

        This is an auto-generated mail.

        Thanks and Regards,
        Piyush Manohar Kahirnar
        Marvellous Infosystem
        """ % (toaddr, time_str)

        subject = "Marvellous Infosystem Process Log generated at: " + time_str

        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        s.login(fromaddr, "tdoyvxfygsuqqesf")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Log file successfully sent through mail")

    except Exception as E:
        print("Unable to send mail.", E)

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    deleted_files = []

    if len(results) > 0:
        for result in results:
            for subresult in result[1:]:
                os.remove(subresult)
                deleted_files.append(subresult)
        print("Duplicate files deleted successfully")
    else:
        print("No duplicate files found")

    return deleted_files

def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if not flag:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is:" + dirName)
            for file in fileList:
                file_path = os.path.join(dirName, file)
                file_hash = hashfile(file_path)

                if file_hash in dups:
                    dups[file_hash].append(file_path)
                else:
                    dups[file_hash] = [file_path]
        return dups
    else:
        print("Invalid path")

def printResult(dict1, logfile, deleted_files):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    with open(logfile, 'w') as f:
        if len(results) > 0:
            print('Duplicates Found', file=f)
            print('The following files are duplicate:', file=f)
            for result in results:
                for subresult in result:
                    print('\t\t%s' % subresult, file=f)
        else:
            print("No duplicate files found", file=f)

        if deleted_files:
            print("\nDeleted Duplicate Files:", file=f)
            for file in deleted_files:
                print('\t\t%s' % file, file=f)
        else:
            print("No duplicate files were deleted", file=f)

def scheduled_task(path):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logfile = "DuplicateFilesLog_" + timestamp + ".txt"

    dups = findDup(path)
    deleted_files = DeleteFiles(dups)
    printResult(dups, logfile, deleted_files)

    if is_connected():
        MailSender(logfile, timestamp)

def main():
    print("------Marvellous Infosystem------")

    print("Application name: " + sys.argv[0])

    if (len(sys.argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
        print("This script is used to traverse a specific directory and delete duplicate files")
        exit()

    if ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        path = sys.argv[1]
        scheduled_task(path)

        schedule.every(1).minutes.do(scheduled_task, path)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
