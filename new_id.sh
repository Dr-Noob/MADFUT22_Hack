#!/bin/bash

adb shell "su -c cat /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml" > /tmp/.activity1.xml
read -n 1 -s -r -p "Press any key when you have obtained the new player"
adb shell "su -c cat /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml" > /tmp/.activity2.xml

./get_ids.sh /tmp/.activity1.xml > /tmp/.decrypted_ids1.txt
./get_ids.sh /tmp/.activity2.xml > /tmp/.decrypted_ids2.txt

echo
echo 'Diff between IDs:'
diff /tmp/.decrypted_ids1.txt /tmp/.decrypted_ids2.txt

rm /tmp/.decrypted_ids1.txt /tmp/.decrypted_ids2.txt /tmp/.activity1.xml /tmp/.activity2.xml

