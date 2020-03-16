from Utils import *

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

def peak_files(GUI, wanted_file):
    # Grab content of file
    content = read_file(GUI, wanted_file)
    GUI.log_action("Content of " + wanted_file + ": \n" + content)
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.spy_energy)
    # Close attack window
    GUI.sub_atk.destroy()