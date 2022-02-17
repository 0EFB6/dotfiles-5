#!/bin/zsh

if [[ "$(route | awk '{print $8}' | tail -1)" == "eno1" ]]
then
	sed -i "s/wlo1/eno1/g" /home/ervin/.config/bandwidth-monitor/config.toml
else
	sed -i "s/eno1/wlo1/g" /home/ervin/.config/bandwidth-monitor/config.toml
fi

bandwidth-monitor -c /home/ervin/.config/bandwidth-monitor/config.toml
