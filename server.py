#importing modules
import socket
import threading

#variables
HOST = '127.0.0.1'
PORT = 1245
LIMIT = 5
#main function
def main():
    #AF_INET uses IPv4 addresses
    #SOCKET_STREAM is a protocol (using tcp protocol) for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the socket class object

#Error Handling
    try:
        server.bind((HOST, PORT)) #telling the server to bind "host" and "port" --> providing the server the address
        print(f"The server is running on {HOST}")
    except:
        print (f"unable to bind to {HOST} and {PORT})")


    #setting the limit for the server
    server.listen(LIMIT) #only allowing 5 connections at the same time. 

    #Listening to the client connections
    while 1:

        client, address = server.accept() #will keep on listening to any connections of the client (will give 2 values which is client and address)

        print(f"Successfully connected to the client {address[0]} {address [1]}")


if __name__ == '__main__':
    main()
