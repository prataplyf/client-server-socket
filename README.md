# client-server-socket


Server client connections are high priority topics nowadays. This use in the field of P2P communication and sometimes for Hacking (where a Hacker can hide from the client to still client data). Here I'm going to tell you that how to make a connection between client and serve.
In this session, I'm going to use SOCKET and show a demo, where a server can waiting for the client and as the client comes into his network he'll attack/send messages to the client system.
I'm going to create 2 files one on the server-side and the client-side.
I want to create an IPv4 connection because I want to create a TCP socket and this TCP socket work with the IP address of IPV4.
To establish a connection I'm using socket.AF_INET tells the compiler to select the IPv4 version and socket.SOCK_STREAM and tells the compiler to use the TCP streams and pass these two variables in socket.socket() method that'll return an object that helps in binding a connection that coming from the clients.
