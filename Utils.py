import subprocess
import random
import string
import os

def change_permissions(perm, request_ID=None, host_ID=None, patch=None):
    if not patch:
        # No patch: allow chmod to happen without check
        subprocess.call(["chmod", perm, "PublicFiles/LogFile.txt"])
        return True
    else:
        # Patch: Check request ID
        if request_ID == host_ID:
            # Reject request if ID is not host
            subprocess.call(["chmod", perm, "PublicFiles/LogFile.txt"])
            return True
    return False

def read_file(GUI, target_file):
    # Retrieve lines from target file
    def get_lines():
        # Check if file exists
        try:
            f = open(target_file)
            lines = f.readlines()
            f.close()
            return lines
        # Return error if file not found
        except:
            return ["Error! File not found"]

    # Read any file given. Vulnerable to "../" file path
    if not GUI.spy_patch:
        return get_lines()
    # Patch is applied: cannot request file path with "../"
    else:
        if ".." in target_file:
            return ["File peak failed! Not able to look at files outside of PublicFiles/"]
        else:
            return get_lines()

def CreateKeyword():
    # Set keyword in private file to enable bonus damage
    key_file = open("PrivateFiles/keyword.txt", "w")
    # Form string of 5 random lowercase characters
    keyword = ''.join(random.choice(string.ascii_lowercase) for z in range(5))
    key_file.write(keyword)
    key_file.close()

def GenerateUserID():
    return "".join(random.choice(string.ascii_lowercase) for z in range(10))

def SetStartingFiles():
    # Set starting files for game.
    # Create folders if not present
    if not os.path.exists('PublicFiles/'):
        os.makedirs('PublicFiles/')
    if not os.path.exists('PrivateFiles/'):
        os.makedirs('PrivateFiles/')
    # Set bonus damage keyword
    CreateKeyword()
    # Set permissions of log file to ensure it is writable
    if os.path.exists("PublicFiles/LogFile.txt"):
        change_permissions("664", patch=False)
    # Open and close log file in write mode to clear it
    log_file = open("PublicFiles/LogFile.txt", "w")
    log_file.close()
    return