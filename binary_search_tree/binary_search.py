# Refer to README.md for the problem instructions


def createOrderedList(uList):
    oList = []
    
    for num_U in uList:
        # Empty list - insert first element
        if(len(oList) == 0):
            oList.append(num_U)
        # next element goes at the end of the list
        elif(num_U > oList[len(oList) - 1]):
            oList.append(num_U)
        # next element goes in the middle of the list
        else:
            i = 0
            while (num_U > oList[i] and i < len(oList)):
                i += 1
            oList.insert(i, num_U)
            
    return oList                


def binarySearch (lst, start, end, val): 
    return -1

ul = [8, 2, 3, 9, 1, 44, 22, 11, 90, 0]

createOrderedList(ul)
