# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:22:33 2017

@author: gabrielfior
"""


def solution(A):

    total_time=0
    print 'started, total time: '+str(total_time)

    A.sort()
    while len(A)>1:
        print A        
        new_item = sum(A[:2])
        A = A.insert(0,new_item)
        print A
        A=A[2:]
        total_time += new_item
        print 'total time: ' + str(total_time)
        
    return total_time

print solution([100, 250, 1000]) #1350
print solution([1010, 250, 1000]) #3260
print solution([0,10,10,30,80]) #3260

b = [2,4,5,6]


print [(b[p1], b[p2]) for p1 in range(len(b)) for p2 in range(p1+1,len(b))]