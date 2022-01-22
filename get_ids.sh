#!/bin/bash -u

if [ $# -ne 1 ]
then
  echo "Usage: $0 MainActivity.xml"
  exit 1
fi

./decrypt.py $1 > /tmp/.decrypted.xml
grep '<string name="ids">' /tmp/.decrypted.xml | tr ',' '\n' | tr '{' '\n' | tail -n +2 | cut -d ':' -f1 | tr -d '"' | tr -d 'i' | tr -d 'd' | sort -n
rm /tmp/.decrypted.xml
