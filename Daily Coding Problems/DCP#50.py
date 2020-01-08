'''
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each
internal node is one of '+', '−', '∗', or '/'
'''
class treeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def arthExpressionTree(node):
    if node.value.isnumeric():
        return int(node.value)
    
    return eval("{} {} {}".format(arthExpressionTree(node.left), node.value, arthExpressionTree(node.right)))
  
a = treeNode("*")
b = treeNode("+")
c = treeNode("+")
a.left = b
a.right = c

d = treeNode("3")
e = treeNode("2")
b.left = d
b.right = e
f = treeNode("4")
g = treeNode("5")
c.left = f
c.right = g

print(arthExpressionTree(a))    #45
print(arthExpressionTree(b))    #5
print(arthExpressionTree(c))    #9