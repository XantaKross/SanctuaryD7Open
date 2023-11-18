def weather_report(day):
    import requests
    from bs4 import BeautifulSoup

    # the day will be today or tomorrow
    query = f'what is the weather {day}'
    url = f"https://www.google.com/search?q={(query.replace(' ', '+'))}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}

    # temperature, sky.
    classes = ['wob_t q8U8x', 'wob_dcp']
    output = ''

    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')

    temperature = str(soup.find('span', class_=classes[0]).text)
    climate = str(soup.find('div', class_=classes[1]).text)

    return (temperature + ' degree celsius ' + climate.lower())


#weather
if 'tomorrow' in cmd:
    text = weather_report('tomorrow')
else:
    text = weather_report('today')
