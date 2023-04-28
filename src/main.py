class Scope:        # consider changing class to list
    def __init__(self, name, type, start):
        # self.id = id
        self.name = name
        self.type = type
        self.start = start
        # self.stop = stop
        # self.parameters = []
        # self.variables = []


f = open("c_test_files/testfile2.c")

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
text = text.split()

print(text)

variables = []
scopes = []

def create_variable(type, name):
    variables.append([type, name])

types = ["int", "char", "float", "double", "void"]
special_types = ["for", "while", "if"]

def create_scope(enumerator, type, name, start):
    scopes.append(Scope(name, type, start))
    for index, word in enumerator:
        if word in types:
            if text[index + 2] == "(":
                create_scope(enumerator, text[index], text[index + 1], index)
            else:
                print("VARIABLE: ", text[index], text[index + 1])
        elif word == "}":
            return 0

enum = enumerate(text)

create_scope(enum, "GLOBAL", "GLOBAL", 0)
for scope in scopes:
    print("SCOPE: ", scope.name, scope.type, text[scope.start])   

f.close()
