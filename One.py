'''
Created on Jul 2, 2017

@author: rjw0028
'''
import random, sys

# Following code tries to tackle the N Qeens problem, using backtracking technique... The algo was available online, the code is written by me... 
global _QUEENS_
_QUEENS_ = []  # Contains [i,j] of all the queens placed...

def pop():
    global _QUEENS_
    if len(_QUEENS_) > 0:
        del _QUEENS_[-1]
    return
def push(i,j):
    global _QUEENS_
    print "Pushing Queen at: ", i, j
    _QUEENS_.append([i,j])
    return


def Diagonal1(x, y, i, j, n):
    print "For Queen at: ", x, y
    ans = True
    if x > y:
        print "X > Y"
        xt = x - y
        xb = n - 1
        yt = 0
        yb = n - 1 - (x - y)

    elif x == y:
        print "X == Y"
        xt = 0
        xb = n - 1
        yt = 0
        yb = n - 1 
            
    elif x < y: # Clear
        print "X < Y"
        xt = 0
        xb = n - 1 - (y - x)
        yt = y - x
        yb = n - 1
    Done = True
    p = xt
    q = yt
    print "Xt: ", xt, "Xb: ", xb 
    print "Yt: ", yt, "Yb: ", yb 
    
    while p <= xb and q <= yb:
        print "P: ", p
        print "Q: ", q
        if p == i and q == j:
            print "p = i and q = j: Lies on Diag 1 of this Queen"
            return False
        p += 1
        q += 1
    
    return ans

def Diagonal2(x, y, i, j, n):
    ans = True
    Diag_list = [[0,0] for d in range((2*n)-1)]
    print Diag_list
    for r in range(n):
        Diag_list[r][1] = 0
        Diag_list[r][0] = r
        if r == n-1:
            s = 1
            while s < n:
                Diag_list[r+s][0] = n-1
                Diag_list[r+s][1] = s
                s += 1
    print "Diag_list: ", Diag_list    
    #Diag_list = [[0,0], [1,0], [2,0], [3,0],[4,0],[5,0],[6,0],[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]]
    
    xb = Diag_list[x+y][0]
    yb = Diag_list[x+y][0]
    xt = Diag_list[x+y][1]
    yt = Diag_list[x+y][1]
    
    p = xb
    q = yt
    
    print "Xt: ", xt, "Xb: ", xb 
    print "Yt: ", yt, "Yb: ", yb
    
    
    while p >= xt and q <= yb:
        print "P: ", p
        print "Q: ", q
        if p == i and q == j:
            print "p = i and q = j: Lies on Diag 2 of this Queen"
            return False
        p -= 1
        q += 1
    return ans


def isSafe(i,j, n):
    global _QUEENS_
    print "For i: ", i, " and j: ", j
    ans = True
    if len(_QUEENS_) == 0:
        return ans
    
    for Q in _QUEENS_:
        if Q[0] == i or Q[1] == j:
            return False
    for Q in _QUEENS_:
        if not Diagonal1(Q[0], Q[1], i, j, n):
            return False
        elif not  Diagonal2(Q[0], Q[1], i, j, n):
            return False
#     x = random.random()        # Used this code to generate random places for Queens..
#     if x > 0.50:
#         ans = True
#     else:
#         ans = False
    return ans

def firstQueen(x,y):
    global _QUEENS_
    print "First Queen is at: ", x, y
    _QUEENS_ = []
    print _QUEENS_
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
            print "Board after New 1st Queen:"
            displayBoard(n)
            for i in range(n):
                for j in range(n):
                    if [i,j] not in _QUEENS_:
                        if isSafe(i, j, n):
                            push(i,j)
                            print "Board:"
                            displayBoard(n)
                            if len(_QUEENS_) == n:
                                print "Solution Reached: "
                                displayBoard(n)
                                return
    print "Solution could not be reached. Some logical error in the code."            
    
def main():    
    n = int(raw_input("Enter an integer for the value of N"))
    
    Solution(n)
    
    
    
    
    
    return 0

if __name__ == '__main__':
    main()
        

