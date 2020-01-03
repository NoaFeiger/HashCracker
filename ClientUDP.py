import struct
from socket import *


def inputUser():
    # _hash = input("Please enter the hash: ")
    _hash = 'a346f3083515cbc8ca18aae24f331dee2d23454b'
    # length = input("Please enter the input string length: ")
    length_user = 2
    if len(_hash) != 40:
        while len(_hash) != 40:
            _hash = input("hash len must be 40! Please enter again: ")
    return _hash, length


address_array = []
name = 'A'*32
_hash = 'B'*32
start = 256*'C'
end = 256*'B'
type_discover = '\x01'
type_offer = '\x02'
length = '\x01'
type_request = '\x03'
type_ack = '\x04'
type_nack = '\x05'


def build_msg(name1, type1, _hash1, length1, start1, end1):
    print(name1, type1, _hash1, length1, start1, end1)
    msg = name1 + type1 + _hash1 + length1 + start1 + end1
    return msg.encode()


if __name__ == "__main__":
    serverName = ''
    serverPort = 3117
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    _hash, length = inputUser()
    message_DISCOVER = build_msg(name, type_discover, _hash, length, start, end)
    clientSocket.sendto(message_DISCOVER, (serverName, serverPort))
    while 1:  # 1 sec
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        if modifiedMessage.decode()[32] == '\x02':
            print("got offer->add to array address->send requst")
            address_array.append(serverAddress)
            print("array len is "+str(len(address_array)))
            build_msg(name, type_request, _hash, length, start, end)
    # send req for all addresses
    # wait to the first ack / all nack

    clientSocket.close()
