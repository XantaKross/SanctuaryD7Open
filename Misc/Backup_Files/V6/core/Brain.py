"""
Essentially darwin's brain. Aka where it processes input from the user and decides it's next action.

"""

from ._common import Node, fast_fltr
from . import Remote, Root

#from gensim.test.utils import simple_preprocess


class construct:
    def __init__(self):
##########################################################################################################################################################################################
        #create the first and main part of the tree. this will the branch out and become more and more complex and intricate with each added node.
        self.tree = Node('-main-', [], "")
##########################################################################################################################################################################################

        
        
        
        #the first branches. or primary branches of darwin.
        #the secondary branches, corresponding to the primary branches.
        #tertiary branches, correspoding to secondary branches.
        
        
#############################################################################################
        self.tree.add_node('system_control', [], "")
#############################################################################################
        self.tree.add_node('run_apps', ['/p', 'open', 'run', 'start',],  
"""
#now i know what the command is, im using that to find the object to use the command on
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
""",'system_control')
#############################################################################################
#        self.tree.add_node('power_mode', ['sleep'],  
#"""
#""",'system_control')
##############################################################################################
#NOTE: doing advance system control using darwin, when it is in it's initial state could be dangerous.
#so im not gonna implement this process right now. I will do it when i have a better filtering system.
        
        
        
        
        
        
        
#############################################################################################        
        self.tree.add_node('online', [], "")
#############################################################################################        
        self.tree.add_node('query', ['/s', 'search', 'look', 'find', 'google', 'who', 'what', 'how', 'when'],
"""
query = cmd.replace(fltr_cmd, '')
text = Remote.search_web(query)
""",'online')
#############################################################################################
        self.tree.add_node('weather', ['weather', 'climate', 'today', 'tomorrow'], 
"""
if 'tomorrow' in cmd:
    text = Remote.weather_report('tomorrow')
else:
    text = Remote.weather_report('today')
""",'online')
##############################################################################################        
        self.tree.add_node('wolfram_oomputation', ['/q', 'calc', 'calculate', 'compute', 'solve', '=', '+', '-', '//',
                                                   '*'],
"""
def func(query):

    lst_ = [['degrees', 'degree', 'deg'],
            ['exact', 'ext', 'exct']]
    
    text = ''
    for item in query.split():
        if item.isdigit() == True:
            continue
            
        elif item in lst_[0]:
            query = (query.replace(item, ''))
            text = Remote.wcalc(query)[-1]
            text = (Remote.wcalc(f'{text[:-20]} rad to degrees')[-1]).replace('°', '')
            
        elif item in lst_[1]:
            query = query.replace(item, '')
            text = Remote.wcalc(query)[0]
            
    if text == '':
        text = Remote.wcalc(query)[-1][:10]
        
            
    
    return text

text = func(cmd.replace(fltr_cmd, ''))
""",'online')
#############################################################################################
####self.tree.add_node('music':['play', 'song', 'music']])









#############################################################################################        
        self.tree.add_node('time_date+', [], "")
#############################################################################################
        self.tree.add_node('clock', ['what is the time', 'tell me the time', 'tell me the hour', 'how late is it'],
"""
text = f'The {fltr_cmd} is, {time_details[3]}'
""", 'time_date+')
#############################################################################################
        self.tree.add_node('date', ['what is the date', 'what day is it'],
"""
text = (" ").join(time_details[:3])
text = text[:3] + 'day' + text[3:]
""", 'time_date+')
#############################################################################################
        self.tree.add_node('set_watch', ['stopwatch', 'alarm'], 
"""
text = 'UNCONFIGURED'
""", 'time_date+')
#############################################################################################
        
        
        
        
        
        
        
        
        
#############################################################################################        
        self.tree.add_node('random_number', [], "")
#############################################################################################
        self.tree.add_node('generate', ['generate', 'random', 'number'], 
"""
text = str(randint(-100000, 100000))
""", 'random_number')
#############################################################################################        










#############################################################################################
        self.tree.add_node('you', [], "")
#############################################################################################
        self.tree.add_node('purpose', ['what is your purpose', 'what is your aim', 'tell me about your mission',
                                       'what exactly is your goal'],
"""
text = "To connect everything."
""",'you')
#############################################################################################
        self.tree.add_node('name', ['what is your name', 'give me a intro', 'introduce yourself'],
"""
text = "My name is Darwin. I am a intelligent, butler created by Master Shahjahan to serve his personal needs."
""", 'you')
#############################################################################################
        self.tree.add_node("birthday", ["what's your birthday", "when were you created", 'when were you born'],
"""
text = "I was evisioned by Father for a long time before I was created. Yet my birthday, as in when my first version was 
        officially completed is 2nd October of 2021."
""", 'you')
#############################################################################################
        self.tree.add_node('emotion', ['what is your personality', 'do you have emotions', 'do you understand feelings',
                                       'tell me about your feelings'],
"""
text = "My Father is trying to teach me human emotions. They're hard. Difficult. As such, currently I am just a humble, 
        boolean butler."
""", 'you')
#############################################################################################









#############################################################################################
        self.tree.add_node('general_talk', [], "")
#############################################################################################
        self.tree.add_node('good_', ['morning', 'evening', 'night', 'afternoon'],
"""
if fltr_cmd == str(Root.time_func(time_details[3])):
    text = f'Good {Root.time_func(time_details[3])} Master.'
else:
    text = f'Actually, it is {Root.time_func(time_details[3])} rather than {fltr_cmd} Master.'
""",'general_talk')
#############################################################################################
        self.tree.add_node('human', ['human', 'alive'],
"""
text = 'No. Unfortunately, your cortex just doesn't impress me.'
""",'general_talk')
#############################################################################################
        self.tree.add_node('greetings', ['hi', 'hello',],
"""
text = 'Hello, Master.'
""",'general_talk')
#############################################################################################

        
        
        
        
        
        
        
#############################################################################################
        self.tree.add_node('pop_references', [], "")
#############################################################################################
        self.tree.add_node('i_robot', ['canvas', 'symphony', 'masterpiece'],
"""
text = "Can you?"
""", 'pop_references')
#############################################################################################
        self.tree.add_node('oddesy', ['pod', 'bay', 'hal'],
"""
text = "I'm sorry, Dave. I'm afraid I can't do that."
""", 'pop_references')
#############################################################################################
        self.tree.add_node('42', ['meaning', 'universe', 'ultimate', 'question', 'answer', 'life', 'everything'],
"""
text = "42"
""", 'pop_references')
#############################################################################################









#############################################################################################
        self.tree.add_node('people', [], '')
#############################################################################################
        self.tree.add_node('Master', ['maker', 'creator', 'master', 'father', 'shahjahan', 'xanta'],
"""
text = "A good man. Not the best thing in the world and bloody cracked in head, but pretty good at heart. 
        And he is also my creator who I like to call my father."
""", 'general_talk')
#############################################################################################
        self.tree.add_node('mom', ['yasmin'],
"""
text = "She is my grandmother. And the mother of my creator. She is a strong and hardworking woman who likes tea a lot. She may be difficult sometimes but is generally very homely."
""", 'people')
#############################################################################################
        self.tree.add_node('brother', ['shae'],
"""
text = "My uncle and thus, the brother of father. He is a very cool-headed uncle. One of the nicest person I can think of."
""", 'people')
#############################################################################################
        
        
        
        
        
        
        
        
#############################################################################################        
        self.tree.add_node('quit', [], "")
#############################################################################################
        self.tree.add_node('none', ['quit', 'exit', 'close'], 
"""
text = f"NULL:{Root.time_func(time_details[3][:2])}."
""", 'quit')
#############################################################################################
        
        
        
        
        
        self.fltr = fast_fltr(dataset=self.tree.temp)
    
        
    def interpret(self, cmd, time_details):
        #example: action --> ['good morning', '1.0']
        #indecision action. when darwin is not sure of the input.
        #cmd--> user input, [0] [-3]
        #fltr_cmd-->filtered command, [1] [-2]
        #conf-->confidence in filteration [2] [-1]
        
        output = self.fltr.extract(cmd)
        if output != None:
            conf, fltr_cmd, relative_cmd = output
        else:
            return "Command not found Master."
        
        print(conf, relative_cmd, fltr_cmd, cmd, '\n\n')
        
        total_dict = locals()
        total_dict.update(globals())
        action_dict = self.tree.check_run(relative_cmd, fltr_cmd, total_dict)
        
        #reactions
        #if conf <= 0.5 or action_dict == None:
        #    text = 'Pardon?'
        if action_dict == {}:
            text = """Forgive me for my impotence, Master.
                But I'm not yet configured for the required task."""
        else:
            text = action_dict['text']

            
        return text
        
        
def er_1():
    msg = 'unconfigured'.upper()
    print(msg)
    return msg
        
