#! /usr/bin/env python3

import numpy as np
import sys
import re
import base64

def xor(a, b):
    xored = []
    for i in range(len(a)):
        xored_value = a[i%len(a)] ^ b[i%len(b)]
        xored.append(chr(xored_value))
    return ''.join(xored)

def get_ids_cracked():
    try:
        input_f = open('ids.txt','r')
    except FileNotFoundError:
        print ('ERROR: File ids.txt does not exist')
        sys.exit(1)

    id_str = '{'
    for line in input_f:
        id_str += '"id'
        id_str += str(line[:-1])
        id_str += '":0,'

    id_str = id_str[:-1]
    id_str += '}'

    return id_str

def get_ids_cracked_old():
    # 104000 - 270000
    return '{"id50331689":0, "id50476077":0}'
    #ids = set()
    #players = np.arange(10, 100, 1)
    #players = np.array([41, 51])

    id_str = '{'
    for player_id in players:
      id_str += '"id'
      id_str += str(player_id)
      id_str += '":100,'

    id_str = id_str[:-1]
    id_str += '}'

    return id_str

if(len(sys.argv) != 2):
    print("ERROR: Need one arg")
    print("Use:",sys.argv[0],"file")
    sys.exit(1)

try:
    input_f = open(sys.argv[1],'r')
except FileNotFoundError:
    print ("ERROR: File '",sys.argv[1],"' does not exist")
    sys.exit(1)

regex_item = re.compile(r'\s*<string\s+name="LwA4">.*')

# XOR key is 0x46644b
xor_key = bytearray([0x46, 0x64, 0x4b])

for line in input_f:
    if regex_item.match(line):
      #print("Found players")
      ids = get_ids_cracked()
      sys.stdout.write('    <string name="LwA4">')
      sys.stdout.write(base64.b64encode(str.encode(xor(str.encode(ids), xor_key))).decode("utf-8"))
      sys.stdout.write('</string>\n')
    else:
      sys.stdout.write(line)
