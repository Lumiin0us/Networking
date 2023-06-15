import socket 

class Client:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 8000 
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = 'utf-8'
        self.LENGTH = 64
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    
    def connect_with_server(self):
        self.client_socket.connect(self.ADDR)
    
    def send_message(self, message):
        message = message.encode(self.FORMAT)
        message_length = len(message)
        message_length = str(message_length).encode(self.FORMAT)
        message_length += b' ' * (self.LENGTH - len(message_length))
        self.client_socket.send(message_length)
        self.client_socket.send(message)

    def close_connection(self):
        self.client_socket.close()

client = Client()
client.connect_with_server()
client.send_message("is maria")
client.send_message("alive and well?")
client.send_message("DISCONNECT")
client.close_connection()