#!/usr/bin/python

from depot.manager import DepotManager
from selenium import webdriver
from pyvirtualdisplay import Display

depot = DepotManager.get()
display = Display(visible=0, size=(800, 800))  
display.start()
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.set_window_size(800, 800) # set the window size that you need 
driver.get('https://github.com')
driver.save_screenshot('github.png')
