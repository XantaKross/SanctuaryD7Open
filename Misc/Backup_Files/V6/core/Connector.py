"""
This file is essentially Adapt's Connector.
The brain file contains the neccessary code for required intelligence.
This file serves as a connector between the website interface
shown on the client side and the facilities of the server computer.



(This code will run everytime the website recieves a input.
 The aim of this code is to basically boot up the libraries and
 requirements such as pre-defined commands needed to run the adapt.)
"""


#views file needs to be imported and connected with this.
#the varables used from view are:
# dialogue: multiline output;
# command: single line input;

from . import Brain
from ._common import format_line
import time as clock

class connect:
    def __init__(self):
        #the voice is loaded.
        #self.voice = pytx.init()

        #some variables that need to be
        #input_width = 54
        #self.limit = 50

        #default dialogue is set.
        self.dialogue = ['Welcome Master, What can I do for you?',] #initial main_text string list.
        self.brain = Brain.construct()

        #the ui is done setting up and is run.
    #    self.talk()
    
    #parameter cmd (command) will be the input.
    def react(self, cmd):
        time_details = list(clock.ctime(clock.time()).split())
        #get the time details.
        
        self.dialogue = self.brain.interpret(cmd, time_details) #format_line(self.brain.interpret(cmd, time_details)) #is a list with multiple single stings.
        #gets output.

        return self.dialogue

    #    self.talk()


    #function that outputs the sound from the dialogue.
    #def talk(self):
    #    self.voice.startLoop(False)
    #
    #
    #    if len(self.dialogue) == 2 and self.dialogue[1] != []:
    #        txt_lst, formatted_lst = self.dialogue
    #
    #        for item_2, item_1 in zip(txt_lst, formatted_lst):
    #            self.main_txt.configure(text=item_1)
    #            self.main_txt.update()
    #
    #            self.voice.say(item_2)
    #            self.voice.iterate()
            
    #    else:
    #        if len(self.dialogue) == 2:
    #            self.dialogue = self.dialogue[0]
    #
    #        for item in self.dialogue:
    #            self.main_txt.configure(text=item)
    #            self.main_txt.update()
                
    #            self.voice.say(item)
    #            self.voice.iterate()
    #
        
    #    self.voice.endLoop()
        
"""
#Booting Sequence: Complete...
#Application Loop: Start...




(This code will run as long as the application is running in the
 Background. This is the interactive part of the application process.)
"""

