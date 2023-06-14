import socket
import threading

class Server:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 8000
        self.FORMAT = "utf-8"
        self.ADDR = (self.IP, self.PORT)
    
    def handle_client(self, conn, addr):
        while True: 
            message = conn.recv(1024)
            if message:
                print(f"\n[CONNECTED TO] {addr}")
                message = message.decode(self.FORMAT).split()
                if message == "DISCONNECT":
                    conn.close()
                    break
                print(message)

    def start_server(self):
        print("[SERVER IS STARTING...]")
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server_socket.bind(self.ADDR)
        server_socket.listen()
        print(f"[SERVER IS LISTENING AT {self.ADDR}]...")
        conn, addr = server_socket.accept()
        threading.Thread(target=self.handle_client, args=(conn, addr)).start()

        print(f"[ACTIVE THREAD COUNT:{threading.active_count()- 1}]")

server = Server()
server.start_server()