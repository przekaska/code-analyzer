class Node:
    def __init__(self, value, name=None):
        self.value = value
        self.name = name
        self.parent = None
        self.children = []
        self.i = 0

    def addchild(self, child):
        child.parent = self
        self.children.append(child)
        return child
    
    def setparent(self, parent):
        self.parent = parent
        parent.children.append(self)
        return parent

    def __iter__(self):
        temp_node = Node("--TEMP-NODE--")
        temp_node.children.append(self)
        temp_node.c_node = temp_node
        return temp_node
    
    # c_node = current_node
    def __next__(self):
        if self.c_node.i < len(self.c_node.children):   
            self.c_node.i += 1
            self.c_node = self.c_node.children[self.c_node.i - 1]
        else:
            self.c_node.i = 0
            self.c_node = self.c_node.parent
            if self.c_node == None:
                raise StopIteration
        return self.c_node

