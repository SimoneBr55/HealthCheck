from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import sys
import fnmatch
import keyring

if sys.argv[0] == "-h":
    print("Welcome to 'database_encryption.py'.")
    print("This script will keep an eye on a 'folder' and will encrypt the NextCloud password database backup as it is added.")
    print("...")

folder_to_track = "/mnt/storage/nextcloud/data/simone/files/Backups"
folder_tree = "/mnt/storage/nextcloud/data/simone/files/Backups/NCPasswords"

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            if fnmatch.fnmatch(filename,'*Passwords*'):
