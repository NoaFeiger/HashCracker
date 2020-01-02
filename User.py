import hashlib


def inputUser():
    h = input("Please enter the hash: ")
    len = input("Please enter the input string length: ")
    print(h)
    print(len)

str = "viper"


result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())

print(str.encode())
