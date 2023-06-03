from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse
from flask import Flask,jsonify, request
from flask_restful import Api, Resource
import time


app = Flask(__name__)
api = Api(app)

PATH = ".chromedriver.exe"


def get_first_image_url_from_google(delay, search_term):
    wd = webdriver.Chrome(PATH)
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = f"https://www.google.com/search?q={urllib.parse.quote(search_term)}&tbm=isch"
    wd.get(url)

    scroll_down(wd)

    thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

    if len(thumbnails) > 0:
        try:
            thumbnails[0].click()
            time.sleep(delay)
        except:
            pass

        images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
        if len(images) > 0 and images[0].get_attribute('src') and 'http' in images[0].get_attribute('src'):
            return images[0].get_attribute('src')
    wd.quit()
    return None



