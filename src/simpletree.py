class Node:
    def __init__(self, object, name=None, parent=None):
        self.value = object
        self.name = name
        self.parent = parent
        self.children = []

    def addchild(self, object):
        child = Node(object, self)
        self.children.append(child)
        return child

