from Utils import *
from Network import send_action, recv_action

def normal_attack(GUI, input_keyword, outgoing=True):
    damage = 1
    # Attacker
    if outgoing:
        # Send attack to opponent
        send_action(GUI.conn, "Normal " + input_keyword)
        # Receive damage dealt successfully
        damage = int(recv_action(GUI))
        # Subtract health from opponent
        GUI.enemy_health -= damage
        # Update health label
        GUI.enemy_health_label.config(text="Enemy Health: " + str(GUI.enemy_health))
        # Report damage dealth
        GUI.log_action("Player dealt " + str(damage) + " damage to enemy!")
        # Update energy
        GUI.update_energy(GUI.attack_energy)
        # Destory attack menus
        GUI.sub_atk.destroy()
        GUI.attack_input.destroy()
        # Update turn count
        GUI.update_turn()
    else:
        # Victim
        if input_keyword != "":
            # Do standard damange to enemy. Bonus damage if keyword is used.
            keyword = read_file(GUI, "PrivateFiles/keywords.txt")[0]
            # Check if input keyword matches stored keyword
            if input_keyword == keyword:
                damage = 5
        # Send damage dealt back to attacker
        send_action(GUI.conn, str(damage))
        # Subtract health from self
        GUI.health -= damage
        # Update health label
        GUI.health_label.config(text="My Health: " + str(GUI.health))
        # Report damage dealth
        GUI.log_action("Enemy dealt " + str(damage) + " damage to Player!")
        # Update turn count
        GUI.update_turn()

def attack_permissions(GUI, foe_ID):
    # Change write permissions on enemy log file to prevent victim from seeing log
    if change_permissions("u-w", foe_ID, GUI.ID, GUI.permission_patch):
        GUI.log_action("Disabled enemy log file!")
    # Report failure if log file permissions patched
    else:
        GUI.log_action("Attack failed! Could not disable enemy log file")
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.change_priv_energy)
    # Close attack window
    GUI.sub_atk.destroy()

def peak_files(GUI, wanted_file, outgoing=True):
    # Attacker
    if outgoing:
        if wanted_file == "":
            return
        # Send attack to opponent
        send_action(GUI.conn, "Spy " + wanted_file)
        # Wait for response
        info = recv_action(GUI)
        # Display info in log window
        GUI.log_action("Content of " + wanted_file + ": \n" + info)
        # Update turn count
        GUI.update_turn()
        # Update energy
        GUI.update_energy(GUI.spy_energy)
        # Close attack windows
        GUI.sub_atk.destroy()
        GUI.attack_input.destroy()
    # Victim
    else:
        # Set default target folder as PublicFiles/
        file_prefix = "PublicFiles/"
        # Grab content of file
        lines = read_file(GUI, file_prefix+wanted_file)
        # Format file lines
        content = "".join("--> "+line.strip()+"\n" for line in lines)
        # Send info to attacker
        send_action(GUI.conn, content)
        # Report data breach (?)
        GUI.log_action("Enemy studied your log file!")
        # Update turn count
        GUI.update_turn()