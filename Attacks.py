import subprocess

def change_permissions(GUI):
    # Change write permissions on enemy log file to prevent victim from seeing log
    subprocess.call(["chmod", "u-w", "PublicFiles/LogFile.txt"])
    GUI.log_action("Disabled enemy log file!")
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.change_priv_energy)
    # Close attack window
    GUI.sub_atk.destroy()