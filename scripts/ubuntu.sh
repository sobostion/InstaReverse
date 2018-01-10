#!/usr/bin/bash

sudo apt-get update
sudo apt-get -y install libxi6 libgconf-2-4 python-pip xvfb
sudo pip install pyvirtualdisplay
sudo pip install selenium
sudo pip install filedepot

# install pillow
sudo apt-get -y install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python-dev
sudo pip install pillow

# for screenshots
sudo apt-get -y install chromium-chromedriver
sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver

sudo mv ../config/nginx /etc/nginx/sites-available/default

# for flask
sudo pip install flask flask-WTF
export FLASK_APP=main.py
(
	cd ../app
	flask run
)
