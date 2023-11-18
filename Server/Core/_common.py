"""
Darwin's common. Where it contains all the classes and functions that are require by Darwin and its sub-files.
"""
from os import path
from importlib.util import spec_from_file_location

# doubly connected list: 2-way list data object.

def eliminator(list, string):
    string = string.lower()
    for i in list: string = string.replace(i.lower(), '')
    return string.strip()

class Bubble:
    def __init__(self):
        self.keys = []
        self.values = []
        self.idxs = []

    def add(self, key, value):
        self.idxs.append(len(self.keys))
        self.keys.append(key)
        self.values.append(value)

    def retrieve(self, key_or_value, tag=0):  # when tag is 1 it retrieves the index. default 0.
        if tag == 0:
            instances = [
                self.values[i] if [key_or_value] == [self.keys[i]] else self.keys[i] if key_or_value in self.values[
                    i] else [] for i in self.idxs]
            # for i in self.idxs:                        #keys are unique.

            #        if [key_or_value] == [self.keys[i]]: instances.append(self.values[i])
            #        elif key_or_value in self.values[i]: instances.append(self.keys[i])

        else:
            if isinstance(key_or_value, list):
                return self.values.index(key_or_value)
            else:
                return self.keys.index(key_or_value)
            # if [key_or_value] == [self.keys[i]] or key_or_value in self.values[i]: return i #instances.append(i)

        return instances

    def print_obj(self):
        string = '([\n'
        for i, j in zip(self.keys, self.values):
            string += f'({i}|{j})\n'
        string += '])'
        print(string)


def purify(string):
    for word in ["'s", "'", '.', ',', ':', '?', '|', '!']: string = string.replace(word, '').lower()
    return string


def find_func(checklist): return [(key) for key, value in checklist.items() if value == max(checklist.values())]


def compress(list_):
    list__ = []
    for i in list_:
        if type(i) == type([]):
            list__ += compress(i)
        else:
            list__.append(i)
    return list__


"""
This is the node class.
This is technically the neuron of darwin's brain. 
This is object that has binds functions and dialogue text to darwin.
by running already-encoded actions/functions.

Current Version: V3
Changes: Simpler, Faster, Smarter.
"""

def merge(dict1, dict2): return {**dict1, **dict2}

def check_run(file, func, cmd, time_details):
    # takes in input, runs the action and also returns the inner variables as a dict.
    location = str(path.abspath(__file__)).replace('Core', 'Edge').replace('_common.py', 'Modules/')
    objective_func = spec_from_file_location(file, location + file).loader.load_module().objective
    text = objective_func(func, cmd, func_dict=merge(globals(), locals()))

    return text