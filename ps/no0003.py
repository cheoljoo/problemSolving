from collections import defaultdict

import sys

INIT = 0
NORMAL = 1
EARLY = 2

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


root = Node(name='root')
child1 = Node(name='child1')
root.add_child(child1)

child2 = Node(name='child2')
child1.add_child(child2)
child1.add_child(child2)
root.add_child(child2)

print('\n---TEST PRINT TREE---\n')
root.print_tree()
child1.print_tree()

print('\n---TEST RECURSION LOOP CHECKS---\n')

root.add_child(root)
child1.add_child(root)

print('\n---TEST METHODS---\n')

print('roots children: ', root.children)
print('child1 children: ', child1.children)
print('root parent: ', root.parent)
print('child1 parent: ', child1.parent)
print('child2 parent: ', child2.parent)

print('root siblings: ', root.get_sibblings())
print('child1 siblings: ', child1.get_sibblings())

print('child1 index: ', child1.get_index())
print('child2 index: ', child2.get_index())

print('\n---TEST REMOVE CHILD---\n')

print('roots children:', root.children)
print('remove child:', root.remove_child(child2.get_index()))
print('roots children:', root.children)

LEAF_NODE = 1
NODE = 2
HAS_NODE = 1
NO_NODE = 2
NOT_VISITED = 0
VISITED = 1

def makeTree(node):
    for i in node_dic:
        print("[" , i , "]", node.name)
    if node_dic[node.name] == VISITED:
        return NO_NODE

    node_dic[node.name] = VISITED
    p_info = new_dic[node.name];
    print("\nID:", node.name)
    for childName in p_info:
        if node_dic[childName] != VISITED:
            print(childName , ':', p_info[childName])
            child = Node(name=childName)
            node.add_child(child)
            makeTree(child)
    return HAS_NODE 


def traverse(n,depth):
    if node_dic[n] == 0:
        return 0

    print("traverse:", n)
    print("node_dic:", node_dic[n])
    print("node_depth:", depth)

    if depth == 1:
        depth = 0
    else:
        depth = 1
        zeroCount[0] += 1

    #for p_id, p_info in new_dic.items():
    node_dic[n]=0
    p_info = new_dic[n];
    print("\nID:", n)
    for key in p_info:
        visited_dic[n][key] = 1
        print(key , ':', p_info[key])
        traverse(key,depth)
    return 1


print("Input the count of node")
nodeCount = int(input())
new_dic = defaultdict(dict)
visited_dic = defaultdict(dict)
node_dic = defaultdict(dict)
node_depth = defaultdict(dict)
zeroCount = defaultdict(dict)
zeroCount[0] = 0
for i in range(nodeCount-1):
    print( i , " of " , nodeCount-1 , " Input the value of x & y")
    x, y = map(int, input("").split(" "))
    print("The value of x & y are: ",x,y)
    new_dic[x][y] = 11
    new_dic[y][x] = 22
    node_dic[i] = NOT_VISITED
    node_depth[i] = 0

root = Node(name=1)
makeTree(root)
root.find_early_adaptor()
root.print_tree()
print(root.early_count)

