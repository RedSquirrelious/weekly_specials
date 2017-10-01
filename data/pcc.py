def get_pcc_specials(bso):
    specials = bso.find("div", {"class": "pcc-weekly-specials-template"})
    return specials


def get_pcc_date(specials):
    date_statement = specials.find("h2").text
    return date_statement


def parse_pcc_date_statement(date_statement):
    a = date_statement.split('.')
    b = a[0].split(' ')
    c = []
    for item in b:
        if item[0].isdigit():
            c.append(item)
        elif item.lower() == 'to' or item.lower() == 'through' or item.lower() == '-':
            c.append('_')
        else:
            pass
    date = ''.join(c)
    return date


def get_pcc_items(specials):
    items = specials.findAll("div", {"class": "card"})
    return items


def parse_pcc_specials(ws, items, sale_dates):
    count = 0
    l = 'local'
    o = 'organic'
    for item in items:
        id = '{}_{}'.format(sale_dates, count)
        brand = item.find("div", {"class": "pcc-weekly-special-label"})
        name = item.find("h5", {"class": "pcc-weekly-special-headline"})
        prices = item.findAll("p", {"class": "pcc-weekly-special-price"})
        price = prices[0].find("strong").text
        ws[id] = {}
        ws[id]['name'] = name.text
        ws[id]['brand'] = brand.text
        ws[id]['price'] = price

        if l in name.text.lower() or l in brand.text.lower():
            ws[id]['local'] = True
        else:
            ws[id]['local'] = None

        if o in name.text.lower() or o in brand.text.lower():
            ws[id]['organic'] = True
        else:
            ws[id]['organic'] = False
        count += 1