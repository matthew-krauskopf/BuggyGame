import subprocess
from Utils import *

def repair_logging(GUI):
    # Restore write permission on log file
    change_permissions("u+w", GUI.ID, GUI.ID, GUI.permission_patch)
    GUI.log_action("Repaired logging!")
    # Update turn count
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.change_priv_energy)
    # Close improvement window
    GUI.sub_def.destroy()

def prevent_log_lockout(GUI):
    # Set flag that permissions have been patched
    GUI.permission_patch = True
    GUI.log_action("Patch successful: Will now check for requester ID")
    # Update turn
    GUI.update_turn()
    # Update energy
    GUI.update_energy(GUI.patch_priv_energy)
    # Close improvement window
    GUI.sub_def.destroy()

def check_write():
    # Check write permission of log file
    try:
        test = open("PublicFiles/LogFile.txt", "a")
        test.close()
        return True
    except:
        return False