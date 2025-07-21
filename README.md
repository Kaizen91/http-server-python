# http-server-python
exploration of python's socket library

This project is loosely based on this series of articles: https://ruslanspivak.com/lsbaws-part1/

I basically wanted to build a simple webserver that loops over the lyrics to DJ Otzi's hit song Hey Baby (https://www.youtube.com/watch?v=s0GIaJuan9Y) 

I also wanted to explore concurrency in python so I've built that server in 3 ways: using processes, threads, and the asyncio library.

to get a basic idea of the setup you can run basic_server.py and then run curl localhost:8888 in another terminal several times.  The problem with this set up is that if you ping the server from another connection, for example another terminal session, you won't start over at the beginning of the song you'll just pick up were the last connection left off.  That's not what we want; we want each session to be independent.

We will handle this with processes, threads, and asyncio in process_server.py, threads_server.py and asyncio_server.py respectively.  Each file can be run and then connected with via multiple different connection each maintaining a record of where each connection is in terms of the song.
