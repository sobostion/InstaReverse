#!/usr/bin/bash

sudo apt-get -y install libxi6 libgconf-2-4 python-pip
sudo pip install pyvirtualdisplay
sudo pip install selenium
sudo pip install filedepot


sudo apt-get -y install chromium-chromedriver
sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver


