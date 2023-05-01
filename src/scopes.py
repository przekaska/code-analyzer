from simpletree import *

scopes = []

types = ["int", "char", "float", "double", "void"]
special_types = ["for", "while", "if"]

class Scope(Node):
    def __init__(self, name, type):
        super().__init__()
        self.name = name
        self.type = type
        self.code = [] 

def init_scopes(text, type, name):
    scope_tree = create_scope(text, enumerate(text), type, name)
    return scope_tree


def create_scope(text, enumerator, type, name):
    current_scope = Scope(name, type)
    scopes.append(current_scope)
    end_word = ";"
    parentheses_level = 0

    for index, word in enumerator:
        parentheses_level += (word == "(") - (word == ")")
    
        if word in types:
            if text[index + 2] == "(":
                current_scope.addchild(create_scope(text, enumerator, text[index], next(enumerator)[1])) 
                text[index] = "#"
        elif word in special_types:
            current_scope.addchild(create_scope(text, enumerator, text[index], text[index]))
            text[index] = "#"
            if end_word == ";":
                word = ";"

        if word == '{' and not parentheses_level:
            end_word = "}"
        if word == end_word and not parentheses_level:
            return current_scope
        
        current_scope.code.append(text[index])
        
    current_scope.stop = index
    return current_scope
