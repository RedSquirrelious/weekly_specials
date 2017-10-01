

def get_tc_specials(bso):
    specials = bso.find("div", {"id": "content"})
    return specials


def get_tc_dates(specials):
    dates = specials.find("h2", {"class": "effective"})
    return dates

def get_tc_market_buys_dates(specials):
    dates = specials.find("div", {"class":"mb_date"})
    return dates.text.strip()

def get_tc_items(specials):
    items = specials.findAll("tr", {"class": "adTextItem"})
    return items


def get_tc_market_buys_items(specials):
    items = specials.findAll("div", {"class": "mb_prod"})
    return items

''' be careful when passing in dictionaries.  Big Board Specials and Biweekly Specials 
have identical ids for different items '''
def parse_tc_specials(ws, items):
    l = 'local'
    o = 'organic'
    for item in items:
        id = item.get("onclick").split(',')[0].split('(')[1]
        deets = item.find("strong")
        name = deets.next
        description = name.next
        price = item.find("td", {"class": "adTextRight"}).text
        ws[id] = {}
        ws[id]['name'] = name.lstrip().rstrip()
        ws[id]['description'] = description.lstrip().rstrip()
        ws[id]['price'] = price.lstrip().rstrip()

        if l in name.lower() or l in description.lower():
            ws[id]['local'] = True
        else:
            ws[id]['local'] = None
        if o in name.lower() or o in description.lower():
            ws[id]['organic'] = True
        else:
            ws[id]['organic'] = False


def parse_tc_market_buys_specials(ws, items):
    l = 'local'
    o = 'organic'
    for item in items:
        id = item.get("data-id")
        name = item.find("div", {"class": "mb_name"})
        description = item.find("div", {"class": "mb_desc"})
        price = item.find("div", {"class": "mb_price"})
        ws[id] = {}
        ws[id]['name'] = name.text

        if description:
            ws[id]['description'] = description.text
        else:
            ws[id]['description'] = None
        ws[id]['price'] = price.text

        if l in name.text.lower():
            ws[id]['local'] = True
        else:
            ws[id]['local'] = None

        if ws[id]['local']:
            pass
        elif ws[id]['description'] and l in ws[id]['description']:
            ws[id]['local'] = True
        else:
            pass

        if o in name.text.lower():
            ws[id]['organic'] = True
        else:
            ws[id]['organic'] = False

        if ws[id]['organic']:
            pass
        elif ws[id]['description'] and o in ws[id]['description']:
            ws[id]['organic'] = True
        else:
            pass