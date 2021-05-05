import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import random

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def WebShare_Proxies():
	#
	#
	#
	url='https://proxy.webshare.io/proxy/list/download/****************/-/socks/username/direct/'
	myfile = requests.get(url)
	open('webshare_proxies.txt', 'wb').write(myfile.content)
	#
	df = pd.read_csv("webshare_proxies.txt", sep=":", header = None)
	df.columns=['IP','Port','username','password']
	#
	#
	#
	return df

print('Initializing Profile...\n')
print('-----------------------------------------------------------------')
#SELENIUM ENTRIES
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
cap['acceptInsecureCerts'] = True
binary = FirefoxBinary('/usr/bin/firefox')
##
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--load-images=no')
options.add_argument("window-size=1400,600")
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--proxy-server=%s' % proxy)
##
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "[user-agent string]")
profile.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")


df_proxies=WebShare_Proxies()
args=df_proxies.values[random.choice(df_proxies.index)].tolist()
#
url='https://shareville.se/medlemmar/valuegrowth/wall'

print('Reading infos from\n:',url)

driver = webdriver.Firefox(profile,options = options,capabilities=cap,firefox_binary=binary)
driver.get(url)
time.sleep(10)

target_user='Valuegrowth'


lst2=[]
for elem in driver.find_elements_by_xpath('.//span[@class = "ng-binding ng-scope"]'):
	if 'SEK' in elem.text:
		lst2.append(elem.text)


df=pd.DataFrame(lst2,index=len(lst2)*[target_user],columns=['Activity'])


print(df)


driver.close()
#
#
#
#
#
#
#

