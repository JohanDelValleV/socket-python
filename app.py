import socket

HOST = '192.168.43.107'
PORT = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
   data = conn.recv(1024)
   print(data.decode('ascii'))
   if not data: break
   conn.sendall(data)
#conn.close()

