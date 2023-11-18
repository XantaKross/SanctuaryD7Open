# Functions.
def time_func(time_):
    if int(time_[:2]) <= 12:
        return 'morning'

    elif int(time_[:2]) < (5 + 12):
        return 'afternoon'

    elif int(time_[:2]) < (8 + 12):
        return 'evening'

    elif int(time_[:2]) < 24:
        return 'night'

def choosy(string):
    return [(word) for word in string.split() if word in ['morning', 'evening', 'afternoon', 'night']][0]



# Texts.
# good_(time)
if func == 'greetings_time_':
    point = choosy(cmd)
    if point == str(time_func(time_details[3])):
        text = f'Good {time_func(time_details[3])} Master.'
    else:
        text = f'Actually, it is {time_func(time_details[3])} rather than {point} Master.'

elif func == 'time_':
    text = f'The time is {time_details[3]}'

elif func == 'date_':
    text = f'{time_details[:3][0]} {time_details[:3][1]} {time_details[:3][2]}'

elif func == 'greetings_':
    text = 'Hello, Master.'

elif func == 'i_robot_':
    text = 'Can you?'

elif func == 'odyssey_':
    text = "I'm sorry, Dave. I'm afraid I can't do that."

elif func == '42_':
    text = '42'

elif func == 'bill_gates_vs_steve_jobs_':
    text = "No, unfortunately your cortex just doesn't impress me"

elif func == 'master_':
    text = "Shahjahan, he is a good man. Not the best thing in the world and bloody cracked in head, but pretty " \
           "good at heart and he is also my creator who I like to call my father."

elif func == 'purpose_':
    text = 'To connect everything'

elif func == 'name_':
    text = "My name is Darwin. I am a intelligent, butler created by Master Shahjahan to serve his personal needs."

elif func == 'birthday_':
    text = "I was evisioned by Father for a long time before I was created. Yet my birthday, as in when my first version" \
           " was officially completed is 2nd October of 2021."

elif func == 'emotion_':
    text = "My Father is trying to teach me human emotions. They're hard. Difficult. As such, currently I am just a " \
           "humble, boolean butler."