#!/bin/bash

sudo apt update
sudo apt install -y tor python3 python3-pip nyx
pip3 install subprocess.run simple-term-menu termcolor requests
echo -e "VirtualAddrNetwork 10.192.0.0/10\nAutomapHostsOnResolve 1\nTransPort 9040\nDNSPort 53" | sudo tee /etc/tor/torrc
