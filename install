#!/bin/bash

apt update
apt install -y which obfs4proxy tor python python-pip
pip install -r requirements.txt

echo пастани один мост сюда
read bridge

# Define the multiline text you want to append
multiline_text="
UseBridges 1 
ClientTransportPlugin obfs4 exec $(which obfs4proxy) 
Bridge $bridge
"

# Append the multiline text to a file named "myfile.txt"
echo "$multiline_text" >> $PREFIX/etc/tor/torrc
