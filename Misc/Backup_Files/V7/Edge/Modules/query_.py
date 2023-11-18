#online texts
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

def eliminator(list, string):
    for i in list: string = string.replace(i, '')
    return string

def imager(query):

#query-search
query = eliminator(['find', 'search', 'google'], cmd)
print(3, query)
text, img = search_web(query)
img =
print(4, text)
