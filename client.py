import socket

SERVER_IP = "169.254.98.199"
SERVER_PORT = 8080
CHUNK_SIZE = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.connect(address)
    
    msg_recevd = sock.recv(CHUNK_SIZE)
    print(msg_recevd.decode('utf-8'))
    sock.close()