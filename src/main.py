from preprocessor import *

class Scope:        # consider changing class to list
    def __init__(self, name, type, start, stop = False):
        # self.id = id
        self.name = name
        self.type = type
        self.start = start
        self.stop = stop
        self.code = []  

{
# text = text.replace("(", " ( ")
# text = text.replace(")", " ) ")
# text = text.replace("[", " [ ")
# text = text.replace("]", " ] ")
# text = text.replace("{", " { ")
# text = text.replace("}", " } ")
# text = text.replace(",", " , ") 
# text = text.replace("*", " * ")
# text = text.replace("+", " + ")
# text = text.replace("-", " - ")
# text = text.replace("/", " / ")
# text = text.replace("%", " % ")
# text = text.replace("=", " = ")
# text = text.replace(">", " > ")
# text = text.replace("<", " < ")
# text = text.replace(";", " ; ")
# text = text.replace("\"", " \" ")
# text = text.replace("'", " ' ")
# text = text.replace("!", " ! ")
# text = text.replace("&", " & ")
# text = text.split()

# scopes = []

# types = ["int", "char", "float", "double", "void"]
# special_types = ["for", "while", "if"]

# def create_scope(enumerator, type, name, start):
#     current_scope = Scope(name, type, start)
#     scopes.append(current_scope)
#     end_word = ";"
#     parentheses_level = 0

#     for index, word in enumerator:
#         current_scope.code.append(word)
#         parentheses_level += (word == "(") - (word == ")")
    
#         if word in types:
#             if text[index + 2] == "(":
#                 create_scope(enumerator, text[index], text[index + 1], index)
#         if word in special_types:
#             word = create_scope(enumerator, text[index], text[index], index)

#         if word == '{' and not parentheses_level:
#             end_word = "}"
#         if word == end_word and not parentheses_level:
#             current_scope.stop = index
#             return ";"

# create_scope(enum, "GLOBAL", "GLOBAL", 0)
# for scope in scopes:
    # print("SCOPE: ", scope.name, scope.type, text[scope.start], text[scope.stop], "\n\n", scope.code, "\n\n")   
}
f = open("c_test_files/testfile1.c")

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
text = text.replace("\n", " \n ")
text = text.split(" ")
text = list(filter(str, text))
print(text)


preprocess(text, "c_test_files/outfile.c")

enum = enumerate(text)
print(defined)

f.close()    
