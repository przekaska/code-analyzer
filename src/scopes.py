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
    create_scope(text, enumerate(text), type, name, start)


def create_scope(text, enumerator, type, name, start):
    current_scope = Scope(name, type, start)
    scopes.append(current_scope)
    end_word = ";"
    parentheses_level = 0

    for index, word in enumerator:
        current_scope.code.append(word)
        parentheses_level += (word == "(") - (word == ")")
    
        if word in types:
            if text[index + 2] == "(":
                create_scope(text, enumerator, text[index], text[index + 1], index)
        if word in special_types:
            word = create_scope(text, enumerator, text[index], text[index], index)

        if word == '{' and not parentheses_level:
            end_word = "}"
        if word == end_word and not parentheses_level:
            current_scope.stop = index
            return ";"
        
