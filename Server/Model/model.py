import socket
import logging

HOST = '127.0.0.1'
PORT = 4000

auto_answers = {
    "привет": "Привет!",
    "как дела?": "Хорошо, а ты?",
    "что делаешь?": "Общаюсь с клиентом :)",
    "exit": "Пока!",
    "как тебя зовут?": "Я сервер-бот :)",
    "чем занимаешься?": "Отвечаю на твои вопросы!"
}


class ServerModel:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(1)
        self.conn = None

    def accept_client(self):
        self.conn, addr = self.server.accept()
        logging.info(f"Client connected: {addr}")
        return addr

    def receive(self):
        data = self.conn.recv(1024)
        return data.decode() if data else None

    def send(self, msg):
        self.conn.send(msg.encode())

    def close(self):
        if self.conn:
            self.conn.close()
        self.server.close()
