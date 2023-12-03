#!/bin/bash

sudo yum -y install git
sudo yum -y install postgresql-devel

sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y zlib zlib-devel bzip2-devel openssl-devel sqlite-devel readline-devel
curl https://pyenv.run | bash


