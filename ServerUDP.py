import struct
from socket import *
import hashlib
import hackathon_range_strings
import threading

TYPE_REQUEST = '\x03'

TYPE_DISCOVER = '\x01'
threads = []
BUFSIZE = 2048
name = 'A' * 32
start = 256 * 'C'
end = 256 * 'B'
type_discover = TYPE_DISCOVER
type_offer = '\x02'
type_request = TYPE_REQUEST
type_ack = '\x04'
type_nack = '\x05'


def get_type():
    return message[32]


def getFrom(message):
    length = message[73]
    return message[74:74 + ord(length)]


def gethash(message):
    return message[33:73]  # not include 73, example:'a346f3083515cbc8ca18aae24f331dee2d23454b' viper


def getEndRange(message):
    length = message[73]
    return message[330:330 + ord(length)]


def get_length(message):
    return message[73]


# get message.decode()
def search_string(message):
    hash = gethash(message)
    start_word = getFrom(message)
    end_word = getEndRange(message)
    test = hackathon_range_strings.Ranger(start_word, end_word)
    for string in test.generate_all_from_to_of_len():
        print(string)
        result = hashlib.sha1(string.encode()).hexdigest()
        if result == hash:
            return string
    return ""


def build_msg(name, type, _hash, length, start, end):
    msg = name + type + _hash + length + start + end
    return msg.encode()


def thread_find_input():
    ans = search_string(message)
    if ans == "":
        modifiedMessage = build_msg(name, type_nack, _hash, length, start, end)
    else:
        modifiedMessage = build_msg(name, type_ack, _hash, length, ans + 'A' * (256 - ord(length)), end)
    serverSocket.sendto(modifiedMessage, clientAddress)


if __name__ == "__main__":
    serverPort = 3117
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print("The server is ready to receive")
    while 1:
        message, clientAddress = serverSocket.recvfrom(BUFSIZE)
        message = message.decode()
        _hash = gethash(message)
        length = get_length(message)
        if message[32] == TYPE_DISCOVER:
            print("got discover")
            modifiedMessage = build_msg(name, type_offer, _hash, length, start, end)
            serverSocket.sendto(modifiedMessage, clientAddress)
        elif message[32] == TYPE_REQUEST:
            print("got request")
            t = threading.Thread(target = thread_find_input)
            threads.append(t)
            t.start()

    # todo kill server when send ack or nack
