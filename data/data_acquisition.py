from bs4 import BeautifulSoup
import os
import pickle
from selenium import webdriver
import constants



def make_browser(driver_file):
    browser = webdriver.Chrome(driver_file)
    return browser


def store_cookies(browser, url, file):
    browser.get(url)
    pickle.dump( browser.get_cookies() , open(file,"wb"))


def get_cookies(file):
    cookies = pickle.load(open(file, "rb"))
    return cookies


def get_site_innerhtml(browser, url, cookies):
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get(url)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    return innerHTML


def make_soup(innerHTML, soup_format):
    bs = BeautifulSoup(innerHTML, soup_format)
    return bs


def get_specials(bso):
    specials = bso.find("div", {"id": "specialsContent"})
    return specials


def get_dates(specials):
    dates = specials.find("div", {"class": "specials_dates"})
    return dates

def get_items(specials):
    items = specials.findAll("div", {"class": "item_view"})
    return items


def parse_specials_to_dict(items):
    ws = {}
    l = 'local'
    o = 'organic'
    for item in items:
        id = item.get("id")
        price = item.find("strong", {"class": "price"})
        sm = item.findAll("small")
        brand = sm[0].text
    #     description = sm[1].text
        deets = item.find("h4")
        name = ''.join(deets.find('br').next_siblings).strip()
        ws[id] = {}
        ws[id]['name'] = name
        ws[id]['price'] = price.text
    #     ws[id]['description'] = description
        if l in brand or l.upper() in brand:
            ws[id]['local'] = True
            ws[id]['brand'] = brand[6:]
        else:
            ws[id]['local'] = False
            ws[id]['brand'] = brand
        if o in brand or o.upper() in brand or o in name or o.upper() in name or o in name.lower():
            ws[id]['organic'] = True
        else:
            ws[id]['organic'] = False
    return ws

#
# b = make_browser(DRIVER_FILE)
# store_cookies(b, mm_url, mm_cookies_file)
# cookies = get_cookies(mm_cookies_file)
# innerHTML = get_site_innerhtml(b, mm_url, cookies)
# bso = make_soup(innerHTML, SOUP_FORMAT)
# weekly_specials = get_specials(bso)
# items = get_items(weekly_specials)
# ws = parse_specials_to_dict(items)
#
# print(ws)
# print(len(ws))
#
#
# dates = weekly_specials.find("div", {"class": "specials_dates"})
# print(dates.text.strip())
#
#
#
#
#
