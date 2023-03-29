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
    if(end >= start):
        mid = (start + end) // 2
        if (lst[mid] == val):
            print('found')
            return mid
        elif (val > lst[mid]):
            binarySearch(lst, mid + 1, end, val)
        else:
            binarySearch(lst, start, mid - 1, val)
    else:
        print('not found')
        return -1


ul = [8, 2, 3, 9, 1, 44, 22, 11, 90, 0]

ol = createOrderedList(ul)

print(ol)

result = binarySearch(ol, 0, len(ol) - 1, 11)

print(str(result))
