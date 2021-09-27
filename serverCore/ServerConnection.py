import socket

DELIMETER = "<END_OF_THE_RESULTS>"
CHUNK_SIZE = 20*1024

class ServerConnection:
    
    def __init__(self):
        """
            Creates a TCP socket for server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def CreateConnection(self, ip= "", port=8080):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.socket.bind(self.address)
    
    def Listen(self, backlog = 5):
        self.socket.listen(backlog)
    
    def AcceptConnect(self):
        self.client_conn, self.client_address = self.socket.accept()
        print("\t\t[+] Connection established with " + str(self.client_address[0]) + " on port "+ str(self.client_address[1]) + "\n\n")
        return (self.client_conn, self.client_address)
    
    def SendData(self, user_input):
        user_input_bytes = bytes(user_input.encode("latin-1"))
        self.client_conn.send(user_input_bytes)
    
    def ReceiveData(self):
        received_data_bytes = self.client_conn.recv(CHUNK_SIZE)
        self.data = received_data_bytes.decode("latin-1")
        return self.data
    
    def ReceiveCommandResult(self):
        print("[+] Getting Command Results")
        result = b''
        while True:
            chunk = self.client_conn.recv(CHUNK_SIZE)
            if chunk.endswith(DELIMETER.encode()):
                chunk += chunk[:-len(DELIMETER)]

                result += chunk
                break
            result += chunk
        print(result.decode('latin-1'))
    
    def SendFile(self, filename, path):
        print("[+] Sending File")
        filename = path+filename
        with open(filename, "rb") as file:
            chunk = file.read(CHUNK_SIZE)
            while len(chunk) > 0:
                self.client_conn.send(chunk)
                chunk = file.read(CHUNK_SIZE)
            
            self.client_conn.send(DELIMETER.encode('latin-1'))
    
   