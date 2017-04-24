# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:35:02 2017

@author: gabrielfior
"""

"""
def solution(X, A):
    # write your code in Python 2.7
    # count array
    # when count = X, it's time
    seen = []
    for i,j in enumerate(A):
        #print j
        if j not in seen:
            #print 'appended '+str(j)
            seen.append(j)
        seen.sort()
        #print seen
        #print (seen == range(1,X+1))
        try:        
            if (seen == range(1,X+1))==True:
                return i
                #quit()
        except AttributeError:
            #print 'error here'
            pass
    return -1

A = [1,3,1,4,2,3,5,4,10]
A=np.array(A)
X=5

print solution(X,A)

A = [1,3,1,4,2,3,4,4]
A=np.array(A)
X=5
print solution(X,A)
"""
"""
def solution(N, A):
    # write your code in Python 2.7
    counter=[0]*N
    print counter
    for i in A:
        print i
        if i==N+1:
            max1 = max(counter)
            for jj in range(len(counter)):
                counter[jj] = max1        
        
        elif i<=N and i>=1:
            counter[i-1]+=1

        print counter
    return counter


print solution(5, [3, 4, 4, 6, 1, 4, 4])

"""
"""
A = [1,2,3,4,5,]
n = len(A)
P = [0] * (n + 1)
for k in xrange(1, n + 1):
    P[k] = P[k - 1] + A[k - 1]
"""
def solution(A):
    
    westcars=0
    cnt_passings=0
    for i in xrange(len(A)-1,-1,-1):
        print i
        if A[i]==0:
            cnt_passings+=westcars
            print 'cnt passings'
            print cnt_passings
            if cnt_passings>1e6:
                return -1
        else:
            westcars +=1
            print 'westcars'
            print westcars
    return cnt_passings


A=[0, 1, 0, 1, 1] 

print solution(A)



















