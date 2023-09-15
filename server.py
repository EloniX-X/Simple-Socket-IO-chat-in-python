import socket
from _thread import *
import select
import sys

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1093

users = []
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen()



print("server running with host "+HOST, "and port " + str(PORT))

def usrthread(conn, addr):
    conn.send("hello".encode('utf-8'))

    f = open("log.txt", "r")
    txtlog = f.read()
    conn.send(txtlog.encode('utf-8'))
    f.close()

    while True:
        conmsg = conn.recv(2042)
        broadcast(conmsg, conn)
        if not conmsg:
            break
        else:
            f = open("log.txt", "a")
            f.write(str(conmsg))
            f.write('\n')
            f.close()
        
        


    
def remove(connection):
    if connection in users:
        users.remove(connection)
        print(addr, ' disconnected')




def broadcast(conmsg, conn):
    for clients in users:
        clients.send(conmsg)

        




while True:
    conn, addr = s.accept()
    print("connection established with ",addr)

    users.append(conn)

    start_new_thread(usrthread, (conn, addr))
#print(addr, " has connected")
   #     welcolmmsg = "hello welcolm to this"
 #       conn.send("ze server has connected a seccesfulle".encode())
  #      users.append(conn)

conn.close()
s.close()