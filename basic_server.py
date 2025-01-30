import socket
from Song import Song

song = Song()
HOST, PORT = '', 8888

# Create a socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind
listen_socket.bind((HOST, PORT))
# listen
listen_socket.listen(1)
print(f'serving HTTP on port {PORT}')

# accept
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    line = song.next_line()

    template = f"""\
HTTP/1.1 200 OK

{line}
"""
    http_response =  bytes(template, 'utf-8')
    client_connection.sendall(http_response)
    client_connection.close()






