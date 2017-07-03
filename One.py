'''
Created on Jul 2, 2017

@author: rjw0028
'''
import random, sys

# Following code tries to tackle the N Qeens problem, using backtracking technique... The algo was available online, the code is written by me... 
global _QUEENS_
_QUEENS_ = []  # Contains [i,j] of all the queens placed...

def pop():
    if len(_QUEENS_) > 0:
        del _QUEENS_[-1]
    return
def push(i,j):
    _QUEENS_.append([i,j])
    return


def Diagonal1(x, y, i, j, n):
    ans = True
    if x > y:
        xt1 = x - y
        xb1 = n - 1
        yt1 = 0
        yb1 = n - 1 - (x - y)

    elif x == y:
        xt1 = 0
        xb1 = n - 1
        yt1 = 0
        yb1 = n - 1 
            
    elif x < y:
        xt1 = 0
        xb1 = n - 1
        yt1 = y - x
        yb1 = n - 1 - (y - x)
    Done = True
    p = xt1
    q = yt1
    
    while p <= xb1 and q <= yb1:
        if p == i and q == j:
            return False
        p += 1
        q += 1
    
    return ans

def Diagonal2(x, y, n):
    ans = True
    return ans


def isSafe(i,j, n):
    ans = True
    if len(_QUEENS_) == 0:
        return ans
    
    for Q in _QUEENS_:
        if Q[0] == i or Q[1] == j:
            return False
        if not Diagonal1(Q[0], Q[1], i, j, n):
            return False
        #elif not  Diagonal2(Q[0], Q[1], n):
         #   return False
#     x = random.random()        # Used this code to generate random places for Queens..
#     if x > 0.50:
#         ans = True
#     else:
#         ans = False
    return ans

def firstQueen(x,y):
    _QUEENS_ = []
    _QUEENS_.append([x,y])
    return

def displayBoard(n):
    for x in range(n):
        for y in range(n):
            if [x,y] in _QUEENS_:
                sys.stdout.write('<Q> ')
                sys.stdout.flush()
            else:
                sys.stdout.write('--- ')
                sys.stdout.flush()    
        print
    return

def Solution(n):
    for x in range(n):
        for y in range(n):
            firstQueen(x,y)
            for i in range(n):
                for j in range(n):
                    if [i,j] not in _QUEENS_:
                        if isSafe(i, j, n):
                            push(i,j)
                            print "Board:"
                            displayBoard(n)
                            if len(_QUEENS_) == n:
                                displayBoard(n)
                                return
                
    
def main():    
    n = int(raw_input("Enter an integer for the value of N"))
    
    Solution(n)
    
    
    
    
    
    return 0

if __name__ == '__main__':
    main()
        

