import threading
import socket

#Create A Chat Room
class create_room(object):
    def __init__(self, mclient, ipaddr, port):
        self.usernameList = []
        self.PORT = port
        self.HOST = ipaddr
        self.MAX = mclient
        threading.Thread(target = self.connection_requirement).start()
        print("Server is Up and running on " + str(self.HOST) + " and port " + str(self.PORT) + " with max Client of " + self.MAX)

    def connection_requirement(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT)) #socket.gethostbyname(socket.gethostname()) for self.IP
        self.socket.listen(int(self.MAX))
        self.connectionlist = []
        threading.Thread(target = self.recvConnection_server).start()

    def recvConnection_server(self):
        while True:
            self.CON, self.CIP = self.socket.accept()
            username = self.CON.recv(1024)
            self.usernameList.append(username)
            print(self.usernameList)
            self.connectionlist.append((self.CON, self.CIP))
            threading.Thread(target = self.recvMsg_server).start()

    def recvMsg_server(self):
        while True:
            self.msg = self.CON.recv(4096)
            #decode message received from client
            self.msg = self.msg.decode("utf-8")
            #encode message received into string format
            self.msg = self.msg.encode("utf-8")
            for i in (self.connectionlist):
                print(i)
                i[0].send(self.msg)