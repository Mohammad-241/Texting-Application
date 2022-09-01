#importing modules
import socket
import threading

#variables
HOST = '127.0.0.1'
PORT = 1245
LIMIT = 5
active_clients = [] #List of connected users currently


#Listenining for any upcoming messages from a client
def message_listener(client, username):
    
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_message(final_msg)

        else:
            print(f"The message send from client {username} is empty")


#Sending Message to single client Function
def send_message_client(client, message):

    client.sendall(message.encode())

#Messaging Function to all the clients that are connected to server
def send_message(message):
    
    for user in active_clients:

        send_message_client(user[1], message)


#Handling Client Function
def handle_client(client):
    
    #Server Listening to message from client that contains username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_message(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=message_listener, args=(client, username, )).start()

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

        threading.Thread(target = handle_client, args = (client, )).start() #threads will handle the clients function. 

if __name__ == '__main__':
    main()
