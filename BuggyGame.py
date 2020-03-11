import tkinter as tk

class VsGame(tk.Frame):
    def __init__(self, root=None):
        # Keep: don't know reason why
        super().__init__(root)
        # Set reference to root
        self.root = root
        # Name window
        self.master.title("Vul Game")
        # Restrict size of window
        self.root.resizable(0,0)

        # Set starting values
        self.time_left = 120
        self.health = 20
        self.enemy_health = 20
        self.energy = 10
        self.turn = 0

        # Create labels and buttons
        self.pack(fill=tk.BOTH, expand=True)
        self.set_layout()
        self.log_action("Game is ready!")
        #self.turn_timer()

    def set_layout(self):
        # Layout columns and rows for GUI
        self.columnconfigure(1, minsize=175)
        self.columnconfigure(2, minsize=175)
        self.columnconfigure(3)
        self.rowconfigure(1, )
        self.rowconfigure(2)
        self.rowconfigure(3)
        self.rowconfigure(4)

        # Create turn label
        self.turn_label = tk.Label(self, anchor="nw", text="Turn 1",
                               height=2, font="arial 24 bold")
        self.turn_label.grid(row=1, column=1, sticky="w")

        # Create health label
        self.health_label = tk.Label(self, text="My Health: " + str(self.health),
                                      bg="#00e600", font="arial 14")
        self.health_label.grid(row=2, column=1, sticky="ew")

        # Create enemy health label
        self.enemy_health_label = tk.Label(self, text="Enemy Health: " + str(self.enemy_health),
                                            bg="red", font="arial 14")
        self.enemy_health_label.grid(row=2, column=2, sticky="ew")

        # Create energy label
        self.energy_label = tk.Label(self, text="Energy: " + str(self.energy),
                                    bg="#33ccff", font="arial 14")
        self.energy_label.grid(row=3, column=1, sticky="ew")

        # Create attack button
        self.attack_button = tk.Button(self, text="Attack", font="arial 14",
                                        command= lambda: self.update_enemy_health(1))
        self.attack_button.grid(row=4, column=1, sticky="ew", columnspan=1)

        # Create improve button
        self.improve_button = tk.Button(self, text="Improve", font="arial 14",
                                         command= lambda: self.update_energy(1))
        self.improve_button.grid(row=4, column=2, sticky="ew")

        # Create log window
        self.log = tk.Text(self, height=10, wrap="word",
                            yscrollcommand="set", state="disabled")
        self.log.grid(row=1, column=3, columnspan=1, rowspan=4, sticky="ns")

    def log_action(self, message):
        # Have to set log state to normal to modify
        self.log.config(state="normal")
        # Show message without header if game is starting
        if self.turn == 0:
            self.log.insert(tk.END, message)
        # Format to show game output each turn
        else:
            self.log.insert(tk.END, "\nTurn " + str(self.turn) + ": " + message)
        # Disable ability to edit window
        self.log.config(state="disabled")
        # Autoscroll to bottom
        self.log.yview(tk.END)
        # TODO Move turn counter to action wrapper
        self.turn += 1
        self.update_turn()

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
        self.log_action("Enemy dealt 1 damage to player!")

    def update_enemy_health(self, damage):
        self.enemy_health -= damage
        self.enemy_health_label.config(text="Enemy Health: " + str(self.enemy_health))
        self.log_action("Player dealt 1 damage to enemy!")

    def update_energy(self, energy):
        self.energy -= energy
        self.energy_label.config(text="Energy: " + str(self.energy))
        self.log_action("Player spent energy to improve code!")
        # Disable improve button if out of energy
        if self.energy == 0:
            self.improve_button.config(state="disabled")

    def update_turn(self):
        self.turn_label.config(text="Turn " + str(self.turn))


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
