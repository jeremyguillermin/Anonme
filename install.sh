#!/bin/bash

sudo apt update
sudo apt install tor python3 python3-pip
chmod +x bash_cmd/*
pip3 install subprocess.run 
pip3 install simple-term-menu 
pip3 install termcolor 
pip3 install requests
sudo echo 'VirtualAddrNetwork 10.192.0.0/10' >> /etc/tor/torrc
sudo echo 'AutomapHostsOnResolve 1' >> /etc/tor/torrc
sudo echo 'TransPort 9040' >> /etc/tor/torrc
sudo echo 'DNSPort 53' >> /etc/tor/torrc