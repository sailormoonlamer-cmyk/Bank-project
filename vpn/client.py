

import socket
from crypto import encrypt, decrypt

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket()
client.connect((HOST, PORT))

while True:
    text = input("Введите сообщение: ")

    client.send(encrypt(text.encode()))

    response = decrypt(client.recv(4096))

    print("Ответ сервера:", response.decode())