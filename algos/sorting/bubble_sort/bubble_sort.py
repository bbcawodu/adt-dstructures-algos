def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # negative range (3rd param) means returned list is reversed and starts from the end.
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
