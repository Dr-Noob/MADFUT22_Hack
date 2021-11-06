#! /usr/bin/env python3

import sys
import re
import base64

def encrypt3(a):
    barr = [0x46, 0x64, 0x4b]
    b = bytearray(barr)
    print("a=", type(a))
    print("b=", type(b))
    xored = []
    for i in range(max(len(a), len(b))):
        print("xor ", hex(a[i%len(a)]), " with ", hex(b[i%len(b)]))
        xored_value = a[i%len(a)] ^ b[i%len(b)]
        xored.append(chr(xored_value))

    return ''.join(xored)

input="KgU/Ixc/BxQ7EAE5NQ0kKA=="

my_str_as_bytes = base64.b64decode(input)
print(my_str_as_bytes)

print(encrypt3(my_str_as_bytes))
