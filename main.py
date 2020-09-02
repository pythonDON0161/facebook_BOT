from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait

from fake_useragent import UserAgent

import time
from time import sleep

import random

import pandas as pd

df = pd.read_csv(r"names.csv", engine='python', sep=',')
data = df.values.tolist()  # convert dataframe to list


# print(data[7])


# sleep(5000)


def main():

    EMAIL = "sushioguapo0161@gmail.com"
    PASSWORD = "Shelbert15"
    ua = UserAgent()
    ua.random  # use a random user agent

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("user-agent=ua")

    # create a new CHROME session
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # Navigate to the application home page
    driver.get("http://www.facebook.com")

    # email_input
    email_input = driver.find_element_by_id("email")  # .send_keys(EMAIL)
    for char in EMAIL:
        email_input.send_keys(char)
    # time between each character being entered
    time.sleep(random.randrange(3, 6))

    password_input = driver.find_element_by_id("pass")
    for char in PASSWORD:
        password_input.send_keys(char)
    # time between each character being entered
    time.sleep(random.randrange(3, 6))

    login_btn = driver.find_element_by_name("login").click()

    search_input = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input")

    # search_button = driver.find_element_by_xpath(
    # "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[9]/div/a")
    y = 19
    for i in data:
        username = data[y]
        y = y+1
        for char in username:
            try:
                search_input.send_keys(char)
                time.sleep(2)
                search_input.send_keys(Keys.ENTER)
                time.sleep(2)
                add_friend = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[3]/span/div")
                add_friend.click()
                time.sleep(1)
                search_input.send_keys(Keys.CONTROL + "a")
                search_input.send_keys(Keys.DELETE)
            except:
                print("error with" + username)
                break

        # click search button

    WebDriverWait()


main()
