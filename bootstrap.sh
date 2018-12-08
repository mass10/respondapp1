#!/bin/bash
virtualenv .
source bin/activate
pip3 install -r requirements.txt
python3 main.py address '0.0.0.0'
deactivate

