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


name = 'A'*32
_hash = 'B'*32

start = 256*'C'
end = 256*'B'
type = '\x01'
length = '\x01'
print(start.encode())
msg = name+type+_hash+length+start+end
print(msg)

msg = msg.encode()
print(msg)

#msg = struct.pack('scscss', name.encode(), b'\x01', _hash.encode(), b'\x01', start.encode(), end.encode())
