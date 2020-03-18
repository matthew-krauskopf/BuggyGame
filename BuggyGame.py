from VsGUI import *
from Utils import *
from Network import *
from sys import argv

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
    if len(argv) > 3 or len(argv) == 2:
        print("Invalid usage!\n py BuggyGame.py [host/client] [port]")
        exit()
    # No internet connect: debug against self
    elif len(argv) == 1:
        return True, None
    # Host/client, port
    else:
        return argv[1] == "host", int(argv[2])

def PlayGame(gui):
    # Flow for enemy turn
    def enemy_turn():
        # Get action
        recv_action(gui)
        # Execute action received from enemy
        gui.execute_queued_action()
        # Update GUI
        gui.update_idletasks()
        gui.update()

    def player_turn():
        if gui.stack != []:
            gui.execute_queued_action()
        gui.update_idletasks()
        gui.update()

    # Launch application for both
    player_turn()
    while gui.health > 0 and gui.enemy_health > 0:
        # Host goes on odd turn, guest on even turns
        if gui.turn % 2 == 0:
            if gui.is_host:
                # I am host, Opponent's turn
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
    # Game has ended
    gui.end_game()
    # Do busy work until user closes app
    while True:
        gui.mainloop()

def on_quit():
    # Exits program gracefully
    exit()

def main():
    # Sets up game and connects players
    SetStartingFiles()
    UserID = GenerateUserID()
    is_host, port = GetRuntimeArgs()
    root = tk.Tk()
    # Handle exiting program gracefully
    root.protocol("WM_DELETE_WINDOW", on_quit)
    gui = VsGame(root, UserID, Connect(is_host, port), is_host)
    PlayGame(gui)

main()