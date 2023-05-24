import sys
from server.server import Server
from client.client import Client

def start_server(num_computers):
    server = Server(num_computers)
    server.start()

def start_client(server_address, server_port):
    client = Client(server_address, server_port)
    client.connect()

    # Exemplo de uso do cliente:
    computers = client.request_computers_status()
    print(f"Computers status: {computers}")

    # Solicita acesso ao computador de índice 0
    client.request_access(0)

    # Libera o acesso do computador de índice 0
    client.release_access(0)

def main():
    print("Select mode:")
    print("1. Server")
    print("2. Client")
    choice = input("Enter your choice: ")

    if choice == "1":
        num_computers = int(input("Enter the number of computers: "))
        start_server(num_computers)
    elif choice == "2":
        server_address = input("Enter the server address: ")
        server_port = int(input("Enter the server port: "))
        start_client(server_address, server_port)
    else:
        print("Invalid choice.")
        sys.exit(1)

if __name__ == "__main__":
    main()
