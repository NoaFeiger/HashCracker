from socket import *
import helper
import time

TIMEOUT_ACK = 20
TIMEOUT_WAIT_OFFER = 1
OFFER_TYPE = '\x02'


def inputUser():
    _hash = input("Please enter the hash: ")
    # _hash = '7f5bb03cf507c861269be561971108be8f37d832'
    length_user = input("Please enter the input string length: ")
    # length_user = '5'
    if len(_hash) != 40:
        while len(_hash) != 40:
            _hash = input("hash len must be 40! Please enter again: ")
    return _hash, length_user


address_array = []
name = 'A' * 32
start = 256 * 'C'
end = 256 * 'B'
type_discover = '\x01'
type_offer = OFFER_TYPE
type_request = '\x03'
type_ack = '\x04'
type_nack = '\x05'


def build_msg(name1, type1, _hash1, length1, start1, end1):
    msg = name1 + type1 + _hash1 + length1 + start1 + end1
    return msg.encode()


if __name__ == "__main__":
    serverName = '255.255.255.255'
    serverPort = 3117
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    _hash, length = inputUser()
    length_int = int(length)
    length = chr(length_int)
    message_DISCOVER = build_msg(name, type_discover, _hash, length, start, end)
    clientSocket.sendto(message_DISCOVER, (serverName, serverPort))
    clientSocket.settimeout(1)
    timeout = time.time() + TIMEOUT_WAIT_OFFER
    while time.time() < timeout:  # 1 sec
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            if modifiedMessage.decode()[32] == OFFER_TYPE:
                print("got offer")
                address_array.append(serverAddress)
                print("array len is " + str(len(address_array)))
        except OSError as msg:
            print(time.time(), timeout)
    string_division = helper.getRanges(length_int, len(address_array))
    i = 0
    for div in string_division:  # send req for all addresses
        msg = build_msg(name, type_request, _hash, length, div[0] + 'A' * (256 - length_int),
                        div[1] + 'A' * (256 - length_int))
        clientSocket.sendto(msg, address_array[i])
        i = i + 1
    count_ack = 0
    ans = ""
    clientSocket.settimeout(TIMEOUT_ACK)
    while count_ack < len(address_array):  # wait to the first ack / all nack
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessage = modifiedMessage.decode()
        if modifiedMessage[32] == '\x04':  # type ack
            ans = modifiedMessage[74:74 + length_int]
            break
        count_ack = count_ack + 1
    if ans == "":
        print("fail with finding the input string")
    else:
        print("The input string is " + ans)
    clientSocket.close()
