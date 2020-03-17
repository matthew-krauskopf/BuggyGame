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
    conn.send(bytearray(action, "utf-8"))

def recv_action(gui):
    # Stay in loop until message is received
    while True:
        try:
            # Wait until received, byt update GUI in the meantime
            action = gui.conn.recv(4096).decode("utf-8")
            action.strip()
            return action
        # Nothing to receive yet: update GUI
        except:
            gui.update_idletasks()
            gui.update()