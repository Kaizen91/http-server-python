import socket

song = """
Heeey HeeeEEEEyyyyy Baaaby!
Ooooooooh! Aaaaaaah!
I want to knoOOOooOOO will you be my girl?
"""

HOST, PORT = '', 8888

def gen_lines():
    for line in song.split('\n'):
        yield line

# Create a socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind
listen_socket.bind((HOST, PORT))
# listen
listen_socket.listen(1)
print(f'serving HTTP on port {PORT}')
lines = gen_lines()

# accept
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)

    template = f"""\
HTTP/1.1 200 OK

{next(lines)}
"""
    http_response =  bytes(template, 'utf-8')
    client_connection.sendall(http_response)
    client_connection.close()






