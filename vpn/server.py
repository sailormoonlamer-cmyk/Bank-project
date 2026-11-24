

import socket
from crypto import decrypt, encrypt

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Ожидание подключения...")

conn, addr = server.accept()

print("Подключился:", addr)

while True:
    data = conn.recv(4096)

    if not data:
        break

    message = decrypt(data)

    print("Получено:", message.decode())

    conn.send(encrypt(b"OK"))

conn.close()
