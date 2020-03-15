import subprocess

def repair_logging(GUI):
    # Change write permissions on enemy log file to prevent victim from seeing log
    subprocess.call(["chmod", "u+w", "PublicFiles/LogFile.txt"])
    GUI.log_action("Repaired logging!")
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.change_priv_energy)
    # Close improvement window
    GUI.sub_def.destroy()

def prevent_log_lockout(GUI):
    # Change settings so that log file permissions cannot be changed by enemy
    pass

def check_write():
    # Check write permission of log file
    try:
        test = open("PublicFiles/LogFile.txt", "a")
        test.close()
        return True
    except:
        return False