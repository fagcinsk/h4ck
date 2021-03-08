#!/usr/bin/env python3
from pathlib import Path
from lib.net import RTSPConnection
from lib.fuzz import Fuzz, Brute, ListFile
import os

from fire import Fire

DATA_PATH = Path(os.path.dirname(__file__)) / 'data'
PATHS_FILE = DATA_PATH / 'rtsp_paths1.txt'
CREDS_FILE = DATA_PATH / 'rtsp_creds_my.txt'

paths = ListFile(PATHS_FILE)
creds = ListFile(CREDS_FILE)


def process_host(host):
    with RTSPConnection(host) as connection:
        for fuzz_result in Fuzz(connection, paths):
            existing_path = fuzz_result.path

            if fuzz_result.ok:
                return connection.url(existing_path)
            elif fuzz_result.auth_needed:
                cred = Brute(connection, existing_path, creds).run()
                if cred:
                    return connection.url(existing_path, cred)


def main(hosts_file):
    with open(hosts_file) as hf:
        for ln in hf:
            result = process_host(ln.rstrip())
            print(result)


if __name__ == "__main__":
    Fire(main)
