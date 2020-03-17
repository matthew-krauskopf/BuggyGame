import socket
HOST = '127.0.0.1'  # The server's hostname or IP address


def host(port):
    # Establish socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    # Listen to for client
    s.listen()
    conn, addr = s.accept()
    print('Connection Successful')
    return conn

def client(port):
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    print('Connection Successful')
    return s

def send_action(conn, action):
    conn.send(bytearray(action, "utf-8"))


def recv_action(conn):
    action = conn.recv(4096).decode("utf-8")
    action.strip()
    return action
