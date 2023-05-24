import socket
import threading
import signal
import sys

class Server:
    def __init__(self, num_computers):
        self.num_computers = num_computers
        self.computers = [False] * num_computers
        self.server_socket = None
        self.server_address = ('192.168.15.10', 5000)

    def start(self):
        print("Starting server...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(5)
        print("Server started.")
        print("Waiting for connections...\n")

        # Lidar com o sinal de interrupção Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown)

        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection: {client_address}")
                thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                thread.start()
            except socket.error:
                break

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                if data == 'get_computers':
                    client_socket.send(str(self.computers).encode('utf-8'))
                elif data.startswith('request_access'):
                    index = int(data.split(':')[1])
                    if not self.computers[index]:
                        self.computers[index] = True
                        client_socket.send("Access granted.".encode('utf-8'))
                    else:
                        client_socket.send("Access denied. Computer is already in use.".encode('utf-8'))
                elif data.startswith('release_access'):
                    index = int(data.split(':')[1])
                    if self.computers[index]:
                        self.computers[index] = False
                        client_socket.send("Access released.".encode('utf-8'))
                    else:
                        client_socket.send("Computer is not in use.".encode('utf-8'))
                else:
                    client_socket.send("Invalid command.".encode('utf-8'))
            except socket.error:
                break

        client_socket.close()

    def shutdown(self, signum, frame):
        print("\nShutting down the server...")
        self.server_socket.close()
        sys.exit(0)
