# Q3 Simulate a client-server communication model using CCS (Calculus of Communicating
# Systems).

## client.py
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    message = "Hello, Server!"
    print(f"Client sends: {message}")
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Client received: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
