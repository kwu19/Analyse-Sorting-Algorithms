#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:26:53 2018

@author: kefei
"""

def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position - 1]
            position = position-1
            
        alist[position] = current_value
        
def selection_sort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        position_of_max = 0
        
        for location in range(1, fillslot+1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
                
        temp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = temp
        
def shell_sort(alist):
    gap = 2
    sublistcount = len(alist)//gap  # "gap" == 2
    
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        
        if len(alist) <= 15:
            print("After increments of size", sublistcount, "The list is", alist)
        
        sublistcount = sublistcount // gap
        
def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]
        position = i
        
        while (position >= gap and
               alist[position-gap] > current_value):
               
                alist[position] = alist[position-gap]
                position = position - gap
                
        alist[position] = current_value
        
def merge_sort(alist):
    #print("Splitting ", alist)
    
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
                
            k += 1
                
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
            
def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
    if first  <last:
        splitpoint = partition(alist,first,last)

        quick_sort_helper(alist,first,splitpoint-1)
        quick_sort_helper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last
 
    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

# test
from random import sample, choices
import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

big_list_1 = choices(range(5_000), k=500)
big_list_2 = choices(range(5_000), k=600)
big_list_3 = choices(range(5_000), k=700)
big_list_4 = choices(range(5_000), k=800)
big_list_5 = choices(range(5_000), k=900)

big_lists = [big_list_1, big_list_2, big_list_3, big_list_4, big_list_5]

results_bub = []
results_ins = []
results_sel = []
results_she = []
results_mer = []
results_qui = []

for lst in big_lists:
    
    t_bub = timeit.Timer("bubble_sort(alist)", globals={"bubble_sort":bubble_sort, "alist":lst})
    t_ins = timeit.Timer("insertion_sort(alist)", globals={"insertion_sort":insertion_sort, "alist":lst})
    t_sel = timeit.Timer("selection_sort(alist)", globals={"selection_sort":selection_sort, "alist":lst})
    t_she = timeit.Timer("shell_sort(alist)", globals={"shell_sort":shell_sort, "alist":lst})
    t_mer = timeit.Timer("merge_sort(alist)", globals={"merge_sort":merge_sort, "alist":lst})
    t_qui = timeit.Timer("quick_sort(alist)", globals={"quick_sort":quick_sort, "alist":lst})
    
    results_bub.append(t_bub.timeit(10))
    results_ins.append(t_ins.timeit(10))
    results_sel.append(t_sel.timeit(10))
    results_she.append(t_she.timeit(10))
    results_mer.append(t_mer.timeit(10))
    results_qui.append(t_qui.timeit(10))

print(results_bub)
print(results_ins)
print(results_sel)
print(results_she)
print(results_mer)
print(results_qui)

sizes = [len(lst) for lst in big_lists]

fig, ax = plt.subplots()
plt.ylabel("Running Time (ms)")
plt.xlabel("Input Size ($N$)")
ax.plot(sizes, results_bub, label='Bubble Sort', color='b')
ax.plot(sizes, results_ins, label='Insertion Sort', color='g')
ax.plot(sizes, results_sel, label='Selection Sort', color='r')
ax.plot(sizes, results_she, label='Shell Sort', color='c')
ax.plot(sizes, results_mer, label='Merge Sort', color='m')
ax.plot(sizes, results_qui, label='Quick Sort', color='y')

legend = plt.legend(loc='center right', fontsize='small')
plt.show()