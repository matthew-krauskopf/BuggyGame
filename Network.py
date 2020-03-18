import socket
HOST = '127.0.0.1'  # The server's hostname or IP address

def host(port, ip):
    # Establish socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn off blocking sends
    print(ip)
    s.bind((ip, port))
    # Listen to for client
    s.listen()
    conn, addr = s.accept()
    conn.setblocking(False)
    print('Connection Successful')
    return conn

def client(port, ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn off blocking sends
    s.connect((ip, port))
    print('Connection Successful')
    s.setblocking(False)
    return s

def send_action(gui, action):
    # Use $ as a message terminator
    gui.conn.send(bytearray(action+"#"+gui.ID+"$", "utf-8"))

def send_message(gui, message):
    # Sending only a single message
    gui.conn.send(bytearray(message, "utf-8"))

def recv_message(gui):
    # Stay in loop until message is received
    while True:
        try:
            # Wait until received, byt update GUI in the meantime
            message = gui.conn.recv(4096).decode("utf-8")
            message.strip()
            # Return message
            return message
        # Nothing to receive yet: update GUI
        except:
            gui.update_idletasks()
            gui.update()

def recv_action(gui):
    # Stay in loop until message is received
    while True:
        try:
            # Wait until received, byt update GUI in the meantime
            message = gui.conn.recv(4096).decode("utf-8")
            # Strip trailing whitespace
            message.strip()
            # If multiple messaged were received, split them on $ terminator
            actions = message.split("$")
            for action in actions:
                # Strip individual actions and split action from ID
                action = action.strip()
                # Grab action and request ID
                a, ID = action.split("#")
                # Reject blank actions
                if a != "":
                    # Keep receiving actions until "Done" is received
                    if a != "Done":
                        # If DoS patch applied, check duplicate ID's
                        if not gui.DoS_patch or not ID in gui.request_IDs:
                            # Send attack and ID to request stack
                            gui.stack.append(a)
                            gui.request_IDs.append(ID)
                        # All messages received: time to exit
                    else:
                        return
        # Nothing to receive yet: update GUI
        except:
            gui.update_idletasks()
            gui.update()