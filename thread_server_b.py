import socket
import os
import time
from Song import Song
from concurrent import futures
HOST, PORT = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection, line):
    request_data = client_connection.recv(1024)
    print(
            'child pid {pid}. parent pid {ppid}'.format(
                pid=os.getpid(),
                ppid=os.getppid()
                )
            )

    template = f"""\
HTTP/1.1 200 OK

{line}
"""
    http_response =  bytes(template, 'utf-8')
    client_connection.sendall(http_response)
    time.sleep(8)

def serve_forever():
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
        # try:
            # client_connection, client_address = listen_socket.accept()
        # except 
        client_connection, client_address = listen_socket.accept()
        line = song.next_line()

song = Song()


if __name__ == '__main__':
    serve_forever()
