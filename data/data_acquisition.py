from bs4 import BeautifulSoup
import os
import pickle
from selenium import webdriver
from .metropolitan_market import *
from .town_and_country_central_market import *


def make_browser(driver_file):
    browser = webdriver.Chrome(driver_file)
    return browser


def resolve_url(domain_url, search_url, secure_protocol=False):
    if secure_protocol:
        protocol = "https://"
    else:
        protocol = "http://"
    full_url = "{}{}{}".format(protocol, domain_url, search_url)
    return full_url


def resolve_file_path(folder, file):
    path = os.path.join(os.path.dirname(os.getcwd()), folder, file)
    return path


def store_initial_cookies(browser, url, file):
    browser.get(url)
    pickle.dump( browser.get_cookies() , open(file,"wb"))


def retrieve_cookies(file):
    cookies = pickle.load(open(file, "rb"))
    return cookies


def add_cookies(browser, cookies):
    for cookie in cookies:
        browser.add_cookie(cookie)


def get_site_html(browser, url):
    browser.get(url)
    html = browser.execute_script("return document.body.innerHTML")
    return html


def make_soup(html, soup_format):
    bs = BeautifulSoup(html, soup_format)
    return bs


