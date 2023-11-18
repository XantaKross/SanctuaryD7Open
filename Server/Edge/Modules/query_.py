dataset = {'search_web':
            [
                'who is the',
                'who discovered',

                'what is a',
                'what for',
                'what is the name of',

                'how to make',
                'how to fix my',
                'how to find the',
                'how to get a job',

                'when was the formed',
                'when were the built',
                'when is',
                'when will end',
                'when are cheap',

                'where is',
                'where will the market go today',
                'where are',
                'where were the',
                'where would',

                'why is the',
                'why will the',
                'why would the',
                'why might'
            
                'can i turn into',
            ],

            'weather_report':
            [
                'what is the weather right now',
                "give me the weather",
                "what's the temperature today",
                'will it rain today or is it gonna be sunny',
                'how is the weather',
                "how's the climate",
                'how hot, cold, warm, cool is it'
            ],

            'wolfram_computation':
            [
                'solve calculate for x, x = 10-90',
                'integrate x^2',
                'find, sin(x) cos(x) tan(x) sec(x) cot(x)',
            ],
}


def search_web(query):
    import requests, re
    from bs4 import BeautifulSoup

    url = f"https://www.google.com/search?q={(query.replace(' ', '+'))}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}

    # 0 and 1 place is locked. don't change list.
    classes = ['Z0LcW', 'uUjm4e', 'kno-rdesc', 'O5uR6d LTKOO', 'hgKELc', 'LGOjhe', 'thODed']  # 'yp1CPe wDYxhc']

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
    import requests
    from bs4 import BeautifulSoup

    # the day will be today or tomorrow
    query = f'what is the weather {day}'
    url = f"https://www.google.com/search?q={(query.replace(' ', '+'))}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}

    # temperature, sky.
    classes = ['wob_t q8U8x', 'wob_dcp']
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')

    temperature = str(soup.find('span', class_=classes[0]).text)
    climate = str(soup.find('div', class_=classes[1]).text)

    return (temperature + ' degree celsius ' + climate.lower())

def getcalc(input):
    import wolframalpha as wolf
    app_id = "A7H284-36L5PQ43H2"
    client = wolf.Client(app_id)
    res = client.query(input)

    abcd = []
    for i in res.results:
        out = i.text.replace('\n', ' ')
        if len(out) > 23: out = (out[:23] + ' ' + out[-19:])
        abcd.append(out)

    return abcd


def wolf_calc(query):
    lst_ = [['degrees', 'degree', 'deg'],
            ['exact', 'ext', 'exct']]
    words = ['solve', 'calculate', 'figure', 'find']

    for item in query.split():
        if item in words: query = query.replace(item, '')

        elif item.isdigit() == True: continue

        elif item in lst_[0]:
            text = getcalc(query)[-1]
            text = (getcalc(f'{text[:-20]} rad to degrees')[-1]).replace('°', '')
            break

        else:
            text = getcalc(query)[0]
            break

    return text



def objective(func, cmd, func_dict):
    if func == 'wolf_computation':
        return wolf_calc(cmd)

    elif func == 'search_web':
        query = func_dict['eliminator'](['find', 'search', 'google'], cmd)
        return search_web(query)

    elif func == 'weather_report':
        # weather
        if 'tomorrow' in cmd: return weather_report('tomorrow')
        else: return weather_report('today')
