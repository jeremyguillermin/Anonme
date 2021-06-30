#!/bin/bash

sudo apt update
sudo apt install tor python3 python3-pip
chmod +x bash_cmd/*
pip3 install subprocess.run 
pip3 install simple-term-menu 
pip3 install termcolor 
pip3 install requests