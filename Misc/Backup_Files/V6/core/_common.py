"""
Darwin's common. Where it contains all the classes and functions that are require by Darwin and its sub-files.
"""
from gensim.models import FastText


#filter class that creates a similarity score based on the letters of the word
#or by using a ml algorithm.
class fast_fltr:
    def __init__(self, dataset):
        self.dataset = dataset
        self.model = FastText(vector_size=20, window=3, min_count=1)  # instantiate
        self.model.build_vocab(dataset)
        self.model.train(dataset, total_examples=len(dataset), epochs=50)

        
    def extract(self, sentence):
        score = []
        for row in self.dataset:
            for item_1 in row:
                score.append([self.model.wv.similarity(sentence, item_1).sum(), item_1, row[0]])
        
        scored = sorted(score)

        print(sentence, scored)
        for item_4 in scored:
            if item_4[1] in sentence:
                item_4[0] = 1 - item_4[0]
                return item_4
                
        return None

    
    
"""
This is the node class.
The literally the neuron of darwin's brain. This is a tree-like object that has heirarchial nodes inside of it which detects and reacts to the valid commands
by running already-encoded actions/functions.

Current Version: V2
"""
class Node:
    def __init__(self, name, values=[], action='', parent=None):
        self.parent = parent #parent of the node.
        
        self.key = name #name of the node.
        self.temp = []  #This is a temporary list object. That will be deleted as soon as the filter object is built.
                        #in order to save ram.
        
        self.public_keys = [name] #list of names of all the subsequent sub_nodes.
        self.public_values = list(values)       #values corresponding to all the subsequent children nodes and it's own values.
                                                #the node check if the value then exists in here. if found will then check in
                                                #private values. if not found in private values will move down a level and 
                                                #check it's children values.
                                                #this will keep on changing and increasing as more sub_nodes are added.
                                                #                        public_values >= private_values
                                    
        self.private_values = list(values) #values corresponding to the node. the node will react if the value is detected here.
                                           #this shouldn't change whatever happens.

        self.func_ = action #function of the node.
        self.sub_nodes = [] # the node's children.
                        
    def add_node(self, name, values, mlt_str, parent_node=None):
        if parent_node != None:
            object = self.from_key(parent_node) #find the parent node.
            if object == None:
                print('The given parent node is not found.')
            else:
                object[1].add_node(name, values, mlt_str, parent_node=None) #considering this object as the main node, add a new node.
        
        else:
            self.sub_nodes.append([name, Node(name, values, mlt_str, self)]) 
            #add node to the list of nodes that already exists.
            #save the string to perform the instructions later when needed.
            #the object where the function is executed, would be the newly created sub-node's parent.
            
            self.refresh(0) #refreshes the branch whenever a new node is added. by updating the public_values list of each parent node.
            
    
    """
    Program: check_run()
    WARNING: This program find the first value in the given tree that matches the input and runs the function bounded to the node containing the value.
    This might lead to problems when there are multiple values for different node-bounded functions.

    for example:
    INPUT                     ---> FILTERING ACTION ---> REACTION ---> OUTPUT
    play the song [song_name] ---> play [song name] ---> [play] as in [run a program]. tries to find a program installed with that name on pc. ---> [shows error as program isn't found]
    
    instead of,
    play the song [song_name] ---> play [song name] ---> [play] as in [play a song in spotify]. tries to find a song on spotify. ---> RUNS SUCCESFULLY
    
    
    This can be either patched with a method or only use unique values per node or design commands in heirarchial manner.
    """


    def check_run(self, key, value, local_dict={}):
    #takes in input, runs the action and also returns the inner variables as a dict.
    
        temp_vars = {}
        if key in self.public_keys:
            if value in self.private_values:
                exec(self.func_, local_dict, temp_vars) #self.func is the multi-line string with the saved function. the output of which is saved in temp_vars dict.
                return temp_vars
            
            else:
                for item in self.sub_nodes:
                    if key in item[1].public_keys:
                        return item[1].check_run(key, value, local_dict)
        else:
            print('Command Not Found.')

    def from_key(self, input): #retrieve the first node that has matching key/name.
        #print(input, self.key, self.sub_nodes, 1)
        if input in self.public_keys: #check if the name exists first in the public key of the tree branch.
            if input == self.key: #check if the input should be added to the main tree.
                return [self.key, self]
                
            else: #if not recursively find the sub-branch that the input should be added to.
                for item in self.sub_nodes:
                    if input in item[1].public_keys: #find if the input exists in a specific item's public_key.
                        temp_key = item[1].from_key(input) #if it does then make that the true branch and find the value.
                        return temp_key
                    
    def from_value(self, input): #retreive first node that has matching given value.
        if input in self.public_values: #check if the name exists first in the public value of the tree branch.            
            if input in self.private_values:
                return [self.key, self]
                
            else:
                for item in self.sub_nodes:
                    return item[1].from_value(input)
    
    def refresh(self, k):   #recurses backwards through the tree and changes the public values of all of it's nodes.
                            #must be used when adding a new node.            
        list_unique_keys = []
        list_unique_values = []
        
        for sub_node in self.sub_nodes:
            for item_key in sub_node[1].public_keys:
                if item_key not in self.public_keys:
                    list_unique_keys.append(item_key)
            
            for item_value in sub_node[1].public_values:
                if item_value not in self.public_values:
                    list_unique_values.append(item_value)
        
        
            if k==0:
                fltr_lst = [sub_node[1].key] + sub_node[1].private_values
                
            else:
                fltr_lst = sub_node[1].temp
                
            if fltr_lst not in self.temp and fltr_lst != []:
                if isinstance(fltr_lst[0], list) == True: #if it is a nested list.
                    for item in fltr_lst: #only pick out the unique values and add them.
                        if item not in self.temp:
                            self.temp.append(item)
                else:
                    self.temp.append(fltr_lst) #otherwise just add them.
            sub_node[1].temp = []
            
        
        #only pick a list of unique/unseen values/keys from the newly added node.
        #ignore all the list of values/keys from the already added nodes.
                
        self.public_values += list(list_unique_values)
        self.public_keys += list(list_unique_keys)
        
        if self.parent != None:
            self.parent.refresh(k=1)
    
    def clear_cache(self):
        del self.temp
        


#line formatter. Deprecated for now.
def format_line(txt, limit=60):
    if txt[:1].isdigit():
        txt_lst = [(txt.replace('\n', ' '))]
        final_lst = []
    
    else:
        txt_lst = txt.split('.')
        final_lst = []
        
        for item in txt_lst:
            if len(item) > limit:
                formatted_txt = ''
                u = 0
                for idx in range(1, len(item)+1):
                    if (idx % limit) == 0 and item[idx-1] == ' ':
                        formatted_txt += '\n'
                        
                    elif (idx % limit) == 0 and item[idx-1] != ' ':
                        u = 1
                    
                    
                    if u == 1 and item[idx-1] == ' ':
                        formatted_txt += '\n'
                        u = 0
                    
                    formatted_txt += item[idx-1]
                    
                final_lst.append(formatted_txt)
            
            else:
                final_lst.append(item)
    
    print(txt_lst, final_lst)
    return txt_lst, final_lst[:-1]
    

#word count. seperates words in a string to a list and gives how long they are.
def word_count(txt):
    txt = txt.replace('\n', '')
    word_lst = []
    vars = ['', 0]
    
    for idx in range(len(txt)):
        if txt[idx] == ' ':
            word_lst.append(vars)
            vars = ['', 0]
        else:
            vars[0] += txt[idx]
            vars[1] += 1
    
    word_lst.append(vars)
    
    return word_lst

#word similarity function. compares similarity of words on the basis of their letter similarities.
def word_sim(word_a, word_b):
    #padding the lower sized string with '#' to make both the strings the same length 
    word_a, word_b = word_a.lower(), word_b.lower()
    mini = min(len(word_a), len(word_b))
    
        
    f_word, l_word, m_word = 0, 0, 0 #checks whether the first and last words are the same.
    
    if word_a[0] == word_b[0]:
        f_word = 3
    if word_a[-1] == word_b[-1]:
        l_word = 3
    if word_a[int(len(word_a)/2)] == word_b[int(len(word_b)/2)]:
        m_word = 3
    
    
    if (len(word_a) > len(word_b)):
        word_b += '#'*(len(word_a) - len(word_b))
    else:
        word_a += '#'*(len(word_b) - len(word_a))
    
    
    similarity, continuity, equality = 0, 0, 0  #similarity means if a letter exists in another word.
                                                #continuity means if whether the equality has been broken or not.
                                                #equality is the most inportant relation. if it is max, everything else will be too.
    
    for index in range(len(word_a)):
        aword_, bword_ = word_a[index], word_b[index]
        
        if aword_ == '#' or bword_ == '#':
            break
        
        elif aword_ == bword_:
            equality   += 1
            continuity += 1
        
        elif aword_ != bword_ and continuity > 0:
            continuity -= 1
        
        if aword_ in word_b.lower():
            similarity += 0.5
    
    
    
    #(actual values of variables)/(their maximal values)
    score = (similarity + continuity + equality + f_word + l_word + m_word)/(2 + 4 + 4 + 3 + 3 + 3)

    return round(score, 2)
