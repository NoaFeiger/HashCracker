import struct
from socket import *
import hashlib
import hackathon_range_strings
import threading

threads = []

BUFSIZE = 2048

serverPort = 3117
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

name = 'A' * 32
_hash = 'B' * 32
start = 256 * 'C'
end = 256 * 'B'
type_discover = '\x01'
type_offer = '\x02'
length = '\x01'
type_request = '\x03'
type_ack = '\x04'
type_nack = '\x05'


def build_msg(name, type, _hash, length, start, end):
    msg = name + type + _hash + length + start + end
    return msg.encode()


while 1:
    message, clientAddress = serverSocket.recvfrom(BUFSIZE)
    message = message.decode()
    if message[32] == '\x01':
        modifiedMessage = build_msg(name, type_offer, _hash, length, start, end)
    else:
        print("fail- not discover message")
        modifiedMessage = struct.pack('c', b'\x02')
    serverSocket.sendto(modifiedMessage, clientAddress)

"""
def get_type():
    return message[32]


def getFrom(message):
    len=message[73]
    return message[74:74+len]


def gethash(message):
    return message[33:73]  #not include 73, example:'a346f3083515cbc8ca18aae24f331dee2d23454b' viper


def getEndRange(message):
    len=message[73]
    return message[]


def search_string(message):
    hash = gethash(message)
    start_word = getFrom(message)
    end_word = getEndRange(message)
    test = hackathon_range_strings.Ranger(start_word, end_word)
    for string in test.generate_all_from_to_of_len():
        result = hashlib.sha1(str.encode())
        if result == hash:
            return string
    return ''  #not found- need to send nack


"""
