from VsGUI import *
from Utils import *
from Network import *
from sys import argv

def Connect(is_host, port, ip):
    # Connect host and client
    if port:
        if is_host:
            return host(port, ip)
        else:
            return client(port, ip)
    else:
        return None

def GetRuntimeArgs():
    # Grab port and if host or client
    # Debug call
    if len(argv) == 1:
        # Is host, no port, localhost
        return True, None, "127.0.0.1"
    elif len(argv) == 4:
        # Return host/client, port, and IP address
        return argv[1] == "host", int(argv[2]), argv[3]
    # Invalid usage
    else:
        print("Invalid usage!\npy BuggyGame.py [host/client] [port] [ip_address]")
        exit()

def update_game(gui):
    # Update screen
    try:
        gui.update_idletasks()
        gui.update()
    # Root has been destroyed: exit program
    except:
        exit()

def PlayGame(gui):
    # Flow for enemy turn
    def enemy_turn():
        # Get action
        recv_action(gui)
        # Execute action received from enemy
        gui.execute_queued_action()
        # Update GUI
        update_game(gui)

    def player_turn():
        if gui.stack != []:
            gui.execute_queued_action()
        update_game(gui)

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
        update_game(gui)

def main():
    # Sets up game and connects players
    SetStartingFiles()
    UserID = GenerateUserID()
    is_host, port, enemy_ip = GetRuntimeArgs()
    root = tk.Tk()
    gui = VsGame(root, UserID, Connect(is_host, port, enemy_ip), is_host)
    PlayGame(gui)

main()