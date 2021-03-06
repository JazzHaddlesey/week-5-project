#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo "Killing existing processes"
# sudo kill $(cat gunicornpidfile)
python3 create.py
python3 -m gunicorn -D -b  0.0.0.0:5000 -w 4 application:app  -p gunicornpidfile 