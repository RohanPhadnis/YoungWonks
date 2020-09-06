from search import *
from sorting import *
import time, random

#Sieve of Erosthasthanos
def sieve():
    n = int(input('What number do you want to find prime numbers till? '))
    init = time.time()
    l=[]

    for x in range(2,n+1):
        if x not in l:
            for y in range(2,x):
                if x%y == 0:
                    l.append(x)
                    break

    l2=[]
    for x in range(2,n+1):
        if x not in l:
            l2.append(x)

    print('The Sieve of Erosthasthanos is an algorithm that finds all prime numbers till a defined limit')
    print(l2)
    print('time: '+str(time.time()-init))

print("--------------Sorting algorithms---------------")
data = [23,56,67,94,2,76,100,25,50]
bubble_sort(data)
print()
print('Recursive Bubble Sort')
init = time.time()
recursive_bubble_sort(data)
print('time: '+str(time.time()-init))
print()
print()
selection_sort(data)
print()
print('Recursive Selection Sort')
init = time.time()
recursive_selection_sort(data,[])
print('time: '+str(time.time()-init))
print()
print()
insertion_sort(data)
print()
print('Recursive Insertion Sort')
init = time.time()
recursive_insertion_sort(data,[])
print('time: '+str(time.time()-init))
print()
print()
merge_sort(data)
print('Merge sort is already recursive...')
print()
print()
print()
print()

print("--------------Search algorithms----------------")
data = [23,56,67,94,2,76,100,25,50]
linear_search(76,data)
data = list(range(0,100,1))
tgt = random.randint(0,100)
print(tgt)
binary_search(data,tgt)
print()
print('Recursive Binary Search')
init = time.time()
recursive_binary_search(data,tgt,[0,len(data)-1])
print('time: '+str(time.time()-init))
print()
print()
print()
print()

print("---------------Sieve of Erosthasthanos-----------------")
sieve()
print()
print()
print()
print()

print("---------------Loops: For Loops vs While Loops vs Recursion------------------")
def funct(start, stop, step):
    if start+step>stop:
        return start
    else:
        funct(start+1, stop, step)
init = time.time()
funct(0,500,1)
print('recursion time: '+str(time.time()-init))

init = time.time()
for n in range(0,500,1):
    pass
print('for loop time: '+str(time.time()-init))

init = time.time()
x = 0
while x<500:
    x+=1
print('while loop time: '+str(time.time()-init))
