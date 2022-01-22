#! /usr/bin/env python3

import numpy as np
import sys
import re
import base64

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def xor(a, b):
    xored = []
    for i in range(len(a)):
        xored_value = a[i%len(a)] ^ b[i%len(b)]
        xored.append(chr(xored_value))
    return ''.join(xored)

def get_ids_cracked():
    try:
        ids = np.loadtxt('ids/ids.txt', dtype=str)
    except FileNotFoundError:
        eprint('ERROR: File ids.txt does not exist')
        sys.exit(1)

    try:
        ids_totw = np.loadtxt('ids/ids_totw.txt', dtype=str)
    except FileNotFoundError:
        eprint('ERROR: File ids_totw.txt does not exist')
        sys.exit(1)

    # 1: valencia, 2: buffon, 3: motta, 4: vardy86, 5: vardy92, 6: vardy95, 7: batistuta, 8: silva92, 9: silva93, 10: silva95
    # 11-13: robben, 14: alonso, 15-17: modric, 18-20: rivellino
    extra = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    # Strange IDs (they are not fetched from .txt):
    # Wijnaldum OTW
    # Taarabt Winter Wildcard
    # Barella TOTW 87
    # Pereyra Versus ice
    # Everton Versus fire
    # Galeno UEL TOTT
    # Nkunku
    # Simeone
    # Ramsdale
    # Theate
    # Payet
    # Orsolini
    # Alexander-Arnold POTM
    # Laborde POTM
    # Mbappe headliner
    # Salah headliner
    # Rafa TOTW
    # Kokcu TOTW
    # Song Wenjie TOTW Silver
    # Brobbey TOTW Silver
    ids = np.append(ids, [50512939, 67288469, 100887528, 67301925, 100886012, 84125562, 184781787, 100880112, 100897230, 100920574, 67286252, 67342420, 100894577, 134427247, 117672259, 151204275, 84102627, 67352109, 50563906, 67360674])
    # Add TOTW to ids_totw to get FUTCHAMP TOTW too
    ids_totw = np.append(ids_totw, [100887528])

    id_str = '{'
    for id in extra:
        id_str += '"id' + str(id).zfill(3) + '":100,'

    for i, line in np.ndenumerate(ids):
        id_str += '"id' + line + '":100,'

    # In MADFUT22, FUTCHAMP TOTW always end in 00
    for i, line in np.ndenumerate(ids_totw):
        id_str += '"id' + line + '00' + '":100,'

    id_str = id_str[:-1]
    id_str += '}'

    return id_str

def crack_players():
    ids = get_ids_cracked()
    sys.stdout.write('    <string name="LwA4">')
    sys.stdout.write(base64.b64encode(str.encode(xor(str.encode(ids), xor_key))).decode("utf-8"))
    sys.stdout.write('</string>\n')

def crack_coins():
    coins = '100000000'
    sys.stdout.write('    <string name="JQsiKBc=">')
    sys.stdout.write(base64.b64encode(str.encode(xor(str.encode(coins), xor_key))).decode("utf-8"))
    sys.stdout.write('</string>\n')

if(len(sys.argv) != 2):
    eprint("ERROR: Need one arg")
    eprint("Use:",sys.argv[0],"file")
    sys.exit(1)

try:
    input_f = open(sys.argv[1],'r')
except FileNotFoundError:
    eprint("ERROR: File '",sys.argv[1],"' does not exist")
    sys.exit(1)

regex_ids = re.compile(r'\s*<string\s+name="LwA4">.*')
regex_coins = re.compile(r'\s*<string\s+name="JQsiKBc=">.*')
regex_end = re.compile(r'</map>')
found = False

# XOR key is 0x46644b
xor_key = bytearray([0x46, 0x64, 0x4b])

for line in input_f:
    if regex_ids.match(line):
        found = True
        crack_players()
    elif regex_coins.match(line):
        crack_coins()
    elif regex_end.match(line) and not found:
        crack_players()
        sys.stdout.write(line)
    else:
        sys.stdout.write(line)
