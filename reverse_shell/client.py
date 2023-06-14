import socket 

class Client:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 8000 
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = 'utf-8'
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


    def connect_with_server(self):
        self.client_socket.connect(self.ADDR)
    
    def send_message(self, message):
        message = message.encode(self.FORMAT)
        self.client_socket.send(message)

client = Client()
client.connect_with_server()
client.send_message("Hello")