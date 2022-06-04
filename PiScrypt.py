import os
import sys
import threading
import keyboard
import pystray
import PIL.Image
from win32gui import GetWindowText, GetForegroundWindow
import webbrowser


# While World of warcraft (Wow.exe?) is the active window,
# listen to keyboard:
#    if ctrl and alt are pressed (i.e. MB4), then block the use of tab
#    else, unblock the use of tab



def main() -> None:
    #this event is used to stop the loop.
    global exit_event
    exit_event = threading.Event()

    #Create and run the system tray icon
    icon = pystray.Icon("PiScrypt", image, menu=pystray.Menu(
        pystray.MenuItem("I Can't Believe You've Done This", systray_on_click),
        pystray.MenuItem("Exit", systray_on_click)
    ))
    icon.title = "Pi's WoW Script"
    icon.run(setup=setup)


def resource_path(relative_path) -> None:
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def systray_on_click(icon, item) -> None:
    match str(item):
        case "I Can't Believe You've Done This":
            webbrowser.open_new(url)
        case "Exit":
            icon.visible = False
            exit_event.set()
            icon.stop()


def setup(icon) -> None:
    icon.visible = True
    while not exit_event.is_set():
        while GetWindowText(GetForegroundWindow()) == "World of Warcraft":
             if keyboard.is_pressed('left ctrl') and keyboard.is_pressed('left alt'):
                keyboard.block_key('tab')
             else:
                 keyboard.unhook_all()


image_path = resource_path("pi.jpg")
image = PIL.Image.open(image_path)
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if __name__ == '__main__':
    main()
