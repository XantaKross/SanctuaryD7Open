dataset = {
    'movie_stream':
        [
            'lets see',
            'I want to watch',
            'stream',
            'play',
            'show bring give me the links to',
            'where can should i watch',
        ]
}

#common_functions
def pad(str1, str2):
    if len(str1) < len(str2): str1 += '#' * (len(str2) - len(str1))
    else: str2 += '#' * (len(str1) - len(str2))
    return zip(str1, str2)

def common_slice(str1, str2):
    for j, k in pad(str1, str2):
        if j == k: str1 = str1.lstrip(k)
        elif j == '#' or k == '#': break
    return str1

def intersection(lst1, lst2): return [(0) if i not in lst2 else (1) for i in lst1]


def movie_stream(search):
    from selenium import webdriver
    from bs4 import BeautifulSoup

    stream_list = [['https://cmovies.so/movie/search/[SEARCH]', '-', 'ml-mask jtajax'],
                   ['https://watchserieshd.live/search/[SEARCH]', '-', 'film-poster-ahref flw-item-tip'],
                   ['https://vu.movies123.sbs/search/[SEARCH]/', '%2b', 'ml-mask jt']]

    links = {}
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = 1
    browser = webdriver.Firefox(options=fireFoxOptions)

    for link in stream_list:
        website_address = link[0].split('search')[0]
        links[website_address] = []

        url = link[0].replace('[SEARCH]', link[1].join(search.split()))

        browser.get(url)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        search_results = [(common_slice(row['href'], website_address)) for row in soup.find_all('a', {"class":link[2]})
                          if 1 in intersection(common_slice(row['href'], website_address).split('/')[1].split('-'), search.split())]
        if len(search_results) != 0: links[website_address] += search_results

    browser.quit()
    return links


def objective(func, cmd, func_dict):
    if func == 'movie_stream':
        query = func_dict['eliminator'](['lets', 'see', 'want', 'to', 'stream', 'play', 'show', 'bring', 'give', 'me', 'the', 'links', 'to', 'where' 'can', 'should', 'watch',], cmd)
        return movie_stream(query)
