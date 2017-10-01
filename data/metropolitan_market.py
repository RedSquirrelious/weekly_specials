


def get_mm_specials(bso):
    specials = bso.find("div", {"id": "specialsContent"})
    return specials


def get_mm_dates(specials):
    dates = specials.find("div", {"class": "specials_dates"})
    return dates

def get_mm_items(specials):
    items = specials.findAll("div", {"class": "item_view"})
    return items



def parse_mm_specials(ws, items):
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
