# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.1.134', port))
#%%
# receive data from the server and decoding to get the string.
x = input()
print("sending:", x)
s.send((str(x) + "\n").encode())
#%% close the connection
s.close()

#%%
