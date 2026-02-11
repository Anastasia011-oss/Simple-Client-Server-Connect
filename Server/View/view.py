import tkinter as tk


class ServerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Server Chat")

        self.log_widget = tk.Text(root, width=50, height=20)
        self.log_widget.pack()

    def log(self, message):
        self.log_widget.insert(tk.END, message + "\n")
