from VsGUI import *
import random
import string
import subprocess

def CreateKeywords():
    # Set keyword in private file to enable bonus damage
    key_file = open("PrivateFiles/keywords.txt", "w")
    # From string of 12 random lowercase characters
    keyword = ''.join(random.choice(string.ascii_lowercase) for z in range(12))
    key_file.write(keyword)
    key_file.close()

def SetStartingFiles():
    # Set starting files for game. Copy all files from StartFiles into InUseFiles
    CreateKeywords()
    # Set permissions of log file to ensure it is writable
    subprocess.call(["chmod", "644", "PublicFiles/LogFile.txt"])
    # Open and close log file in write mode to clear it
    log_file = open("PublicFiles/LogFile.txt", "w")
    log_file.close()
    return

def Connect():
    # Connect 2 instances of game and return connection object
    return

def TakeTurn():
    # Take action. Waits for user input
    return

def WaitTurn():
    # Wait for opponent to act. Listens for signal
    return

def PlayGame():
    # Main flow of game.
    return

def main():
    # Sets up game and connects players
    SetStartingFiles()
    Connect()
    PlayGame()
    root = tk.Tk()
    gui = VsGame(root)
    gui.mainloop()

main()
