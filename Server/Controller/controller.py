import threading
import logging
from Server.Model.model import ServerModel, auto_answers


class ServerController:
    def __init__(self, view):
        self.model = ServerModel()
        self.view = view

    def start_server(self):
        self.view.log("Server started")
        logging.info("Server started")

        addr = self.model.accept_client()
        self.view.log(f"Client connected: {addr}")

        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        while True:
            msg = self.model.receive()
            if not msg:
                break

            self.view.log("Client: " + msg)
            logging.info(f"Received: {msg}")

            reply = auto_answers.get(msg.lower(), "Не понимаю")
            self.model.send(reply)

            self.view.log("Server: " + reply)
            logging.info(f"Sent: {reply}")

            if msg.lower() == "exit":
                break

        self.model.close()
        logging.info("Server stopped")
