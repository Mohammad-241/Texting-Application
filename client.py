#importing modules
import socket
from statistics import median
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

#variables
HOST = '127.0.0.1'
PORT = 1245

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)
WHITE = "white"
LIGHT_GREY = '#D3D3D3'

#creating socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
        
    #connecting to server
    try:    
        client.connect((HOST, PORT))
        print("Connected to the server successfully")
        add_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to {HOST} and {PORT}")
    
    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode()) #sending username to server
    else:
        messagebox.showerror("Invalid Username", "Cannot be empty")

    threading.Thread(target=listening_messages_server, args=(client, )).start()

    username_textbox.config(state = tk.DISABLED)
    username_button.config(state = tk.DISABLED)

def send_message(): #sending message to server
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message)) #empties the message textbox after sending message
    else:
        messagebox.showerror("Empty MEssage", "Message cannot be empty")

   
#initializing tkinter (gui box)
root = tk.Tk()
root.geometry("600x600") #Changing width and length of GUI
root.title("Texting Client") #GUI Title
root.resizable(False, False) #GUI not resizable

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 4)
root.grid_rowconfigure(2, weight = 1)

#Framing
top_frame =tk.Frame(root, width = 600, height = 100, bg = DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width = 600, height = 400, bg = MEDIUM_GREY)
middle_frame.grid(row = 1, column = 0, sticky = tk.NSEW)

bottom_frame = tk.Frame(root, width = 600, height = 100, bg = DARK_GREY)
bottom_frame.grid(row = 2, column = 0, sticky = tk.NSEW)

#label on top of gui
username_label = tk.Label(top_frame, text="Enter Username:", font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx= 10)

#textbox at top of gui
username_textbox = tk.Entry(top_frame, font = FONT, bg=MEDIUM_GREY, fg=WHITE, width = 23)
username_textbox.pack(side=tk.LEFT)

#button on top of gui (join)
username_button = tk.Button(top_frame, text = "Join", font=BUTTON_FONT, bg=LIGHT_GREY, fg=WHITE, command = connect)
username_button.pack(side=tk.LEFT, padx = 15)

#message textbox
message_textbox =tk.Entry(bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=35)
message_textbox.pack(side=tk.LEFT, padx=10)

#send button
message_button = tk.Button(bottom_frame, text = "Send", font=BUTTON_FONT, bg= LIGHT_GREY, fg = WHITE, command = send_message)
message_button.pack(side=tk.LEFT, padx = 15)

#message box
message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg = MEDIUM_GREY, fg=WHITE, width = 70, height = 26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


#Listening messages from Server
def listening_messages_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~") [0]
            content = message.split('~') [1]

            add_message(f"[{username}] {content}")
        else:
            messagebox.showerror("Error", "Message received from client is empty")
            

def main():
    
    root.mainloop() #start the loop of tkinter

if __name__ == "__main__":
    main()
