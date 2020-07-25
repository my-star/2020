import socket

#bind_ip="0.0.0.0"
host="0.0.0.0"
bind_port=9990

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,bind_port))

server.listen(5)
print "[*] Listening on %s:%d"% (host,bind_port)

while True:
    client,addr=server.accept()

    print "[*] Accept connection from %s:%d"%(addr[0],addr[1])

    request = client.recv(4096)
    print "[*] Received from %s:%s"% (addr[0],request)

    client.send("ACK!")
    client.close()

