class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def buildBST(nums):
    
    for i, num in enumerate(nums):
        if i ==0:
            r = Node(num)
        else:
            r = insert(r, num)
    return r


def findLevel(root, findVal):
    return None
    
numbers = [50, 30, 20 , 40, 70, 60, 80]

buildBST(numbers)
