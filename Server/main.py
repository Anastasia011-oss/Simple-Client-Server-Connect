import socket
import threading
import tkinter as tk
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

conn = None

auto_answers = {
    "привет": "Привет!",
    "как дела?": "Хорошо, а ты?",
    "что делаешь?": "Общаюсь с клиентом :)",
    "exit": "Пока!",
    "как тебя зовут?": "Я сервер-бот :)",
    "чем занимаешься?": "Отвечаю на твои вопросы!"
}

def start_server():
    global conn
    log.insert(tk.END, "Server started\n")
    logging.info("Server started")

    conn, addr = server.accept()
    log.insert(tk.END, f"Client connected: {addr}\n")
    logging.info(f"Client connected: {addr}")

    threading.Thread(target=receive_messages).start()


def receive_messages():
    global conn
    while True:
        data = conn.recv(1024)
        if not data:
            break

        msg = data.decode()
        log.insert(tk.END, "Client: " + msg + "\n")
        logging.info(f"Received: {msg}")

        reply = auto_answers.get(msg.lower(), "Не понимаю")
        conn.send(reply.encode())
        log.insert(tk.END, "Server: " + reply + "\n")
        logging.info(f"Sent: {reply}")

        if msg.lower() == "exit":
            break


root = tk.Tk()
root.title("Server Chat")

log = tk.Text(root, width=50, height=20)
log.pack()

threading.Thread(target=start_server).start()

root.mainloop()

if conn:
    conn.close()
server.close()
logging.info("Server stopped")
print("Server closed")
