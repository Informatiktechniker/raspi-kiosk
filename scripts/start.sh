#!/usr/bin/env bash

cd /home/bszw/Documents/raspi-kiosk
source ./.venv/bin/activate

#sleep 60# Not needed as we run it as a service that delays start until network online. When run as a cron-job it is needed

python /home/bszw/Documents/raspi-kiosk/main.py https://digikabu.de/DisplayPanel?config=Config_EDV_Schulen_Lehrerzimmer

exit 0
