import socket
import sys

# Refer to README.md for the problem instructions

host = "127.0.0.1"
port = 5000
srv_port = 1337


def contact_clients():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))
    
    s.send(str(srv_port).encode())

    s.close()

def serve_clients():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, srv_port))

    s.settimeout(5.0)

    s.listen(5)

    contact_clients()

    file_count = 0

    c, addr = s.accept()
    while True:

        data = c.recv(2048)

        if not data:
            break

        file = data.decode('utf-8')


        file_content = file.split('\n')

        with open(file_content[0], "w") as f:
            for line in file_content[1:]:
                print(line)
                f.write(line)

    s.close()
