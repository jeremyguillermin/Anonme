#!/bin/bash

check_ip() 
{
    local url_list=(
        'https://ipleak.net/json/'
        'https://api.myip.com/'
        'https://ipinfo.io/'
        'http://ip-api.com/'
    )

    for url in "${url_list[@]}"; do
        local request="$(curl -s "$url")"
        local response="$?"

        if [[ "$response" -ne 0 ]]; then
            continue
        fi

        printf "%s\\n" "${request}"
        break
    done
}

check_ip