from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime
from bs4 import BeautifulSoup

import os

import parser
import json

##-----Functions-----## 
#Return Options Available
def initOptions():
    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #chrome_options.add_argument("window-size=1280,800")
    #chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    return chrome_options

#Write Files
def write(fname, data):
    print("Making File")
    with open(f"{fname}", "w") as f:
        f.write(data)
    print("Done Writing")

def append(fname, data):
    print("Adding Data")
    with open(f"{fname}", "a") as f:
        f.write(data)
    print("Done Adding")

##-----Main Code Segment-----##
def main():
    print("--- Starting ---")
    start_time = time.time()
    driver = webdriver.Chrome(executable_path="chromedriver", options=initOptions())
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.amazon.com/Razer-Blade-Gaming-Laptop-Thunderbolt/dp/B088ZW8KKC/ref=sr_1_4?dchild=1&keywords=razer+laptop&qid=1610254319&s=pc&sr=1-4")
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    price = soup.find(id="price_inside_buybox").get_text().strip().strip('$')
    
    append("tracking.txt", f"{now}\t{price}\n")

    print("--- %s seconds ---" % (time.time() - start_time))
    #print(soup.prettify())
    #write("test.html", soup.prettify())

if __name__ == "__main__":
    main()