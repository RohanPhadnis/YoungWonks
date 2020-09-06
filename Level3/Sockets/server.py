import socket
host=''
port=1000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print('binded')
s.listen()
print('listening...')
conn,addr=s.accept()
print("Got connection from",addr)
while True:
    conn.send(input('say something: ').encode())
    data=conn.recv(1024).decode('utf-8')
    print(data)
conn.close()
