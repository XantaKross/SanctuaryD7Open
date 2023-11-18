"""
This file is essentially Adapt/Darwin's Connector.
The brain file contains the neccessary code for intialization of intelligence/ further interpretation.
This file serves as a connector between the website interface
shown on the client side and the facilities of the server computer.



(This code will run everytime the website recieves a input.
 The aim of this code is to basically boot up the libraries and
 requirements such as pre-defined commands needed to run the adapt/darwin.)
"""

#REMOVE PYTTSX AND REPLACE IT WITH ESPEAK


#views file needs to be imported and connected with this.
#the varables used from view are:
# dialogue: multiline output;
# command: single line input;

from Core.Brain import Brain
from Edge.Databases.iodata import command_set
import time as clock
import subprocess as subp
import re, os
from tabulate import tabulate

#This class connects the constructed tree to the web ui interface.
class connect:
    def __init__(self):
        #default dialogue is set.
        self.dialogue = ['Welcome Master, What can I do for you?',] #initial main_text string list.
        self.brain = Brain(command_set)

    #parameter cmd (command) will be the input.
    def react(self, cmd):
        #get the time details.
        time_details = list(clock.ctime(clock.time()).split())

        #gets output.
        self.dialogue = self.brain.interpret(cmd, time_details)

        redunt_chr = re.compile("[^a-zA-Z]") # naming of the audio file in order to save it/which is also connected to the subtitle shown to client
        if isinstance(self.dialogue, dict):  sentence = redunt_chr.sub('', str(list(self.dialogue.values()))[1:11].replace('/', '_')) + '.mp3'
        else:  sentence = redunt_chr.sub('', self.dialogue[0:10].replace(' ', '_')) + '.mp3'

        location_of_cache = f"Edge/Cache/Audio_files/{sentence}"
        audio_addr = str(__file__).replace('Core/Connector.py', location_of_cache)

        audio_files = os.listdir(audio_addr.replace(sentence, ''))


        if sentence not in audio_files: # Create the tabulation filtered file if it doesn't exist. otherwise pass.
            if isinstance(self.dialogue, dict):
                subp.run(['espeak', '-v', 'mb-en1', '-s', '120',
                          f'Here are the results for "{cmd}"', '-w', audio_addr],
                         check=True)
            else: # Create the file if it doesn't exist. otherwise pass.
                subp.run(['espeak', '-v', 'mb-en1', '-s', '120', self.dialogue, '-w', audio_addr],
                         check=True)

        #print(2, self.dialogue, [audio_addr, sentence])
        return self.dialogue, [audio_addr, sentence]


"""
#Booting Sequence: Complete...
#Application Loop: Start...




(This code will run as long as the application is running in the
 Background. This is the interactive part of the application process.)
"""

