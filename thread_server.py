import socket
import os
import time
import threading
import socketserver

from Song import Song

HOST, PORT = '', 8888
REQUEST_QUEUE_SIZE = 5
BUFF_SIZE = 1024


class ThreadedTCPRequestHandeler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, serve):
        super().__init__(request, client_address, server)

    def handle(self):
        line = song.next_line()
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        template = f"""\
    HTTP/1.1 200 OK

    {cur_thread}: {line}
    """
        http_response =  bytes(template, 'utf-8')
        self.request.sendall(http_response)
        time.sleep(8)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


song = Song()

if __name__ == '__main__':
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandeler)
    ip, port = server.server_address
    print(f'server running on port {PORT}')
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
