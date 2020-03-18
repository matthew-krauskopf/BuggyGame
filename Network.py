import socket
import errno
HOST = '127.0.0.1'  # The server's hostname or IP address

def host(port):
    # Establish socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn off blocking sends
    s.bind((HOST, port))
    # Listen to for client
    s.listen()
    conn, addr = s.accept()
    conn.setblocking(False)
    print('Connection Successful')
    return conn

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Turn off blocking sends
    s.connect((HOST, port))
    print('Connection Successful')
    s.setblocking(False)
    return s

def send_action(conn, action):
    # Use $ as a message terminator
    conn.send(bytearray(action+"$", "utf-8"))

def send_message(conn, message):
    # Sending only a single message
    conn.send(bytearray(message, "utf-8"))

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
            print("Message received: ", message)
            # If multiple messaged were received, split them on $ terminator
            actions = message.split("$")
            for action in actions:
                # Strip individual actions
                a = action.strip()
                if a != "":
                    # Keep receiving actions until "Done" is received
                    if a != "Done":
                        print("Received ", a)
                        gui.stack.append(a)
                    # All messages received: time to execute top action
                    else:
                        print("My stack is this: ")
                        print(gui.stack)
                        return
        # Nothing to receive yet: update GUI
        except:
            gui.update_idletasks()
            gui.update()