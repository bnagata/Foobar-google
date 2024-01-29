from base64 import b64decode
from itertools import cycle

encrypted = b''

file = open('key.txt','r')
key = bytes(file.read(), "utf8")
file.close()

message = []

message = bytes(a ^ b for a,b in zip(b64decode(encrypted), cycle(key)))
print(message)