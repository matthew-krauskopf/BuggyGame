import tkinter as tk

class VsGame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # Set class attributes
        self.root = root
        self.time_left = 120
        self.health = 20
        self.energy = 10
        self.turn = 1

        # Create labels and buttons
        self.pack()
        self.set_turn_count()
        self.display_health()
        self.display_energy()
        self.display_attack_button()
        self.display_improve_button()
        #self.turn_timer()

    def set_turn_count(self):
        self.title = tk.Label(self.root, anchor="nw", text="Turn 1", pady=1, height=1, font="arial 24 bold")
        self.title.pack()

    def display_health(self):
        self.health_label = tk.Label(self.root, text="Health: " + str(self.health))
        self.health_label.pack()

    def update_health(self, damage):
        self.health -= damage
        self.health_label.config(text="Health: " + str(self.health))

    def display_energy(self):
        self.energy_label = tk.Label(self.root, text="Energy: " + str(self.energy))
        self.energy_label.pack()

    def display_attack_button(self):
        self.attack_button = tk.Button(self.root, text="Attack", command= lambda: self.update_health(1))
        self.attack_button.pack()

    def display_improve_button(self):
        self.improve_button = tk.Button(self.root, text="Improve", command= lambda: self.update_health(-1))
        self.improve_button.pack()

    def set_turn_timer(self):
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
