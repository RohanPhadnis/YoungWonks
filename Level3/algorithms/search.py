import random, time

#Linear Search
def linear_search(val,lst):
    if val not in lst:
        print("Item not in list")
    else:
        init = time.time()
        for n in range(0,len(lst)):
            if lst[n] == val:
                break
        print('Linear Search:')
        print("The linear search algorithm goes through a list in order to find the index of a targetted value")
        print('index: ' + str(n))
        print('time: '+str(time.time()-init))
    print()

#Binary Search
def binary_search(l,target):
    if target not in l:
        print("Item not in list")
    else:
        init = time.time()
        limits = [0,len(l)-1]
        index = 0
        while True:
            if (limits[0]+limits[1])//2 == index:
                break
            else:
                index = (limits[0]+limits[1])//2
            if l[index]==target:
                break
            elif l[index]>target:
                limits[1] = index
            else:
                limits[0] = index
        print('Binary Search:')
        print("The binary search algorithm is an algorithm that can effectively search for items in a sorted list. It calculates the limits of its data set and reduces down on its target.")
        if l[index] == target:
            print('Target found. Index: '+str(index))
        else:
            print('Target not in list')
        print('time: '+str(time.time()-init))
    print()


def recursive_binary_search(l,target,limits):
    if target in l:
        if l[(limits[0]+limits[1])//2] == target:
            print('target found. index: '+str((limits[0]+limits[1])//2))
            return
        elif l[(limits[0]+limits[1])//2] > target:
            recursive_binary_search(l,target,[limits[0],(limits[0]+limits[1])//2])
        else:
            recursive_binary_search(l,target,[(limits[0]+limits[1])//2,limits[1]])
    else:
        print('target not in list')
