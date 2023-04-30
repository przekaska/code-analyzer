from preprocessor import * 
from scopes import *

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
f.close()    

preprocess(text, "c_test_files/outfile.c")
f = open("c_test_files/outfile.c")
text = f.read()
text = text.split()
print(text)

init_scopes(text, "*GLOBAL*", "*GLOBAL*", 0)

for scope in scopes:
    print("SCOPE: ", scope.name, scope.type, text[scope.start], text[scope.stop], "\n\n", scope.code, "\n\n")   

print(defined)

