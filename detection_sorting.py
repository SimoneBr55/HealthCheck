from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import sys

if sys.argv[0] == "-h":
    print("Welcome to detection_sorting.py")
    print("This script wacthes a given directory and categorizes files.")
    print("USAGE:")
    print(" 'detection_sorting.py -h' ")
    print("Shows these help messages.")
    print()
    print(" 'detection_sorting.py folder_to_track folder_root' ")
    print("""Be aware that this script requires folder_root to be a root directory
in which python wants to find proper subdirectories for the filetypes detected.""")
    quit()

folder_destination = ""
folder_to_track = sys.argv[0]
folder_tree = sys.argv[1]


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename == ".DS_Store":
                print("Passo")
                continue
            if filename.lower().endswith(".dmg"):
                #print("dmg")
                folder_destination = folder_tree + "/" + "dmg"
            elif filename.lower().endswith(".pkg"):
                folder_destination = folder_tree + "/" + "pkg"
            #ext = os.path.splitext(filename)[-1].lower()
            #if ext == ".DS_Store":
            #    pass
            #if ext == ".pkg":
            #    folder_destination = folder_tree + "/" + "pkg"
            #elif ext == ".dmg":
            #    folder_destination = folder_tree + "/" + "dmg"
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
