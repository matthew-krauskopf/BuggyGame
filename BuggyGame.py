from VsGUI import *
from Utils import *
from Network import *
import sys

def Connect(is_host, port):
    # Connect host and client
    if port:
        if is_host:
            return host(port)
        else:
            return client(port)
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
        return sys.argv[1] == "host", int(sys.argv[2])

def PlayGame(gui):
    # Flow for enemy turn
    def enemy_turn():
        # Get action and interpret what to do
        action = recv_action(gui)
        gui.interpret_action(action)
        # Update GUI
        gui.update_idletasks()
        gui.update()

    def player_turn():
        gui.update_idletasks()
        gui.update()

    # Launch application for both
    player_turn()
    while gui.health > 0 or gui.enemy_health > 0:
        # Host goes on odd turn, guest on even turns
        if gui.turn % 2 == 0:
            if gui.is_host:
                # I am host, Opponent's turn
                # Get action and interpret what to do
                enemy_turn()
            else:
                # I am guest, my turn
                player_turn()
        else:
            if gui.is_host:
                # I am host, my turn
                player_turn()
            else:
                # I am guest, opponent's turn
                enemy_turn()

def main():
    # Sets up game and connects players
    SetStartingFiles()
    UserID = GenerateUserID()
    is_host, port = GetRuntimeArgs()
    root = tk.Tk()
    gui = VsGame(root, UserID, Connect(is_host, port), is_host)
    PlayGame(gui)

main()