defined = {}

def include():
    return True

def define(name, value):

    defined[name] = value

def ifdef(name):
    try:
        defined[name]
        return True
    except:
        return False

def ifndef(name):
    try:
        defined[name]
        return False
    except:
        return True

def preprocess_text(text, outfile, write_mode=True, index=0):
    while index < len(text):
        if(text[index] == "#endif"):
            return index

        if write_mode:
            try:
                outfile.write(" " + defined[text[index]])
            except:
                if(text[index] == "#define"):
                    define(text[index + 1], text[index + 2])
                    index += 2
                elif(text[index] == "#ifdef"):
                    index = preprocess_text(text, outfile, ifdef(text[index + 1]), index + 2)
                elif(text[index] == "#ifndef"):
                    index = preprocess_text(text, outfile, ifndef(text[index + 1]), index + 2)
                elif(text[index] == "#include"):
                    index += 3          # FINISH INCLUDE!!!!!
                else:
                    outfile.write(" " + text[index])
        index += 1

def preprocess(text, file_name):
    outfile = open(file_name, "w")
    preprocess_text(text, outfile)
    xd = 7
    outfile.close()  

