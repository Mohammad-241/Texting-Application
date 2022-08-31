#importing modules

import socket
import threading

#variables
HOST = '127.0.0.1'
PORT = 1245

def main():
    
    #creating socket object

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connecting to server
    try:    
        client.connect((HOST, PORT))
        print("Connected to the server successfully")
    except:
        print(f"Unable to connect to {HOST} and {PORT}")


if __name__ == "__main__":
    main()
