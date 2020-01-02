import hashlib


def inputUser():
    _hash = input("Please enter the hash: ")
    len = input("Please enter the input string length: ")
    if len(_hash) != 40:
        while len(_hash) != 40:
            _hash = input("Please enter the hash: ")


#search servers with DISCOVER




str = "viper"
result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())

