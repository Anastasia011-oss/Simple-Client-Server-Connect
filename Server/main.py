import tkinter as tk
import threading
import logging

from Server.View.view import ServerView
from Server.Controller.controller import ServerController


logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    root = tk.Tk()

    view = ServerView(root)
    controller = ServerController(view)

    threading.Thread(target=controller.start_server).start()

    root.mainloop()


if __name__ == "__main__":
    main()
