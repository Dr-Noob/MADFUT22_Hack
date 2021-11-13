#!/bin/bash

function scrap_ids() {
  UA=""
  next_page=1
  p=1

  while [ $next_page -eq 1 ]
  do
    wget --user-agent="$UA" "https://www.fifplay.com/fifa-22/players/?position=&quality=&type=&squad=&status=&nation=&league=&club=&sort=&foot=&minrating=$2&maxrating=$1&search=&page=$p" -O fifplay.html
    grep '<div><a href="https://www.fifplay.com/fifa-22/players/' fifplay.html | cut -d'/' -f6 >> ids.txt

    let "p=p+1"
    if ! grep -q "page=$p" fifplay.html
    then
      next_page=0
    fi

    sleep 3
  done
}

rm -f ids.txt

maxR=99
minR=70

scrap_ids $maxR $minR

minR=64
maxR=64

scrap_ids $maxR $minR
