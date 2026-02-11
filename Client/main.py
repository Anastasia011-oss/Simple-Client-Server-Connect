import tkinter as tk
import logging

from Client.View.view import ClientView
from Client.Controller.controller import ClientController


logging.basicConfig(
    filename="client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    root = tk.Tk()

    controller = ClientController(None)
    view = ClientView(root, controller.send_message)
    controller.view = view

    controller.start()

    root.mainloop()


if __name__ == "__main__":
    main()
