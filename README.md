The goal is to use MouseButton4 as a new modifier in World of Warcraft in order to have access to another pool of keybinds, but also have MB4 remain as a useful browser 'back' button when alt-tabbed.

The idea is to replace MB4 keypress with CTRL+ALT, so WoW thinks you're holding down both CTRL and ALT (which are modifier keys) instead of MB4.

There are plenty of ways to do this (like AutoHotKey), but I've found this free tool to be easy and useful:
https://www.highrez.co.uk/downloads/xmousebuttoncontrol.htm

Using the above program, I have created a profile which, when playing World of Warcraft, sends CTRL and ALT keypresses when the MouseButton4 button is pressed (and releases CTRL and ALT when MB4 is released). It also blocks the original sending of MB4 so that the game/other programs don't register MB4+CTRL+ALT.

Cool, huh? Except this presents a problem. What happens when you're holding down MB4 (sending CTRL + ALT), and then press Tab?
Well, it registers as an Alt+Tab, which tabs you out of the game. Additionally, because the script stops running when WoW.exe is not the active window, the keys CTRL and ALT remain in a 'pressed' state which can result in all sorts of funky shit happening.

In order to remedy this issue without disabling alt+tab completely, I created a python script which will prevent 'alt tabbing' when the MouseButton4 (CTRL+ALT) key is pressed.

This exe runs a script encapsulated within a system tray icon. Use this in conjunction with XMouseButtonControl for coolness.
