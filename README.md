# HealthCheck
 Set of scripts to keep my PC healthy and clean.

1. _detection_sorting.py_ # Tool written in Python3 (taken from ... somewhere... and developed) to track changes inside some folder and reorder new files according to file extensions. (*order*)
  DEPENDENCIES: watchdog

2. _log_events.sh_ # Script to track important edit and commands run in my machine. (*security*)

3. _encrypt.sh_ # Script to encrypt important documents via AES256 symmetric encryption (*security*)

4. _decrypt.sh_ # Script to decrypt previously encrypted documents (using script no.3) (*security*)

5. _database_encryption_ # Script that automatically detects database file being added, decrypts it (using previous scripts) and deletes it (*security*)
