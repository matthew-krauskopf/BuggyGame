import subprocess

def change_permissions(perm, request_ID=None, host_ID=None, patch=None):
    if not patch:
        # No patch: allow chmod to happen without check
        subprocess.call(["chmod", perm, "PublicFiles/LogFile.txt"])
        return True
    else:
        # Patch: Check request ID
        if request_ID == host_ID:
            # Reject request if ID is not host
            subprocess.call(["chmod", perm, "PublicFiles/LogFile.txt"])
            return True
    return False