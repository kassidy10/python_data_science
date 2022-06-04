#Task
# given a list of numbers and the number of rows(r), rehshape
#the list into 2-dimensional array. Note that r divides the length of the list evenly

#input Format
# first line: an integer (r) indicating the number of rows of the 2-dimensional array
#Next line: numbers separated by the space

#Output Format
#An numpy 2d array of values rounded to the second decimal

#import necessary modules
import numpy as np

r = int(input())
lst = [ float(x) for x in input().split()]
arr = np.array(lst)

#perfect code
arr_new = arr.reshape(r,-1)
print(arr_new)

#print(np.round(arr.reshape(r,2), decimals = 2))
#arrS = arr.reshape((r,int(len(lst)/2)))

#print(arrS)