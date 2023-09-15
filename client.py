import socket
import sys
import select 
print("pm")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 1093
c.connect((HOST, PORT))

name = "usr1"

msgencoded = ""
inputstream = []
i = True
while i == True:
    sockets_list = [sys.stdin, c]


    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == c:
            data = c.recv(2042)
            print(data.decode('utf-8'))
           
        else:

            msgpend = input("say what? ")
            if msgpend == "name":
                name = input("what would you like to nickname yourself: ")
            if msgpend == "quit":
                print("goodbye")
                i = False
                break
            msgsend = name + ": " + msgpend
            msgencoded = msgsend.encode('utf-8')
            inputstream.append(msgencoded)
            c.send(msgencoded)
    
c.close()