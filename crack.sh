#!/bin/bash

auser=""

set -e

if [ -z "${auser}" ]
then
  echo "$0: Android user not specified!"
  echo "$0: Please, open the script and set the auser variable to the Android user that owns the app files"
  echo "$0:"' You can check it with: adb shell "su -c ls -l /data/data/com.madfut.madfut22/shared_prefs"'
  exit 1
fi

# 1. Unpack .tar.gz ids
cd ids/ && ./unpack_ids.sh && cd -

# 2. Copy original xml file from the phone
adb shell "su -c cat /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml" > MainActivity.xml

if ! grep -q '<map>' MainActivity.xml
then
  echo "$0: /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml: No such file or directory"
  echo "$0: File was not found on the phone storage. Please, install the app and open it at least once"
  exit 1
fi

# 3. Get cracked xml
./madfut22.py MainActivity.xml > Cracked.xml

# 4. Copy cracked xml to the phone
adb push Cracked.xml /storage/emulated/0/ && adb shell "su -c mv /storage/emulated/0/Cracked.xml /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml" && adb shell "su -c chown $auser:$auser /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml"

echo "$0: Cracked successfully!"
