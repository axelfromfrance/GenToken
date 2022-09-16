import random
import pystyle
from pystyle import Colors, Colorate

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(100):
    first = ''.join((random.choice(chars) for i in range(24)))
    second = ''.join((random.choice(chars) for i in range(6)))
    third = ''.join((random.choice(chars) for i in range(27)))


    result = first + "." + second + "." + third

    token = open("token.txt", "a")
    token.write(result + "\n")
