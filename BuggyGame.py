from VsGUI import *
from Utils import *

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