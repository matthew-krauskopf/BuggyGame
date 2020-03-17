import tkinter as tk
from Attacks import *
from Improvements import *

class VsGame(tk.Frame):
    def __init__(self, root=None, UserID=None, conn=None, is_host=True):
        # Keep: don't know reason why
        super().__init__(root)
        # Set reference to root
        self.root = root
        # Set reference to socket
        self.conn = conn
        # Mark if host or client
        self.is_host = is_host
        # Name window
        self.master.title("Vul Game")
        # Restrict size of window
        self.root.resizable(0,0)
        # Set User ID
        self.ID = UserID
        # Set standard font
        self.font = "arial 14"
        # Set starting values
        self.time_left = 30
        self.health = 20
        self.enemy_health = 20
        # TODO set better value
        self.energy = 9
        self.turn = 0
        self.gain_energy = 1
        # Set energy costs for attacks
        self.attack_energy = 1
        self.spy_energy = 3
        self.change_priv_energy = 5
        self.DoS_energy = 10
        # Set energy costs for improvements
        self.patch_spy_cost = 5
        self.patch_priv_cost = 10
        self.patch_DoS_cost = 20
        self.repair_log_cost = 3
        self.reset_keyword_cost = 10
        # Set patching flags to emulate code patches
        self.permission_patch = False
        self.spy_patch = False
        # Create labels and buttons
        self.pack(fill=tk.BOTH, expand=True)
        self.set_layout()
        self.log_action("Game is ready!", False)
        self.update_turn()

    def set_layout(self):
        # Layout columns and rows for GUI
        self.columnconfigure(1, minsize=225)
        self.columnconfigure(2, minsize=225)

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

    def update_energy(self, energy):
        self.energy -= energy
        self.energy_label.config(text="Energy: " + str(self.energy))
        # Disable improve button if out of energy
        if self.energy == 0:
            self.improve_button.config(state="disabled")

    def new_turn_energy(self):
        self.energy += self.gain_energy
        self.energy_label.config(text="Energy: " + str(self.energy))

    def update_turn(self):
        # Set settings for enemy turn
        def enemy_turn():
            # Disable action buttons
            self.attack_button.config(state="disabled")
            self.improve_button.config(state="disabled")
            self.turn_label.config(text="Turn " + str(self.turn) + "\nEnemy's turn")

        def player_turn():
            # Enable action buttons
            self.new_turn_energy()
            self.attack_button.config(state="normal")
            self.improve_button.config(state="normal")
            self.turn_label.config(text="Turn " + str(self.turn) + "\nYour turn")

        # Increase turn counter
        self.turn += 1
        # Alternate turns
        if self.turn % 2 == 0:
            if self.is_host:
                enemy_turn()
            else:
                player_turn()
        else:
            if self.is_host:
                player_turn()
            else:
                enemy_turn()

    def attack_menu(self):

        def attack_input_menu(title):
            # Create attack input sub menu
            self.attack_input = tk.Toplevel(self.root)

            # Disable master menu to prevent launching multiple windows
            self.attack_input.grab_set()

            # Configure rows and columns
            self.attack_input.rowconfigure(1, pad=25)
            self.attack_input.rowconfigure(2, pad=5)

            # Create label for new menu
            self.attack_input_label = tk.Label(self.attack_input, text=title, font="arial 24 bold", width=20)
            self.input_field = tk.Entry(self.attack_input, width=25, font=self.font)
            # Submit button for spying on files. Input must be provided
            if title == "Select File":
                self.submit = tk.Button(self.attack_input, text="Submit", font=self.font, width=15,
                                                command= lambda: peak_files(self, self.input_field.get()), bg="gray")
            # Submit button for standard attack. Leave blank if no keyword
            elif title.startswith("Use bonus keyword?"):
                self.submit = tk.Button(self.attack_input, text="Submit", font=self.font, width=15,
                                                command= lambda: normal_attack(self, self.input_field.get()), bg="gray")
            # Pack widgets
            self.attack_input_label.grid(row=1, column=1)
            self.input_field.grid(row=2, column=1)
            self.submit.grid(row=3, column=1)

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
                                            command= lambda: attack_input_menu("Use bonus keyword? \n(Leave blank if no)"), bg="red")
        self.sub_spy = tk.Button(self.sub_atk, text="Spy enemy files", font=self.font, width=25,
                                            command= lambda: attack_input_menu("Select File"), bg="red")
        self.sub_change_priv = tk.Button(self.sub_atk, text="Change enemy log privledges", font=self.font, width=25,
                                            command= lambda: attack_permissions(self, self.ID), bg="red")
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
        self.sub_def.rowconfigure(6, pad=5)

        # Create label for new menu
        self.sub_title = tk.Label(self.sub_def, text="Select Improvement", font="arial 24 bold", width=20)
        # Define attack buttons
        self.sub_impv_energy = tk.Button(self.sub_def, text="Improve energy gain", font=self.font, width=25,
                                            command= lambda: improve_energy_gains(self), bg="#33ccff")
        self.sub_def_spy = tk.Button(self.sub_def, text="Patch file leakage", font=self.font, width=25,
                                            command= lambda: prevent_file_leakage(self), bg="#33ccff")
        self.sub_def_priv = tk.Button(self.sub_def, text="Patch file privledges", font=self.font, width=25,
                                            command= lambda: prevent_log_lockout(self), bg="#33ccff")
        self.sub_def_DoS = tk.Button(self.sub_def, text="Patch DoS vulnerability", font=self.font, width=25,
                                            command= lambda: self.log_action("Feature coming soon!", False), bg="#33ccff")
        self.sub_def_repair_log = tk.Button(self.sub_def, text="Repair logging output", font=self.font, width=25,
                                            command= lambda: repair_logging(self), bg="#33ccff")
        self.sub_def_reset_keyword = tk.Button(self.sub_def, text="Reset keyword", font=self.font, width=25,
                                            command= lambda: reset_keyword(self), bg="#33ccff")

        # Configure button states if enough energy is present
        # Patch Spy energy
        if self.energy < self.patch_spy_cost:
            self.sub_def_spy.configure(state="disabled")
        # Change privledge energy
        if self.energy < self.patch_priv_cost:
            self.sub_def_priv.configure(state="disabled")
        # DoS energy
        if self.energy < self.patch_DoS_cost:
            self.sub_def_DoS.configure(state="disabled")
        # Repair log energy. Also disable if file is writable already
        if self.energy < self.repair_log_cost or check_write():
            self.sub_def_repair_log.configure(state="disabled")
        # Reset Keyword energy
        if self.energy < self.reset_keyword_cost:
            self.sub_def_reset_keyword.configure(state="disabled")

        # Pack attack buttons
        self.sub_title.grid(row=1, column=1)
        self.sub_impv_energy.grid(row=2, column=1)
        self.sub_def_spy.grid(row=3, column=1)
        self.sub_def_priv.grid(row=4, column=1)
        self.sub_def_DoS.grid(row=5, column=1)
        self.sub_def_repair_log.grid(row=6, column=1)
        self.sub_def_reset_keyword.grid(row=7, column=1)


    def interpret_action(self, message):
        # Normal attack
        segments = message.split()
        if segments[0] == "Normal":
            if len(segments) == 2:
                normal_attack(self, segments[1], False)
            else:
                normal_attack(self, "", False)
        # Spy on file
        elif segments[0] == "Spy":
            peak_files(self, segments[1], False)
        # Change write permissions
        elif segments[0] == "Chmod":
            attack_permissions(self, segments[1], False)
        # Opponent improved their system
        else:
            self.log_action("Enemy spent energy to improve system")
            # Update turn count
            self.update_turn()