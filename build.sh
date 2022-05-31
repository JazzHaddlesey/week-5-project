#!/bin/bash
sudo apt install python3 python3-pip python3-venv -y
pyhton -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html
