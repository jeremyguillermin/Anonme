#!/bin/bash

sudo mv -n /etc/tor/torrc /etc/tor/torrc.original
sudo mv data/torrc.config /etc/tor/torrc
cp data/torrc.start data/torrc.config