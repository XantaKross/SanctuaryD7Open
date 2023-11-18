"""
Darwin's remote. Where it contains all the classes and functions that make change or affect or have a relation, when given the command to the internet or other external devices.
"""

from . import _common
import wolframalpha as wolf
import requests
from bs4 import BeautifulSoup

def search_web(query):
    url = f"https://www.google.com/search?q={(query.replace(' ', '+'))}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    
    #0 and 1 place is locked. don't change list.
    classes = ['Z0LcW', 'uUjm4e', 'kno-rdesc', 'O5uR6d LTKOO', 'hgKELc', 'LGOjhe', 'thODed']#'yp1CPe wDYxhc']

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    
    for item in classes:
        result = (soup.find('div', class_=item))
        
        if result != None:            
            if item == classes[0]:
                out = (result.extract()).text
                
            elif item == classes[1]:
                out = re.sub(r"(\w)([A-Z])", r"\1 \2", f"{result.span.text}")
            
            elif item == classes[2]:
                out = re.sub(r"(\n)( :)", r" \1\2", f"{(result.extract()).text}")
                out = re.sub(r"(\w)([A-Z])", r"\1 \2", f"{out}")
            
            elif item == classes[3]:
                out = result.text
                
            else:
                out = result.span.text
            break
        
        
    if result == None:
        return "Search not found, Master. I'd suggest you to modify your query."
    else:
        return out.replace('Description ', '', 1)
        


def weather_report(day):
    #the day will be today or tomorrow
    query = f'what is the weather {day}'
    url = f"https://www.google.com/search?q={(query.replace(' ', '+'))}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    
    #temperature, sky.
    classes = ['wob_t q8U8x', 'wob_dcp']
    output = ''

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    
    temperature = str(soup.find('span', class_=classes[0]).text)
    climate = str(soup.find('div', class_=classes[1]).text)
    
    return (temperature + ' degree celsius ' + climate.lower())
    
    

def wcalc(input):
    app_id = "A7H284-36L5PQ43H2"
    client = wolf.Client(app_id)
    res = client.query(input)

    abcd = []
    for i in res.results:
        out = i.text.replace('\n', ' ')
            
        if len(out) > 23:
            print(out)
            out = (out[:23] + ' ' + out[-19:])

        abcd.append(out)
        
    return abcd
    
    