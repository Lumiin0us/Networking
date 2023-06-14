import socket
import threading

class Server:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 8000
        self.FORMAT = "utf-8"
        self.ADDR = (self.IP, self.PORT)
        self.DISCONNECT = "DISCONNECT"
        self.LENGTH = 64
    
    def handle_client(self, conn, addr):
        print(f"\n[CONNECTED TO] {addr}")
        while True: 
            message_length = conn.recv(self.LENGTH).decode(self.FORMAT)
            if message_length:
                message_length = int(message_length)
                message = conn.recv(message_length).decode(self.FORMAT)
                if message == self.DISCONNECT:
                    print("[DISCONNECTING]")
                    break
                print(message)
        conn.close()

    def start_server(self):
        print("[SERVER IS STARTING...]")
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server_socket.bind(self.ADDR)
        server_socket.listen()
        print(f"[SERVER IS LISTENING AT {self.ADDR}]...")
        
        while True: 
            conn, addr = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()
            print(f"[ACTIVE THREAD COUNT: {threading.active_count()- 1}]")

server = Server()
try: 
    server.start_server()
except KeyboardInterrupt as e: 
    print("\n[TERMINATING SERVER...]")
