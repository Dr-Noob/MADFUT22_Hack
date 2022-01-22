# MADFUT 22 Hack
This project is a proof-of-concept for hacking the MADFUT 22 game on Android.

| :warning: DISCLAIMER: This software is provided for educational purposes only :warning: |
| --- |

## What does this script do?
- **100% of the collection** (all the cards in the game).
- **Unlimited coins** (a really big number of coins).
- **Unlimited LTM Points** (a really big number of points).

## Limitations
- Works only for **Android** devices
- The Android device **must be rooted**
- The script must be executed from a Linux host
- Needs `adb` installed in the Linux host

## Usage
1. Connect your rooted device to the Linux computer
2. Make sure you have the app installed and that you have opened it at least once.
3. **Make a backup of your MainActivity.xml file**. The progress of the game is stored in that file, and this script will replace it. If you do not want to lose your progress, please make a backup of this file (you can use the script `backup.sh` for this duty).
4. Open `crack.sh` and set the `auser` variable to the corresponding MADFUT 22 Android user in your phone. This can be retrieved using `adb shell "su -c ls -l /data/data/com.madfut.madfut22/shared_prefs"`. The Android user looks something like: `u0_aXXX`
5. Run `./crack.sh`. If the script worked, you will see a `Cracked successfully!` message.

### Outdated script
The script needs to be updated when new cards are released to be able to get the 100% of the collection, so I will be updating it from from time to time. Please, **DO NOT ask for script updates** in the GitHub issues page.
