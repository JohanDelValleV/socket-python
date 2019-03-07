import socket

HOST = '192.168.137.202'    # The remote host
PORT = 3000              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print('mensaje:')
        msg=input()
        if msg !='':
            s.sendall(msg.encode())
            data = s.recv(1024)
            print('Received', repr(data.decode('ascii')))