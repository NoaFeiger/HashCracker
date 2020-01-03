import hashlib
import struct


def inputUser():
    _hash = input("Please enter the hash: ")
    len = input("Please enter the input string length: ")
    if len(_hash) != 40:
        while len(_hash) != 40:
            _hash = input("Please enter the hash: ")

    return _hash, len
#search servers with DISCOVER

str = 'viper'
print(hashlib.sha1(str.encode()).hexdigest())
