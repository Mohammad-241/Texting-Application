#importing modules

import socket
import threading

#variables
HOST = '127.0.0.1'
PORT = 1245

#Listening messages from Server
def listening_messages_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~") [0]
            content = message.split('~') [1]

            print(f"[{username}] {content}")
        else:
            print("Message received from client is emptry")
            

#Sending Messages to the server
def sending_message_server(client):
    
    while 1:
        message = input("Message: ")

        if message != '':
            client.sendall(message.encode())
        else:
            print("Empty Message")
            exit(0)

#Talking to the server
def server_communicate(client):
    
    username = input("Enter username: ") #Inputting username 
    if username != '':
        client.sendall(username.encode()) #sending username to server
    else:
        print("Cannot be empty")
        exit(0)

    threading.Thread(target=listening_messages_server, args=(client, )).start()

    sending_message_server(client)

def main():
    
    #creating socket object

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connecting to server
    try:    
        client.connect((HOST, PORT))
        print("Connected to the server successfully")
    except:
        print(f"Unable to connect to {HOST} and {PORT}")

    server_communicate(client)

if __name__ == "__main__":
    main()
