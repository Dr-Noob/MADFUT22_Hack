#!/bin/bash -u

function scrap_ids() {
  UA=""
  next_page=1
  p=1
  max_retries=3
  r=0

  while [ $next_page -eq 1 ]
  do
    while true; do
      let r=r+1
      wget --user-agent="$UA" "https://www.fifplay.com/fifa-22/players/?position=&quality=&type=$3&squad=&status=&nation=&league=&club=&sort=&foot=&minrating=$2&maxrating=$1&search=&page=$p" -O fifplay.html
      sleep $((1 + $RANDOM % 2))
      [[ $? -ne 0 && $r -le $max_retries ]] || break
    done

    if [[ $r -eq $max_retries ]]; then
      echo 'Too much errors, exiting...'
      exit 1
    fi

    grep '<div><a href="https://www.fifplay.com/fifa-22/players/' fifplay.html | cut -d'/' -f6 >> "$4"

    let r=0
    let "p=p+1"
    if ! grep -q "page=$p" fifplay.html
    then
      next_page=0
    fi
  done
}

rm -f ids.txt ids_totw.txt

out="ids.txt"
type=""
maxR=99
minR=70

scrap_ids "$maxR" "$minR" "$type" "$out"

out="ids.txt"
type=""
minR=64
maxR=64

scrap_ids "$maxR" "$minR" "$type" "$out"

out="ids_totw.txt"
type="totw"
maxR=99
minR=45

scrap_ids "$maxR" "$minR" "$type" "$out"
