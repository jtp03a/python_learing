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
    level = 0
    level = search(root, findVal, level)
    return level
    
def search(root, findVal, level):
    if root is None or root.val == findVal:
        return level
    level += 1
    if root.val < findVal:
        return search(root.right, findVal, level)
    else:
        return search(root.left, findVal, level)
   
   
    
numbers = [50, 30, 20 , 40, 70, 60, 80]

r = buildBST(numbers)

result = findLevel(r, 80)

print(result)

numbers2 = [7, 3, 8, 9, 2, 6]

r2 = buildBST(numbers2)

result2 = findLevel(r, 6)

print(result)

result2 = findLevel(r, 16)

print(result)
