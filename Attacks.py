from Utils import *
from Network import send_action, send_message, recv_message

def normal_attack(GUI, input_keyword, outgoing=True):
    damage = 1
    # Attacker
    if outgoing:
        # Send attack to opponent
        send_action(GUI, "Normal " + input_keyword)
        # Send "Done" message
        send_action(GUI, "Done")
        # Receive damage dealt successfully
        damage = int(recv_message(GUI))
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
            keyword = read_file(GUI, "PrivateFiles/keyword.txt")[0]
            # Check if input keyword matches stored keyword
            if input_keyword == keyword:
                damage = 5
        # Send damage dealt back to attacker
        send_message(GUI.conn, str(damage))
        # Subtract health from self
        GUI.health -= damage
        # Update health label
        GUI.health_label.config(text="My Health: " + str(GUI.health))
        # Report damage dealt
        GUI.log_action("Enemy dealt " + str(damage) + " damage to Player!")
        # Update turn count
        GUI.update_turn()

def attack_permissions(GUI, request_ID, outgoing=True):
    # Attacker
    if outgoing:
        # Send attack to opponent
        send_action(GUI, "Chmod ")
        # Send "Done" message
        send_action(GUI, "Done")
        # Wait for response
        info = recv_message(GUI)
        if info == "Success":
            GUI.log_action("Player disabled enemy log file!")
        else:
            GUI.log_action("Attack failed! Could not disable enemy log file")
        # Update turn count
        GUI.update_turn()
        # Update energy
        GUI.update_energy(GUI.change_priv_energy)
        # Close attack window
        GUI.sub_atk.destroy()
    # Victim
    else:
        # Remove write permissions on log file to prevent victim from seeing log
        if change_permissions("u-w", request_ID, GUI.ID, GUI.permission_patch):
            # Send success
            send_message(GUI, "Success")
            GUI.log_action("Enemy changed log file permissions!")
        # Report failure if log file permissions patched
        else:
            send_message(GUI, "Failure")
            GUI.log_action("Enemy failed to disable log file!")
        # Update turn count
        GUI.update_turn()


def peak_files(GUI, wanted_file, outgoing=True):
    # Attacker
    if outgoing:
        if wanted_file == "":
            return
        # Send attack to opponent
        send_action(GUI, "Spy ")
        # Send "Done" message
        send_action(GUI, "Done")
        # Wait for response
        info = recv_message(GUI)
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
        send_message(GUI.conn, content)
        # Report data breach (?)
        if GUI.spy_patch and ".." in wanted_file:
            GUI.log_action("Enemy was prevented from reading illegal file!")
        else:
            GUI.log_action("Enemy studied your log file!")
        # Update turn count
        GUI.update_turn()

def DoS(GUI):
    # Flood enemy with 3 "skip turn" requests
    for z in range(3):
        send_action(GUI, "Skip ")
    # Tell enemy this was a DoS
    send_action(GUI, "DoS")
    # Send "Done" message
    send_action(GUI, "Done")
     # Display info in log window
    GUI.log_action("Opponent has been DoS'd!")
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.DoS_energy)
    # Close attack windows
    GUI.sub_atk.destroy()