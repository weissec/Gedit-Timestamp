# Gedit-Timestamp
Gedit (GNOME Text Editor) plugin for quick parsing of timestamps.

How to install:
--------------------------

1.  Copy both files in:

    ~/.local/share/gedit/plugins/

    Note: If the folder doesn't exist create it.

2.  After copying the files open Gedit and go to Preferences.
    In the Plugins management tab activate Timestamp.

3.  Press F5 (Fn + F5 on laptops) to add the current timestamp to the cursor location.


Custom Settings:
--------------------------

Note: GUI settings for the plugin are not yet implemented and currently under development.

Manual Settings:
--------------------------

Date/Time format: 
- Open the "timepstamp.py" file and edit line 53.

    current format: %H:%M %d/%m/%Y  (10:54 04/12/2018)
    
Keyboard Key:
- Open the "timestamp.py" file and edit line 25.

    current key: F5

Why?
--------------------------
Let's start by saying that Gedit is not a recommended editor for writing manual logs.
However it comes as standard in various distros and is customisable, simple to use and clean.
Adding timestamps can be a necessity when writing log files and having the option to add date and time quickly and with a single key press ease and speed up the process.
