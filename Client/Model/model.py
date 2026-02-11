import socket
import logging
import time

HOST = '127.0.0.1'
PORT = 4000


class ClientModel:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_with_ping(self, log_callback):
        while True:
            try:
                self.client.connect((HOST, PORT))
                logging.info("Connected to server")
                log_callback("Connected to server")
                break
            except:
                log_callback("Ping server...")
                time.sleep(1)

    def receive(self):
        data = self.client.recv(1024)
        return data.decode() if data else None

    def send(self, msg):
        self.client.send(msg.encode())
        logging.info(f"Sent: {msg}")

    def close(self):
        self.client.close()
        logging.info("Client stopped")
