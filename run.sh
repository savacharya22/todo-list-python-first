#!/bin/bash


# check if python is installed


python3 -m venv .venv
source .venv/bin/activate
pip install colored
python3 main.py