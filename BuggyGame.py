from VsGUI import *
from Utils import *

def SetStartingFiles():
    # Set starting files for game. Copy all files from StartFiles into InUseFiles
    CreateKeyword()
    # Set permissions of log file to ensure it is writable
    change_permissions("664", patch=False)
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
    UserID = GenerateUserID()
    Connect()
    PlayGame()
    root = tk.Tk()
    gui = VsGame(root, UserID)
    gui.mainloop()

main()
