from VsGUI import *
from Utils import *
from Network import *

import sys

def Connect(HoC, port):
    if HoC and port:
        if HoC == "host":
            host(port)
        else:
            client(port)
        exit()
    else:
        return None

def GetRuntimeArgs():
    # Grab port and if host or client
    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Invalid usage!\n py BuggyGame.py [host/client] [port]")
        exit()
    # No internet connect: debug against self
    elif len(sys.argv) == 1:
        return None, None
    # Host/client, port
    else:
        return sys.argv[1], int(sys.argv[2])


def main():
    # Sets up game and connects players
    SetStartingFiles()
    UserID = GenerateUserID()
    HoC, port = GetRuntimeArgs()
    root = tk.Tk()
    gui = VsGame(root, UserID, Connect(HoC, port))
    gui.mainloop()

main()