import tkinter as tk

class VsGame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # Set class attributes
        self.root = root
        self.time_left = 120


        self.pack()
        self.create_buttons()
        self.turn_timer()

    def create_buttons(self):
        self.title = tk.Label(self.root, text="Welcome to the game!")
        self.title.pack()
        self.time_button = tk.Button(self.root, text="Action", width=25, command=self.root.destroy)
        self.timer = tk.Label(self.root)
        self.timer.pack()
        self.time_button.pack()

    def turn_timer(self):
        def count():
            self.time_left -= 1
            self.timer.config(text=str(self.time_left))
            self.timer.after(1000, count)
        count()


def SetStartingFiles():
    # Set starting files for game. Copy all files from StartFiles into InUseFiles
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

    #print("Hello world!")

main()
