import tkinter as tk
from Attacks import *
from Improvements import *

class VsGame(tk.Frame):
    def __init__(self, root=None, UserID=None):
        # Keep: don't know reason why
        super().__init__(root)
        # Set reference to root
        self.root = root
        # Name window
        self.master.title("Vul Game")
        # Restrict size of window
        self.root.resizable(0,0)
        # Set User ID
        self.ID = UserID
        # Set temp foe ID
        self.FoeID = "adfasdfeaf"
        self.CurID = self.ID
        # Set standard font
        self.font = "arial 14"
        # Set starting values
        self.time_left = 30
        self.health = 20
        self.enemy_health = 20
        # TODO set better value
        self.energy = 100
        self.turn = 1
        # Set energy costs for attacks
        self.attack_energy = 1
        self.spy_energy = 3
        self.change_priv_energy = 5
        self.DoS_energy = 10
        # Set energy costs for improvements
        self.patch_spy_energy = 5
        self.patch_priv_energy = 10
        self.patch_DoS_energy = 20
        self.repair_log_energy = 3
        # Set patching flags to emulate code patches
        self.permission_patch = False
        # Create labels and buttons
        self.pack(fill=tk.BOTH, expand=True)
        self.set_layout()
        self.log_action("Game is ready!", False)
        #self.turn_timer()

    def set_layout(self):
        # Layout columns and rows for GUI
        self.columnconfigure(1, minsize=175)
        self.columnconfigure(2, minsize=175)

        # Create turn label
        self.turn_label = tk.Label(self, anchor="nw", text="Turn 1",
                               height=2, font="arial 24 bold")
        self.turn_label.grid(row=1, column=1, sticky="w")

        # Create health label
        self.health_label = tk.Label(self, text="My Health: " + str(self.health),
                                      bg="#00e600", font=self.font)
        self.health_label.grid(row=2, column=1, sticky="ew")

        # Create enemy health label
        self.enemy_health_label = tk.Label(self, text="Enemy Health: " + str(self.enemy_health),
                                            bg="red", font=self.font)
        self.enemy_health_label.grid(row=2, column=2, sticky="ew")

        # Create energy label
        self.energy_label = tk.Label(self, text="Energy: " + str(self.energy),
                                    bg="#33ccff", font=self.font)
        self.energy_label.grid(row=3, column=1, sticky="ew")

        # Create attack button
        self.attack_button = tk.Button(self, text="Attack", font=self.font,
                                        command=self.attack_menu)
        self.attack_button.grid(row=4, column=1, sticky="ew", columnspan=1)

        # Create improve button
        self.improve_button = tk.Button(self, text="Improve", font=self.font,
                                         command=self.improve_menu)
        self.improve_button.grid(row=4, column=2, sticky="ew")

        # Create log window
        self.log = tk.Text(self, height=10, wrap="word",
                            yscrollcommand="set", state="disabled")
        self.log.grid(row=1, column=3, columnspan=1, rowspan=4, sticky="ns")

    def log_action(self, message, next_turn=True):
        # Have to set log state to normal to modify
        self.log.config(state="normal")
        # Try catch for logging. Will error if privledges have been changed
        try:
            log_file = open("PublicFiles/LogFile.txt", "a")
            # Show message without header if game is starting
            if not next_turn:
                # Update log file in PublicFiles
                log_file.write(message+"\n")
                self.log.insert(tk.END, message + "\n")
            # Format to show game output each turn
            else:
                log_file.write("Turn " + str(self.turn) + ": " + message+"\n")
                self.log.insert(tk.END, "Turn " + str(self.turn) + ": " + message + "\n")
            log_file.close()
        except:
            self.log.insert(tk.END, "Error! Cannot access log file. Reading privledges may have been abused\n")
        # Disable ability to edit window
        self.log.config(state="disabled")
        # Autoscroll to bottom
        self.log.yview(tk.END)

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

    def normal_attack(self, damage):
        self.enemy_health -= damage
        self.enemy_health_label.config(text="Enemy Health: " + str(self.enemy_health))
        self.log_action("Player dealt 1 damage to enemy!")
        self.sub_atk.destroy()
        self.update_turn()

    def update_energy(self, energy):
        self.energy -= energy
        self.energy_label.config(text="Energy: " + str(self.energy))
        # Disable improve button if out of energy
        if self.energy == 0:
            self.improve_button.config(state="disabled")

    def update_turn(self):
        self.turn += 1
        self.turn_label.config(text="Turn " + str(self.turn))
        # Simulate changing turn to foe
        if self.turn % 2 == 0:
            self.CurID = self.ID
        else:
            self.CurID = self.FoeID

    def attack_menu(self):
        # Create attack sub menu
        self.sub_atk = tk.Toplevel(self.root)

        # Disable master menu to prevent launching multiple windows
        self.sub_atk.grab_set()

        # Configure rows and columns
        self.sub_atk.rowconfigure(1, pad=25)
        self.sub_atk.rowconfigure(2, pad=5)
        self.sub_atk.rowconfigure(3, pad=5)
        self.sub_atk.rowconfigure(4, pad=5)
        self.sub_atk.rowconfigure(5, pad=5)

        # Create label for new menu
        self.sub_title = tk.Label(self.sub_atk, text="Select Attack", font="arial 24 bold", width=20)
        # Define attack buttons
        self.sub_normal_atk = tk.Button(self.sub_atk, text="Normal Attack", font=self.font, width=25,
                                            command= lambda: self.normal_attack(1), bg="red")
        self.sub_spy = tk.Button(self.sub_atk, text="Spy enemy files", font=self.font, width=25,
                                            command= lambda: self.log_action("Feature coming soon!", False), bg="red")
        self.sub_change_priv = tk.Button(self.sub_atk, text="Change enemy log privledges", font=self.font, width=25,
                                            command= lambda: attack_permissions(self, self.CurID), bg="red")
        self.sub_DoS = tk.Button(self.sub_atk, text="Execute DoS", font=self.font, width=25,
                                            command= lambda: self.log_action("Feature coming soon!", False), bg="red")

        # Configure button states if enough energy is present
        # Normal attack energy
        if self.energy < self.attack_energy:
            self.sub_normal_atk.configure(state="disabled")
        # Spy energy
        if self.energy < self.spy_energy:
            self.sub_spy.configure(state="disabled")
        # Change privledge energy
        if self.energy < self.change_priv_energy:
            self.sub_change_priv.configure(state="disabled")
        # DoS energy
        if self.energy < self.DoS_energy:
            self.sub_DoS.configure(state="disabled")

        # Pack attack buttons
        self.sub_title.grid(row=1, column=1)
        self.sub_normal_atk.grid(row=2, column=1)
        self.sub_spy.grid(row=3, column=1)
        self.sub_change_priv.grid(row=4, column=1)
        self.sub_DoS.grid(row=5, column=1)

    def improve_menu(self):
        # Create attack sub menu
        self.sub_def = tk.Toplevel(self.root)
        # Disable master menu to prevent launching multiple windows
        self.sub_def.grab_set()

        # Configure rows and columns
        self.sub_def.rowconfigure(1, pad=25)
        self.sub_def.rowconfigure(2, pad=5)
        self.sub_def.rowconfigure(3, pad=5)
        self.sub_def.rowconfigure(4, pad=5)
        self.sub_def.rowconfigure(5, pad=5)

        # Create label for new menu
        self.sub_title = tk.Label(self.sub_def, text="Select Improvement", font="arial 24 bold", width=20)
        # Define attack buttons
        self.sub_impv_energy = tk.Button(self.sub_def, text="Improve energy gain", font=self.font, width=25,
                                            command= lambda: self.update_energy(1), bg="#33ccff")
        self.sub_def_spy = tk.Button(self.sub_def, text="Patch file leakage", font=self.font, width=25,
                                            command= lambda: self.log_action("Feature coming soon!", False), bg="#33ccff")
        self.sub_def_priv = tk.Button(self.sub_def, text="Patch file privledges", font=self.font, width=25,
                                            command= lambda: prevent_log_lockout(self), bg="#33ccff")
        self.sub_def_DoS = tk.Button(self.sub_def, text="Patch DoS vulnerability", font=self.font, width=25,
                                            command= lambda: self.log_action("Feature coming soon!", False), bg="#33ccff")
        self.sub_def_repair_log = tk.Button(self.sub_def, text="Repair logging output", font=self.font, width=25,
                                            command= lambda: repair_logging(self), bg="#33ccff")

        # Configure button states if enough energy is present
        # Patch Spy energy
        if self.energy < self.patch_spy_energy:
            self.sub_def_spy.configure(state="disabled")
        # Change privledge energy
        if self.energy < self.patch_priv_energy:
            self.sub_def_priv.configure(state="disabled")
        # DoS energy
        if self.energy < self.patch_DoS_energy:
            self.sub_def_DoS.configure(state="disabled")
        # Repair log energy. Also disable if file is writable already
        if self.energy < self.repair_log_energy or check_write():
            self.sub_def_repair_log.configure(state="disabled")

        # Pack attack buttons
        self.sub_title.grid(row=1, column=1)
        self.sub_impv_energy.grid(row=2, column=1)
        self.sub_def_spy.grid(row=3, column=1)
        self.sub_def_priv.grid(row=4, column=1)
        self.sub_def_DoS.grid(row=5, column=1)
        self.sub_def_repair_log.grid(row=6, column=1)
