import socket

HOST = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Client connected")

while True:
    msg = input("Enter math expression (or 'exit' to quit): ")

    if msg == "exit":
        break

    client.send(msg.encode())

    data = client.recv(1024)
    result = data.decode()
    print("Result from server:", result)

client.close()
print("Client closed")
