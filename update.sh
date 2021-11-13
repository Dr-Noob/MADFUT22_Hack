#!/bin/bash

set -e

./madfut22.py MainActivity.xml > Cracked.xml

adb push Cracked.xml /storage/emulated/0/ && adb shell "su -c mv /storage/emulated/0/Cracked.xml /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml" && adb shell "su -c chown u0_a95:u0_a95 /data/data/com.madfut.madfut22/shared_prefs/MainActivity.xml"
