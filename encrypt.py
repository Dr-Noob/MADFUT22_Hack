#! /usr/bin/env python3

import sys
import re
import base64

def xor(a, b):
    xored = []
    for i in range(len(a)):
        xored_value = a[i%len(a)] ^ b[i%len(b)]
        xored.append(chr(xored_value))
    return ''.join(xored)

if(len(sys.argv) != 2):
    print("ERROR: Need one arg")
    print("Use:",sys.argv[0],"file")
    sys.exit(1)

try:
    input_f = open(sys.argv[1],'r')
except FileNotFoundError:
    print ("ERROR: File '",sys.argv[1],"' does not exist")
    sys.exit(1)

regex_item = re.compile(r'\s*<string\s+name="([^"]+)">([^<]+)</string>')

sys.stdout.write("<?xml version='1.0' encoding='utf-8' standalone='yes' ?>\n")
sys.stdout.write("<map>\n")

# XOR key is 0x46644b
xor_key = bytearray([0x46, 0x64, 0x4b])

for line in input_f:
    if regex_item.match(line):
        m = re.search(regex_item, line)
        sys.stdout.write("    <string name=\"")
        sys.stdout.write(base64.b64encode(str.encode(xor(str.encode(m.group(1)), xor_key))).decode("utf-8"))
        sys.stdout.write("\">")
        sys.stdout.write(base64.b64encode(str.encode(xor(str.encode(m.group(2)), xor_key))).decode("utf-8"))
        sys.stdout.write("</string>\n")

sys.stdout.write("</map>\n")
