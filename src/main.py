class Scope:        # consider changing class to list
    def __init__(self, name, type, start, stop = False):
        # self.id = id
        self.name = name
        self.type = type
        self.start = start
        self.stop = stop
        # self.parameters = []
        self.variables = []     

f = open("c_test_files/testfile3.c")

text = f.read()
text = text.replace("(", " ( ")
text = text.replace(")", " ) ")
text = text.replace("[", " [ ")
text = text.replace("]", " ] ")
text = text.replace("{", " { ")
text = text.replace("}", " } ")
text = text.replace(",", " , ") 
text = text.replace("*", " * ")
text = text.replace("+", " + ")
text = text.replace("-", " - ")
text = text.replace("/", " / ")
text = text.replace("%", " % ")
text = text.replace("=", " = ")
text = text.replace(">", " > ")
text = text.replace("<", " < ")
text = text.replace(";", " ; ")
text = text.replace("\"", " \" ")
text = text.replace("'", " ' ")
text = text.replace("!", " ! ")
text = text.replace("&", " & ")
text = text.split()

scopes = []

types = ["int", "char", "float", "double", "void"]
special_types = ["for", "while", "if"]

def create_scope(enumerator, type, name, start):
    current_scope = Scope(name, type, start)
    scopes.append(current_scope)
    end_word = ";"
    parentheses_level = 0

    for index, word in enumerator:
        parentheses_level += (word == "(") - (word == ")")
    
        if word in types:
            if text[index + 2] == "(":
                create_scope(enumerator, text[index], text[index + 1], index)
        if word in special_types:
            word = create_scope(enumerator, text[index], text[index], index)

        if word == '{' and not parentheses_level:
            end_word = "}"
        if word == end_word and not parentheses_level:
            current_scope.stop = index
            return ";"

enum = enumerate(text)
print(text)
create_scope(enum, "GLOBAL", "GLOBAL", 0)
for scope in scopes:
    print("SCOPE: ", scope.name, scope.type, scope.variables, text[scope.start], text[scope.stop])   

f.close()
