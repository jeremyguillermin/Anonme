#!/bin/bash

export red="$(tput setaf 1)"
export green="$(tput setaf 2)"
export reset="$(tput sgr0)"

die() 
{
    printf "${red}%s${reset}\\n" "[!] $@" >&2
    exit 1
}

msg() 
{
    printf "${b}${green}%s${reset} %s\\n\\n" "[OK]" "${@}"
}

if systemctl is-active tor.service >/dev/null 2>&1; then
        msg "Tor service is active"
    else
        die "Tor service is not running!"
    fi