from simpletree import *

scopes = []

types = ["int", "char", "float", "double", "void"]
special_types = ["for", "while", "if"]

class Scope:        # consider changing class to list
    def __init__(self, name, type, start, stop = False):
        # self.id = id
        self.name = name
        self.type = type
        self.start = start
        self.stop = stop
        self.code = [] 

def init_scopes(text, type, name, start):
    scope_tree = create_scope(text, enumerate(text), type, name, start)
    return scope_tree


def create_scope(text, enumerator, type, name, start):
    current_scope = Scope(name, type, start)
    scopes.append(current_scope)
    current_node = Node(current_scope, name)
    end_word = ";"
    parentheses_level = 0

    for index, word in enumerator:
        current_scope.code.append(word)
        parentheses_level += (word == "(") - (word == ")")
    
        if word in types:
            if text[index + 2] == "(":
                current_node.addchild(create_scope(text, enumerator, text[index], text[index + 1], index))
        elif word in special_types:
            current_node.addchild(create_scope(text, enumerator, text[index], text[index], index))
            if end_word == ";":
                word = ";"

        if word == '{' and not parentheses_level:
            end_word = "}"
        if word == end_word and not parentheses_level:
            current_scope.stop = index
            return current_node
        
    current_scope.stop = index
    return current_node
