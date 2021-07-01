# Anonme
This tool allows you to route all your network traffic through Tor. You can choose which countries you want to enter, exit, and which ones you want to exclude. Tool developed for Debian

# Functions
You can configure your Tor nodes.
![Peek 01-07-2021 22-22](https://user-images.githubusercontent.com/85474922/124185238-fdb1eb00-daba-11eb-94f1-f1f6575425d6.gif)

Search for .onion sites . At the moment you can't search them with Tor enabled but it will be possible soon.
![Peek 01-07-2021 21-55](https://user-images.githubusercontent.com/85474922/124182401-15877000-dab7-11eb-8046-a2bd2f8952c1.gif)

View your Tor relay information.
![Peek 01-07-2021 22-17](https://user-images.githubusercontent.com/85474922/124184622-24bbed00-daba-11eb-916e-7acc4a3a80a8.gif)

# Requiments
sudo, tor, iptables, nyx

python3 : subprocess, simple-term-menu, termcolor, requests

# Install
git clone https://github.com/x0Dsj/anonme

cd anonme

chmod +x install.sh

./install.sh

# Start the tool 
python3 anonme.py

# Licence 
GNU General Public License v3.0
