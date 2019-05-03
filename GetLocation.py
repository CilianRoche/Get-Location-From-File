import pandas as pd
import codecs

def clean_location():
    i = codecs.open('path/to/output.txt', encoding='UTF-16')
    distinguished = []
    for x in i.readlines():
        if x.startswith('Distinguished'):
            distinguished.append(x)

    page = [x[44:] for x in distinguished]
    locations = [x.replace('\r', '').replace('Family Care Network', '').replace(',', '').replace('OU', '').replace('CN', '').replace('DC', '').replace('=', '').replace('Family Care Network', '').replace('Computers', '').replace('net', '').replace('fcn', '').replace('\n', '') for x in page]
    return locations

def clean_names():
    i = codecs.open('path/to.output.txt', encoding='UTF-16')
    names = []
    for x in i.readlines():
        if x.startswith('Name'):
            names.append(x)
    page = [x[20:] for x in names]
    finalName = [x.replace('\r', '').replace('Name', '').replace('\n', '') for x in page]
    return finalName

def output():
    locations = clean_location()
    names = clean_names()
    df = pd.DataFrame({'Name':names, 'Location': locations})
    df.to_csv('path/to.csv', index=False)

output()
