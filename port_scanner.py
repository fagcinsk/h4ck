#!/usr/bin/env python3
from queue import Queue
import socket
from threading import Thread
from fire import Fire
from lib.utils import parse_range_list


def port_check(target):
    with socket.socket() as s:
        if s.connect_ex(target) == 0:
            print('%s:%s' % target, 'open')


def scan(queue):
    while True:
        port_check(queue.get())
        queue.task_done()


def main(ip: str = '127.0.0.1', ports: str = '1-1024', t: float = 1, w: int = 64):
    queue = Queue()
    socket.setdefaulttimeout(t)

    args = (queue,)

    for _ in range(w):
        Thread(target=scan, args=args, daemon=True).start()

    for port in parse_range_list(ports):
        target = (ip, port)
        queue.put(target)

    queue.join()


if __name__ == "__main__":
    Fire(main)
