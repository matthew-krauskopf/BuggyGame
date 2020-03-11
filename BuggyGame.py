import tkinter as tk
from tkinter.ttk import Frame

class VsGame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # Set class attributes
        self.root = root
        #self.root.geometry("800x100")
        self.time_left = 120
        self.health = 20
        self.enemy_health = 20
        self.energy = 10
        self.turn = 1

        # Create labels and buttons
        self.pack(fill=tk.BOTH, expand=True)
        self.set_layout()
        #self.turn_timer()

    def set_layout(self):

        # Set title frame
        frame1 = Frame(self)
        frame1.pack(fill=tk.X)

        # Create turn label
        self.turn_label = tk.Label(frame1, anchor="nw", text="Turn 1", width=10,
                               height=2, font="arial 24 bold")
        self.turn_label.pack(side=tk.LEFT)

        # Set health frame
        frame2 = Frame(self)
        frame2.pack(fill=tk.X)

        # Create health label
        self.health_label = tk.Label(frame2, text="My Health: " + str(self.health),
                                      bg="#00e600", width=15)
        self.health_label.pack(side=tk.LEFT)

        # Create enemy health label
        self.enemy_health_label = tk.Label(frame2, text="Enemy Health: " + str(self.enemy_health),
                                            width=15, bg="red")
        self.enemy_health_label.pack(side=tk.LEFT, padx=5)

        # Set energy frame
        frame3 = Frame(self)
        frame3.pack(fill=tk.X)

        # Create energy label
        self.energy_label = tk.Label(frame3, text="Energy: " + str(self.energy),
                                    bg="#33ccff", width=15)
        self.energy_label.pack(side=tk.LEFT)

        # Set action frame
        frame4 = Frame(self)
        frame4.pack(fill=tk.X)

        # Create attack button
        self.attack_button = tk.Button(frame4, text="Attack", width=15,
                                        command= lambda: self.update_enemy_health(1))
        self.attack_button.pack(side=tk.LEFT)

        # Create improve button
        self.improve_button = tk.Button(frame4, text="Improve", width=15,
                                         command= lambda: self.update_energy(1))
        self.improve_button.pack(side=tk.LEFT)

        # Create log window
        #self.log = tk.Text(self.root)


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

    def update_my_health(self, damage):
        self.health -= damage
        self.health_label.config(text="My Health: " + str(self.health))

    def update_enemy_health(self, damage):
        self.enemy_health -= damage
        self.enemy_health_label.config(text="Enemy Health: " + str(self.enemy_health))

    def update_energy(self, energy):
        self.energy -= energy
        self.energy_label.config(text="Energy: " + str(self.energy))

        # Disable improve button if out of energy
        if self.energy == 0:
            self.improve_button.config(state="disabled")


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
