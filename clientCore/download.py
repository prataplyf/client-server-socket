



def DownloadFile(socket):
    print("[+] Downloading Files")

    filename = socket.ReceiveData()
    socket.ReceiveFile(filename)