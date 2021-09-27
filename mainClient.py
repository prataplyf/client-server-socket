from clientCore.ClientConnection import ClientConnection
from clientCore.handleConnection import handleConnection

if __name__ == "__main__":
    
    clientSocket = ClientConnection()
    
    clientSocket.CreateConnection("192.168.42.123", 8080)
    
    handleConnection(clientSocket)
    clientSocket.close()
    # print(clientSocket.ReceiveData())    
    # clientSocket.SendData("Hi this is client")