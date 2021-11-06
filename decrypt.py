#! /usr/bin/env python3

import sys
import re
import base64

def xor(a, b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = a[i%len(a)] ^ b[i%len(b)]
        xored.append(chr(xored_value))
    return ''.join(xored)

input="KgU/Ixc/BxQ7EAE5NQ0kKA=="
key = bytearray([0x46, 0x64, 0x4b])

print(xor(base64.b64decode(input), key))
