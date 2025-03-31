# Q3 Simulate a client-server communication model using CCS (Calculus of Communicating
# Systems).

## server.py
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)

    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    message = conn.recv(1024).decode()
    print(f"Server received: {message}")

    response = "Hello, Client!"
    print(f"Server sends: {response}")
    conn.sendall(response.encode())

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    main()
