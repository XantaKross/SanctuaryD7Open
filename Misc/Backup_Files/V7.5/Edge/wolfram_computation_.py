#saving the defined function.
#local_dict['wolf_calc'] = wolf_calc()

# wolfram_calculations
def func(query, wolf_calc):
    lst_ = [['degrees', 'degree', 'deg'],
            ['exact', 'ext', 'exct']]
    words = ['solve', 'calculate', 'figure', 'find']

    for item in query.split():
        if item in words:
            query = query.replace(item, '')

        elif item.isdigit() == True:
            continue

        elif item in lst_[0]:
            #query = (query.replace(item, ''))
            text = wolf_calc(query)[-1]
            text = (wolf_calc(f'{text[:-20]} rad to degrees')[-1]).replace('°', '')
            break

        else:
            #query = query.replace(item, '')
            print()
            print(3, query)
            text = wolf_calc(query)[0]
            print(4, text)
            break

    return text

def wolf_calc(input):
    import wolframalpha as wolf

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




text = func(cmd, wolf_calc)
