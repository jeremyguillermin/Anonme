#!/bin/bash

sudo iptables -F
sudo iptables -t nat -F
sudo service tor stop