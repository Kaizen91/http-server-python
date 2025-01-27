import socket
import os
import time


HOST, PORT = '', 8888
REQUEST_QUEUE_SIZE = 5

class Song():
    def __init__(self):
        self.lyrics = """Heeey HeeeEEEEyyyyy Baaaby!
            Ooooooooh! Aaaaaaah!
            I want to knoOOOooOOO will you be my girl?"""
        self.lines = self._gen_lines()

    def _gen_lines(self):
        for line in self.lyrics.split('\n'):
            yield line

    def next_line(self):
        try:
            return next(self.lines)
        except StopIteration:
            self.lines = self._gen_lines()
            return next(self.lines)


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
    time.sleep(20)


song = Song()


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
        client_connection, client_address = listen_socket.accept()
        line = song.next_line()

        pid = os.fork()
        if pid == 0: #child
            listen_socket.close() #close child copy
            handle_request(client_connection, line)
            client_connection.close()
            os._exit(0) #child exits here
        else: # parent
            client_connection.close()


if __name__ == '__main__':
    serve_forever()




