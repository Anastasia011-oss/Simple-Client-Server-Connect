import socket
import logging

HOST = '127.0.0.1'
PORT = 4000

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server start")
logging.info("Server started")

conn, addr = server.accept()
print("Client connected by", addr)
logging.info(f"Client connected: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        logging.info("Client disconnected")
        break

    msg = data.decode()
    print("Client msg:", msg)
    logging.info(f"Received expression: {msg}")

    try:
        result = str(eval(msg))
        logging.info(f"Result: {result}")
    except Exception as e:
        result = "Error in expression"
        logging.error(f"Error while evaluating '{msg}': {e}")

    conn.send(result.encode())

conn.close()
server.close()
logging.info("Server stopped")
print("Server closed")
