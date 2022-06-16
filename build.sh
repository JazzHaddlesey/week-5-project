#!/bin/bash
echo "Installing packages"
sudo apt install python3 python3-pip python3-venv -y
echo "Setting up venv"
pyhton -m venv venv
source venv/bin/activate
echo "Installing dependencies"
pip3 install -r requirements.txt
echo "Running unit tests"
python3 -m pytest --cov=application --cov-report=html
echo " Copying files"
scp -r . jenkins@app-server:/home/jenkins/app
echo "Deploying app"
ssh jenkins@app-server < deploy.sh
