import threading
import logging
from Client.Model.model import ClientModel


class ClientController:
    def __init__(self, view):
        self.model = ClientModel()
        self.view = view

    def start(self):
        threading.Thread(target=self.model.connect_with_ping, args=(self.view.log,)).start()
        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        while True:
            msg = self.model.receive()
            if not msg:
                break

            self.view.log("Server: " + msg)
            logging.info(f"Received: {msg}")

            if msg.lower() in ["пока!", "exit"]:
                break

        self.model.close()

    def send_message(self):
        msg = self.view.get_message()
        if not msg:
            return

        self.model.send(msg)
        self.view.log("Client: " + msg)
