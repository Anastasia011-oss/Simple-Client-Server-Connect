import socket
import threading
import tkinter as tk
import time
import logging

HOST = '127.0.0.1'
PORT = 4000

logging.basicConfig(
    filename="client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect_with_ping():
    while True:
        try:
            client.connect((HOST, PORT))
            log.insert(tk.END, "Connected to server\n")
            logging.info("Connected to server")
            break
        except:
            log.insert(tk.END, "Ping server...\n")
            time.sleep(1)


def receive_messages():
    while True:
        data = client.recv(1024)
        if not data:
            break

        msg = data.decode()
        log.insert(tk.END, "Server: " + msg + "\n")
        logging.info(f"Received: {msg}")

        if msg.lower() == "пока!" or msg.lower() == "exit":
            break


def send_message():
    msg = entry.get()
    entry.delete(0, tk.END)

    client.send(msg.encode())
    log.insert(tk.END, "Client: " + msg + "\n")
    logging.info(f"Sent: {msg}")


root = tk.Tk()
root.title("Client Chat")

log = tk.Text(root, width=50, height=20)
log.pack()

entry = tk.Entry(root, width=40)
entry.pack()

btn = tk.Button(root, text="Send", command=send_message)
btn.pack()

threading.Thread(target=connect_with_ping).start()
threading.Thread(target=receive_messages).start()

root.mainloop()

client.close()
logging.info("Client stopped")
print("Client closed")
