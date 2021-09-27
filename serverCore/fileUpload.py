# read file from the disk {hacker Machine | Server side}
# read it in the form of bytes
# append a delimeter to the end of the file
# transfer the file over a network
# receive file on client side
# remove the delimeter from the the bytes to recover the original data
# write the file to the client disk

from glob import glob
from typing import get_origin
import os


def upload_files(serverSocket):
    print("[+] Upload file")
    path = "Document/"
    files = glob(path + "*")
    for index, filename in enumerate(files):
        filename = os.path.basename(filename)
        print("\t\t", index, ": ", filename)

    
    while True:
        try:
            fileIndex = int(input("[+] Select File: "))
            if len(files) >= fileIndex >= 0:
                fileName = files[fileIndex]
                break
        except Exception as e:
            print("[-] Invalid file selected")
    
    print("[+] Selected File: ", fileName)
    serverSocket.SendData(fileName)
    serverSocket.SendFile(filename, path)



