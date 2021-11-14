# MAD FUT 22 Hack
This project is a proof-of-concept for hacking the MAD FUT 22 game on Android.

## Disclaimer
This software is provided for educational purposes only.

### 1. What does this script do?
- **100% of the collection** (all the cards in the game).
- **Unlimited coins** (a really big number by default).

### 2. Limitations
- Works only for **Android** devices
- The Android device must be **rooted**
- The script must be executed from a Linux host
- Needs `adb` installed in the Linux host

### 3. Usage
1. Connect your rooted device to the Linux computer
2. Make sure you have the app installed and that you have opened it at least once.
3. **Make a backup of your MainActivity.xml file**. The progress of the game is stored in that file, and this script will replace it. If do not want to lose your progress, please make a backup of this file.
4. Open `crack.sh` and set the `auser` variable to the corresponding Android user in your phone. You need to set the user owner of the app. This can be retrieved using `su -c ls -l /data/data/com.madfut.madfut22/shared_prefs`
5. Run `./crack.sh`. If the script has worked, you will see a `Cracked successfully!` message.
