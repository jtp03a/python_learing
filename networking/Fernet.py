import socket
import re
import binascii
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

# Refer to README.md for the problem instructions

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server


# Your create_fernet_and_find_sign_key function here

def create_fernet_and_find_sign_key(master_key):

    try: 
        f = Fernet(master_key)
    except ValueError:
        print('Potential Intrusion Event Detected')
        return 'Potential Intrusion Event Detected'
    
    return f, f._signing_key


def dowork():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    data = s.recv(2048)

    result = create_fernet_and_find_sign_key(data)

    if(result == 'Potential Intrusion Event Detected'):
        s.close()
        return

    print(result)

    f, signing_key = result
 
    print(signing_key)

    s.send(signing_key)

    data = s.recv(2048)

    print(data)

    decrypted_msg = f.decrypt(data)

    print(decrypted_msg)

    s.send(decrypted_msg)

    resp = s.recv(2048)

    print(resp.decode('utf-8'))
    
    return resp


def main():
    dowork()


if __name__ == '__main__':
    main()
