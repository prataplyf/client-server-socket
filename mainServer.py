from serverCore.ServerConnection import ServerConnection
from serverCore.handleConnection import handleConnection




if __name__ == "__main__":
    print("[+] waiting for client...\n")
    serverSocket = ServerConnection()
    serverSocket.CreateConnection("", 8080)
    
    serverSocket.Listen()
    conn, _ = serverSocket.AcceptConnect()
    
    handleConnection(serverSocket)
    # serverSocket.SendData("Hi this is server")
    # print(serverSocket.ReceiveData())
    conn.close()
    # serverSocket.close()