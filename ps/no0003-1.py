from collections import defaultdict

import sys

INIT = 0
NORMAL = 1
EARLY = 2
VISITED = 1
NOT_VISITED = 2

class Node(object):
    def __init__(self, name=None, data=None, parent=None):
        self.name = name
        self.data = data
        self.parent = parent
        self.status = INIT
        self.early_count = 0
        self.children = []

    def add_child(self, child):
        # Check if Child is Node()
        if type(child) is not type(self):
            print('Child not added.')
            print('Child[{0}] is not type:{1}'.format(type(child),type(self)))
            return
        # Check if child is self or if child is ancestor
        ancestors = self.get_ancestors()
        if child is not self and child not in ancestors:
            self.children.append(child)
            child.parent = self
        # Check Failed. Would cause infinite recursion
        else:
            print('Child not added. Recursive loop.')
            print('Tried to add: [{0}] to Self:[{1}] | Ancestors:{1}'.format(child, self, ancestors))
            # Print recursion cause
            if child is self:
                print('Child is self')
            else:
                print('Child is ancestor')

    def get_children(self):
        return self.children

    def get_child(self, index):
        try:
            return self.children[index]
        except IndexError:
            print('Child index not found')

    # Perhaps parent should be list. 
    # Current implementation fails if node is child of different nodes
    # only returns last parent
    def get_parent(self):
        return self.parent

    def get_ancestors(self):
        ancestor = self.parent
        ancestors = [ancestor]
        try:
            while ancestor.parent != None:
                ancestors.append(ancestor)
                parent = self.parent
                ancestor = parent.get_parent()
            return ancestors
        # Node is root. Root's parent is None
        except AttributeError:
            return []

    def get_sibblings(self):
        # Excludes self
        if self.parent is not None:
            parents_chidren = list(self.parent.children)
            parents_chidren.pop(self.get_index())
            siblings = parents_chidren
            return siblings

    def get_index(self):
        for n, child in enumerate(self.parent.children):
            if child is self:
                return n

    def remove_child(self, index):
        try:
            self.children.pop(index)
        except IndexError:
            print('Cannot remove. Child Index not found')
        return self.children

    def print_tree(self, level=0):
        print('\t' * level + '+'*(level+1) + repr(self))
        # Check if in infinite recursion loop.
        if level > 10:
            print('Maxium recursion exceeded.')
            raise Exception('Maximum recursion.')
            sys.exit()
        for child in self.children:
            child.print_tree(level+1)

    def __repr__(self):
        if self.children == []:
            return '[Leaf:{0}-S:{2}-EC:{3}|Parent:{1}]'.format(self.name, self.parent, self.status,self.early_count)
        else:
            return '[Node:{0}-S:{2}-EC:{3}|Parent:{1}]'.format(self.name, self.parent, self.status,self.early_count)

    def find_early_adaptor(self,level=0):
        #print('\t' * level + '-'*(level+1) + repr(self))
        if self.children == []:
            self.status = NORMAL
            return 0
        flag = 0
        for child in self.children:
            child.find_early_adaptor(level+1)
            self.early_count += child.early_count
            if child.status != EARLY:
                flag = 1
        if flag == 1:
            self.status = EARLY
            self.early_count += 1
        else:
            self.status = NORMAL
        #print('\t' * level + '+'*(level+1) + repr(self))


def makeTree(node):
    #for i in node_dic:
        #print("[" , i , "]", node.name)
    if node_dic[node.name] == VISITED:
        return 0

    node_dic[node.name] = VISITED
    p_info = new_dic[node.name];
    #print("\nID:", node.name)
    for childName in p_info:
        if node_dic[childName] != VISITED:
            #print(childName , ':', p_info[childName])
            child = Node(name=childName)
            node.add_child(child)
            makeTree(child)
    return 1 


#print("Input the count of node")
nodeCount = int(input())
new_dic = defaultdict(dict)
visited_dic = defaultdict(dict)
node_dic = defaultdict(dict)
node_depth = defaultdict(dict)
zeroCount = defaultdict(dict)
zeroCount[0] = 0
for i in range(nodeCount-1):
    #print( i , " of " , nodeCount-1 , " Input the value of x & y")
    x, y = map(int, input("").split(" "))
    #print("The value of x & y are: ",x,y)
    new_dic[x][y] = 11
    new_dic[y][x] = 22
    node_dic[i] = NOT_VISITED
    node_depth[i] = 0

root = Node(name=1)
makeTree(root)
root.find_early_adaptor()
print(root.early_count)

