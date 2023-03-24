#!/usr/bin/env python

# Demonstrates concepts of python structs being used to send custom network packets
# translation between host and network byte order
# encryption/decryption
# simple client/server communication

import socket, struct
from cryptography.fernet import Fernet

# Refer to README.md for the problem instructions

dest = ('127.0.0.1', 1337)

cmd_list = {
    'key-request' : 0x800,
    'key-provide' : 0x801,
    'encrypted-message' : 0x802,
    'error' : 0x8FF
}

#
#  You may wish to write helper functions here
# 


#This function should return the server's final message as an actual Python 3 string,
#not as a byte sequence.
def get_message_using_encrypted_request_protocol():
    # setup the TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to destination ip and port
    s.connect((dest[0], dest[1]))

    # construct the payload with a tuple of the command and the message
    message = (cmd_list['key-request'], b'')
    # construct the packet using format specifies, we want a 48 byte payload
    # so the command is 4 bytes and the message string is 44 bytes
    # I means unsigned int and 44s means 44 byte string
    packet = struct.Struct('! I 44s')
    # pack the packet
    packed_msg = packet.pack(*message)

    # send the packet
    s.send(packed_msg)
    # recieve the server response which is a byte object
    resp = s.recv(2048)
    # use the format specifiers again to form a struct out of the response
    response = struct.Struct('I 44s')

    # unpack the response
    unpacked_msg = response.unpack(resp)
    # get the key from the second item in the unpacked tuple
    key = unpacked_msg[1].decode()
    # create a fernet object with the key
    try:
        f = Fernet(key)
    except ValueError:
        print('bad key')
    # encrypt the message to send to the server with the fernet object
    token = f.encrypt(b'I challenge!')
    # create the response packet with the encrypted message, 100byte string this time
    response_msg = (cmd_list['encrypted-message'], token)
    packet2 = struct.Struct('! I 100s')
    packed_msg2 = packet2.pack(*response_msg)
    # send the packet
    s.send(packed_msg2)
    # get the second server response
    resp2 = s.recv(2048)
    # unpack the response
    response2 = struct.Struct('I 100s')
    unpacked_msg2 = response2.unpack(resp2)
    # decrypt the message in the reponse with the fernet object
    d = f.decrypt(unpacked_msg2[1])
    # close the socket
    s.close()
    # return the response message as a python string
    return d.decode()


if __name__ == "__main__":
    message = get_message_using_encrypted_request_protocol()
    print(message)
