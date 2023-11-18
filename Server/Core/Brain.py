"""
Essentially darwin's brain. Aka where it processes input from the user and decides it's next action.
"""

from Server.Core._common import compress, find_func, Bubble, purify, check_run

#The probablity/context filter for darwin V7 or DV7
#This class creates the filter.
class Brain():
    def __init__(self, data):
        self.data = data
        self.sub_nodes = {}

    def add_data(self, data_point, file):
        self.data = {**self.data, **data_point}
        self.format_data(file) #format data each time new data is added.

    def run(self, cmd): return find_func(self.parse(purify(cmd)))

    def format_data(self, file):
        self.bubble = Bubble() # bubble object the word-function formatted data.
        # 1) {'words': 'respective_key_1', 'words': 'respective_key_2', ...}

        for function, sentences in self.data.items():
            #storing the function into memory from dataset to use them whenever needed.
            if function not in self.sub_nodes.keys(): self.sub_nodes[function] = file

            #creating the word-function classifier.
            for row in sentences:
                addenum = purify(row).split()

                for word in addenum:
                    if word.isalpha():
                        if word not in self.bubble.keys:
                            self.bubble.add(word, [function])

                        else:
                            idx = self.bubble.retrieve(word, tag=1)
                            if function not in self.bubble.values[idx]: self.bubble.values[idx] += [function]


    #This function needs rewriting.

    def parse(self, command):
        # first create a checklist. with keys being the unique values
        checklist = {(i): (0) for i in compress(self.bubble.values)}
        cmds = command.split()

        uncertainity = 0 # when the algorithm attains a higher uncertainity it will search it online.
        last_idx = 0 # distance between the last index where uncertainity was met vs now.

        for word_idx in range(len(cmds)): # for each command.
            functions_bound_to_word = compress(self.bubble.retrieve(cmds[word_idx]))
            #print(5, functions_bound_to_word)

            if functions_bound_to_word == []:
                weight = (word_idx-last_idx+1)*(cmds[word_idx] not in self.bubble.keys) + 1*(cmds[word_idx] in self.bubble.keys)
                uncertainity += (1/len(cmds))*weight
                checklist['search_web'] += uncertainity
                checklist['wolfram_computation'] += uncertainity
                checklist['movie_stream'] += uncertainity
                last_idx = (word_idx)*(cmds[word_idx] not in self.bubble.keys)

            #the function needs to loop in on itself to save time space of O^2. Needs rewriting.

            for function in functions_bound_to_word:
                checklist[function] += (1/len(functions_bound_to_word))

        return checklist

    def interpret(self, cmd, time_details):
        # example: action --> ['what are you doing today?', '1.0']

        temp = self.parse(purify(cmd))
        output = compress(find_func(temp))

        if len(output) == 1: extract_cmd = output[0] #the first item.
        else: return "Command not found Master. Try being more descriptive."

        print(0, cmd, extract_cmd, '\n\n')

        text = check_run(self.sub_nodes[extract_cmd], extract_cmd, cmd, time_details)

        return text
