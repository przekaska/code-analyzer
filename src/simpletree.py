class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self._i = 0 # used by the __next__ method to keep track of the children

    def addchild(self, child):
        child.parent = self
        self.children.append(child)
        return child
    
    def setparent(self, parent):
        self.parent = parent
        parent.children.append(self)
        return parent

    # __iter__ method needs to create the temp_node, because the __next__ method  returns nodes
    # starting from the first child (so it won't return the root itself if we start from the
    # root). Adding temp_node with root as a child solves this problem.
    def __iter__(self):
        temp_node = Node()              
        temp_node.children.append(self) # it doesn't change the parent of the 'self'
        temp_node.c_node = temp_node # c_node (current_node) is used by the __next__ method
        return temp_node                
                                        
    # c_node = current_node
    def __next__(self):
        if self.c_node._i < len(self.c_node.children):   
            self.c_node._i += 1 # each node has its own 'i' so it needs to be incremented
                                # before changing current_node 
            self.c_node = self.c_node.children[self.c_node._i - 1]
        else:
            self.c_node._i = 0 
            self.c_node = self.c_node.parent    
            if self.c_node == None: 
                raise StopIteration
        return self.c_node

