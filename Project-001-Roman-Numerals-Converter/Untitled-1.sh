#!/bin/bash -x
yum update -y
yum install python3 -y
pip3 install flask
cd /home/ec2-user
FOLDER="https://raw.githubusercontent.com/Younaluna/my-repository/main/Project-001-Roman-Numerals-Converter"
wget ${FOLDER}/app.py
mkdir templates
cd templates
wget ${FOLDER}/templates/index.html
wget ${FOLDER}/templates/result.html
cd ..
python3 app.py