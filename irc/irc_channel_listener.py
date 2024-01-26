# Simple check for irc channel activity
# Full raw data on wire

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'irc.libera.chat' #irc server
PORT = 6667 #port
NICK = 'YourNick'

s.connect((HOST, PORT))

nick_data = ('NICK ' + NICK + '\r\n')
s.send(nick_data.encode())

usernam_data= ('USER YourNick1 YourNick2 YourNick3 :YourNick4 \r\n')
s.send(usernam_data.encode())

s.send('JOIN #programming \r\n'.encode()) #channel

while True:
    result = s.recv(1024).decode('utf-8')
    print(result)

    if result[0:4] == "PING":
        s.send(("PONG" + result[4:] + "\r\n").encode())

    if len(result) == 0:
        break   
