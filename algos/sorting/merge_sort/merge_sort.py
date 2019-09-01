def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        mergeTwoLists(alist, lefthalf, righthalf)

    print("Merging ",alist)


def mergeTwoLists(baselist, lefthalf, righthalf):
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            baselist[k] = lefthalf[i]
            i = i + 1
        else:
            baselist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        baselist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        baselist[k] = righthalf[j]
        j = j + 1
        k = k + 1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
