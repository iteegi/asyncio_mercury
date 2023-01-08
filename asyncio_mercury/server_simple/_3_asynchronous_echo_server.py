import asyncio
import logging
import socket
import signal

from asyncio import AbstractEventLoop
from typing import List


async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    """Expect input from the user.

    After receiving the data, send it back to the client.

    :param connection: socket object usable to send and receive data on the connection
    :type connection: socket
    :param loop: event loop
    :type loop: AbstractEventLoop

    """
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('got data!')
            if data == b'boom\r\n':
                raise Exception("Unexpected network error")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


echo_tasks = []


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop) -> None:
    """For each connection, create a task that wraps the echo coroutine.

    :param server_socket: connection socket
    :type server_socket: socket
    :param loop: event loop
    :type loop: AbstractEventLoop

    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()


async def close_echo_tasks(echo_tasks: List[asyncio.Task]) -> None:
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass


async def main() -> None:
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await listen_for_connection(server_socket, loop)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
