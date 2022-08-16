#  File: Spiral.py

#  Description: This program will create a spiral of numbers in increasing order
#  starting with 1 at the center and be a nxn grid. Then the program outputs the
#  sum of adjacent numbers when given a number inside the spiral. 1 is adjacent
#  to 2, 3, 4, 5, 6, 7, 8, 9 and the sum of those excluding 1 is 44.

#  Student Name: Cody Hayes

#  Student UT EID: cmh 5538 

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6-4-22

#  Date Last Modified: 6-5-22

#  Input: 11
#         1
#         42
#         110
#         91
#  Output: 44
#          382
#          477
#          239
import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):
    if (n % 2 == 0): #creates an odd number to construct the spiral 
        n = n + 1
        
    num = 1
    blank = [[0 for x in range(n)] for y in range(n)] #creates blank spiral
    r = int(n/2)
    c = int(n/2)
    blank[r][c] = num
    step = 1

    while(num < n**2):
        for i in range(step):
            num = num + 1
            r,c = move_right(r,c)
            blank[r][c] = num
        if (num == n**2):
            break
        elif(num !=2):
            num = num + 1
            r, c = move_right(r,c)
            blank[r][c] = num
            step = step + 1
            
        for i in range(step):
            num = num + 1
            r, c = move_down(r,c)
            blank[r][c] = num
            
        step = step + 1

        for i in range(step):
            num = num + 1
            r,c = move_left(r,c)
            blank[r][c] = num

        for i in range(step):
            num = num + 1
            r, c = move_up(r, c)
            blank[r][c] = num 
    
    return blank

def move_right(x,y):
    y =  y + 1
    return x, y

def move_down(x, y):
    x = x + 1
    return x, y

def move_left(x, y):
    y = y - 1
    return x, y

def move_up(x,y):
    x = x - 1
    return x,y
    
    
    ''' right, down, left left, up up, right right right, down
down, down, left left left left, up up up up, right right right right right

'''
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    if( n <= 0 or n > spiral[0][-1]):
        return 0
    r = 0
    for row in spiral:
        if(n in row):
            index = row.index(n)
            break
        r = r + 1
    #(r, index)

    adj = []
    if(r == 0 and index == 0):
        x,y = move_right(r, index)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    elif(r == 0 and index == len(spiral[0]) - 1):
        x,y = move_left(r, index)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_right(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    elif(r == len(spiral[0]) - 1 and index == 0):
        x,y = move_right(r, index)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    elif(r == len(spiral[0]) - 1 and index == len(spiral[0]) - 1):
        x,y = move_left(r, index)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        x,y = move_right(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    elif(r == 0):
        x,y = move_right(r, index)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    elif(r == len(spiral[0]) - 1):
        x,y = move_right(r, index)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    
    elif(index == 0):
        x,y = move_up(r, index)
        adj.append(spiral[x][y])

        x,y = move_right(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ

    elif(index == len(spiral[0]) - 1):
        x,y = move_up(r, index)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_right(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    else:
        x,y = move_up(r, index)
        adj.append(spiral[x][y])

        x,y = move_right(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_down(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_left(x,y)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        x,y = move_up(x,y)
        adj.append(spiral[x][y])

        summ = sum(adj)
        return summ
    
def main():
    n = int(sys.stdin.readline().strip())
    
    spiral = create_spiral(n)

    input_ = sys.stdin.readlines()

    for line in input_:
        print(sum_adjacent_numbers(spiral, int(line)))
        
    


    
    #for row in spiral:
        #print(row)

    '''print(sum_adjacent_numbers(spiral, 1))
    print(sum_adjacent_numbers(spiral, 42))
    print(sum_adjacent_numbers(spiral, 110))
    print(sum_adjacent_numbers(spiral, 91))
    print(sum_adjacent_numbers(spiral, 200))'''
# read the input file

# create the spiral


# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()
