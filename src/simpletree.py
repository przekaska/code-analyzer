class Node:
    def __init__(self, value, name=None):
        self.value = value
        self.name = name
        self.parent = None
        self.children = []

    def addchild(self, child):
        child.parent = self
        self.children.append(child)
    
    def setparent(self, parent):
        self.parent = parent
        parent.children.append(self)





