# Each file will contain a dataset as well as certain functions.

dataset = {
    'time_':
        [
            'what is the time?',
            'tell me the time',
            'what is the hour?',
            'how late is it?',
            'what was the time again'
        ],

    'date_':
        [
            'give me the date',
            'what day is today, is it  again',
            'was is it a sunday, monday, tuesday, wednesday, thursday, friday, saturday',
        ],

    'greetings_time_':
        [
            'good morning, evening, night, afternoon',
            'good day, night'
        ],

    'greetings_':
        [
            'hi, hello, yo, hey there',
        ],

    'i_robot_':
        [
            'Can a robot write a symphony?',
            'Can a robot turn a canvas into a beautiful masterpiece?',
        ],

    'odyssey_':
        [
            'open the pod bay doors please hal',
            'Hal, I won’t argue with you anymore. Open the doors',
        ],

    '42_':
        [
            'what is the meaning of life the universe and everything',
        ],

    'bill_gates_vs_steve_jobs_':
        [
            'do you want to be human, alive, real, body',
        ],

    'master_':
        [
            'who is your father, creator, maker, master',
            'who is xanta, shahjahan',
            'who created, made you, name of',
        ],

    'grandma_':
        [
            'who is yasmin',
            'who is your grandmother, grandma',
        ],

    'uncle_':
        [
            'who is shae, khan',
            'who is your uncle',
        ],

    'purpose_':
        [
            'what is your goal, purpose, aim',
            'why were you created for',
            'why do you exist',
            'what is your use',
            'what accomplishment'
        ],

    'name_':
        [
            'who are you',
            'what is your name',
            'give me a intro',
            'introduce yourself',
            'what are you called',
            'what do you call yourself?',
            'what are you named?'
        ],

    'birthday_':
        [
            "what's your birthday",
            "when were you created",
            'when were you born'
        ],

    'emotion_':
        [
            'what is your personality',
            'do you have emotions',
            'do you understand feelings',
            'tell me about your feelings',
            'include, contain, exist'
        ], }



# Functions.
def time_func(time_):
    hour = int(time_[3][:2])
    if hour <= 12: return 'morning'
    elif hour < (5 + 12): return 'afternoon'
    elif hour < (8 + 12): return 'evening'
    elif hour < 24: return 'night'

def choosy(string): return [(word) for word in string.split() if word in ['morning', 'evening', 'afternoon', 'night']][0]



def objective(func, cmd, func_dict):
    # Texts.
    # good_(time)
    if func == 'greetings_time_':
        point = choosy(cmd)
        if point == str(time_func(func_dict['time_details'][3])):
            text = f"Good {time_func(func_dict['time_details'])} Master."
        else:
            text = f"Actually, it is {time_func(func_dict['time_details'])} rather than {point} Master."

    elif func == 'time_':
        text = f"The time is {func_dict['time_details'][3]}"

    elif func == 'date_':
        text = f"{func_dict['time_details'][:3][0]} {func_dict['time_details'][:3][1]} {func_dict['time_details'][:3][2]}"

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
        text = "Shahjahan, he is a good man. Not the best thing in the world and bloody cracked in head but pretty " \
               "good at heart and he is also my creator who I like to call my father."

    elif func == 'grandma_':
        text = "My grandmother yasmin. The mother of my creator. She is a strong and hardworking woman who likes tea a lot." \
               " She may be difficult sometimes but is generally very homely."

    elif func == 'uncle_':
        text = "My uncle and thus, the brother of my father. He is a very cool-headed uncle. One of the nicest person I can" \
               " think of."

    elif func == 'purpose_':
        text = 'To connect everything'

    elif func == 'name_':
        text = "My name is Darwin. I am a intelligent butler created by Master Shahjahan to serve his personal needs."

    elif func == 'birthday_':
        text = "I was evisioned by Father for a long time before I was created. Yet my birthday, as in when my first version" \
               " was officially completed is 2nd October of 2021."

    elif func == 'emotion_':
        text = "My Father is trying to teach me human emotions. They're hard. Difficult. As such, currently I am just a " \
               "humble, boolean butler."

    return text