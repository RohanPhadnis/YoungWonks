import time, random

#bubble sort
def bubble_sort(l):
    init = time.time()
    temp = 0
    for n in range(len(l)-1,0,-1):
        for index in range(0,n):
            if l[index]>l[index+1]:
                temp = l[index]
                l[index]=l[index+1]
                l[index+1]=temp
    print('bubble sort:')
    print("Bubble sort is an algorithm that sorts a list. It iterates over the list and swaps two adjacent elements if they are in the wrong order. It keeps doing this, over and over again until the list is completely sorted.")
    print(l)
    print('time: '+str(time.time()-init))
    print()

def recursive_bubble_sort(l):
    corrected = 0
    for n in range(0,len(l)-1):
        if l[n]>l[n+1]:
            corrected+=1
            temp = l[n]
            l[n] = l[n+1]
            l[n+1] = temp
    if corrected == 0:
        print(l)
        return
    else:
        recursive_bubble_sort(l)

#selection sort
def selection_sort(l):
    init = time.time()
    low = 0

    for cut in range(0,len(l)-1):
        for index in range(cut+1,len(l)-1):
            if l[index]<l[low]:
                low = index
        if l[len(l)-1]<l[low]:
            low=len(l)-1
        temp = l[low]
        l.pop(low)
        l.insert(cut,temp) 


    for cut in range(0,len(l)-1):
        low  = cut
        for index in range(cut+1,len(l)):
            if l[index]<l[low]:
                low=index
        if low!=cut:
            l[cut],l[low]=l[low],l[cut]
    print('selection sort: ')
    print("Selection sort is another type of sorting algorithm. It swaps places of the max and min index.")
    print(l)
    print('time: '+str(time.time()-init))
    print()

def recursive_selection_sort(original,new):
    if len(original)==0:
        print(new)
        return
    else:
        val = min(original)
        original.remove(val)
        new.append(val)
        recursive_selection_sort(original,new)

#insertion sort

def insertion_sort(l):
    init = time.time()
    temp = 0
    temp2 = 0

    for index in range(1,len(l)):
        temp2 = index
        for index2 in range(index-1,-1,-1):
            if l[temp2]<l[index2]:
                temp = l[index2]
                l[index2]=l[temp2]
                l[temp2]=temp
                temp2-=1
    print('insertion sort:')
    print("The insertion sort algorithm compares each index with the indices before it to place it in the correct position")
    print(l)
    print('time: '+str(time.time()-init))
    print()

def recursive_insertion_sort(l,done):
    if len(done) == len(l):
        print(l)
        return
    else:
        for num in range(len(l)):
            if l[num] not in done:
                break
        place = num
        for num2 in range(num-1,-1,-1):
            if l[num]<l[num2]:
                place-=1
        temp = l[num]
        l.pop(num)
        l.insert(place, temp)
        done.append(temp)
        recursive_insertion_sort(l,done)


#merge sort

def split(num_list):
    if len(num_list)<=1:
        return num_list
    else:
        mid = len(num_list)//2
        left = split(num_list[:mid])
        right = split(num_list[mid:])
        return merge(left, right)

def merge(l,r):
    temp = []
    i = 0
    j = 0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            temp.append(l[i])
            i+=1
        else:
            temp.append(r[j])
            j+=1
    temp = temp+l[i:]
    temp = temp+r[j:]
    return temp

def merge_sort(l):
    init = time.time()
    print('merge sort')
    print("The merge sort algorithm breaks apart a list into smaller datasets and combines them in the correct order again.")
    print(split(l))
    print('time: '+str(time.time()-init))
    print()
