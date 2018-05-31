import socket
import datetime
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 4444))
    sock.listen(1)
    conn, addr = sock.accept()

    print('connected:', addr)
    time = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
    conn.send(time.encode())
    conn.close()
finally:
    exit()
