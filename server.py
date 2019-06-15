import socket
import sys

from config import PORT, OPEN_CONNECTIONS

class Server:
    def __init__(self):
        try:
            soc = socket.socket() 
            soc.bind(("", PORT))
            soc.listen(OPEN_CONNECTIONS)
            self.soc = soc
            print "Socket is listening..."
        except Exception as e:
            print e
            sys.exit()

    def start_listening(self):
        try:
            while True:
                con, addr = self.soc.accept()
                print "Recieved connection from {}".format(addr)
                cs = ChatSession(con)
                cs.manage_session()
        except KeyboardInterrupt:
            self.soc.close()


class ChatSession:
    def __init__(self, con):
        self.con = con
        
    def manage_session(self):
            self.con.send("Hello, World!")
            self.con.close()



ser = Server()
ser.start_listening()