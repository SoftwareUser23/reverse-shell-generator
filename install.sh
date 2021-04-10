#!/usr/bin/bash

echo  "Clonning repository "
git clone https://github.com/SoftwareUser23/reverse-shell-generator

echo  "Changing Directory and Installing Dependencies "
cd reverse-shell-generator && pip3 install -r requirements.txt
exec bash 



