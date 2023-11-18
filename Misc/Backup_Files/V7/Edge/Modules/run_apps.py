# is not working because of new filter.
def run_apps(query):
    address = r'C:\Users\Pranav\Desktop\Programs'
    programs = list(listdir(address))

    results = []
    for idx in range(len(programs)):
        results.append([_common.word_sim(query, programs[idx]), programs[idx], idx])
        # conf, fltrd_command, index

    best_result = max(results)
    app_name = programs[best_result[2]]

    u = f'{address}\\{app_name.lower()}'

    if len(best_result) != 0 or best_result[0] > 0.5:
        webb.open(u)

    return [best_result[0], app_name.replace('.lnk', '')]


# now i know what the command is, im using that to find the object to use the command on
app_name = cmd.split(' ').copy()
app_name.remove(fltr_cmd)

if len(app_name) > 1:
    app_name = ' '.join(app_name)

else:
    app_name = str(app_name[0])

op = Root.run_apps(app_name)
if op[0] == 0:
    text = 'No such program detected.'
else:
    text = f'{fltr_cmd}ing {op[1]}'