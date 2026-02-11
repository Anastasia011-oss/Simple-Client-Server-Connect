import tkinter as tk


class ClientView:
    def __init__(self, root, send_callback):
        self.root = root
        self.root.title("Client Chat")

        self.log_widget = tk.Text(root, width=50, height=20)
        self.log_widget.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.btn = tk.Button(root, text="Send", command=send_callback)
        self.btn.pack()

    def log(self, message):
        self.log_widget.insert(tk.END, message + "\n")

    def get_message(self):
        msg = self.entry.get()
        self.entry.delete(0, tk.END)
        return msg
