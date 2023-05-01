from preprocessor import * 
from scopes import *

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
text = text.replace("\n", " \n ")
text = text.split(" ")
text = list(filter(str, text))
# print(text)
f.close()    

preprocess(text, "c_test_files/outfile.c")
f = open("c_test_files/outfile.c")
text = f.read()
text = text.split()
# print(text)

tree = init_scopes(text, "*GLOBAL*", "*GLOBAL*")

for scope in scopes:
    print(scope.name, "\n\n", scope.code, "\n\n")

print(defined)

