import socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_address, self.server_port))
            print("Connected to the server.")
        except ConnectionRefusedError:
            print("Connection refused. The server may not be available.")
            exit(1)

    def request_computers_status(self):
        self.client_socket.send('get_computers'.encode('utf-8'))
        response = self.client_socket.recv(1024).decode('utf-8')
        return eval(response)

    def request_access(self, computer_index):
        self.client_socket.send(f'request_access:{computer_index}'.encode('utf-8'))
        response = self.client_socket.recv(1024).decode('utf-8')
        print(response)

    def release_access(self, computer_index):
        self.client_socket.send(f'release_access:{computer_index}'.encode('utf-8'))
        response = self.client_socket.recv(1024).decode('utf-8')
        print(response)

    def close_connection(self):
        self.client_socket.close()
