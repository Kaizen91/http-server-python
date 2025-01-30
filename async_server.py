import socket
import asyncio
import sys
from asyncio.trsock import TransportSocket
from typing import cast
from Song import Song

HOST, PORT = '', 8888

song = Song()

async def supervisor(host: str, port: int) -> None:
    server = await asyncio.start_server(handle_request, host, port)
    socket_list = cast(tuple([TransportSocket, ...]), server.sockets)
    addr = socket_list[0].getsockname()
    print(f'serving on {addr}. Hit Ctrl-C to stop.')
    await server.serve_forever()


async def handle_request(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    client = writer.get_extra_info('peername')
    while True:
        await reader.readline()
        line = song.next_line()
        template = f"""\
{line}
    """
        response = template.encode()
        writer.write(response)
        await writer.drain()


def main(host=HOST, port=PORT):
    port = int(port)
    try:
        asyncio.run(supervisor(host, port))
    except KeyboardInterrupt:
        print('\nshutting down server')


if __name__== '__main__':
    main(*sys.argv[1:])
