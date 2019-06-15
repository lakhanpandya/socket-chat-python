import socket

from config import PORT, SERVER

class Client:
    def __init__(self):
        soc = socket.socket()
        soc.connect((SERVER, PORT))
        self.soc = soc
        msg = soc.recv(1024)
        print msg
        soc.close()


cl = Client()