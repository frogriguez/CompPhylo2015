"""
Practice Different Functions
"""

import math
import numpy as np
import random
import numpy as np
import random
import scipy as sp
from scipy.stats import binom
from scipy.linalg import expm
from scipy.stats import expon
from collections import Counter

"""
#Practice Round
rando = random.random()
round0 = round(rando)
round1 = round(rando,1)
round2 = round(rando,2)
round3 = round(rando,3)
print(rando, round0, round1, round2, round3)
"""

"""
#practice lambda

#lambda syntax:  lambda arugument_list: expression
x,y = [1,2,3],[4,5,6]
lambda x, y : x + y

#assign a function with lambda to call later:
sum = lambda x, y : x + y

#Try map() function:
#syntax: result = map(function,sequence_list)

list = [1,2,3]
def add_one(x)
	return x+1
r = map(add_one,

#use map + lambda:
listold = []
[listold.append(x) for x in range (0,10)]
def multiply(x):
	return x*2
#listnew = map(lamda x: x*2,listold)
listnew = list(map(lambda x: multiply(x),listold))	#use list() function to create a new list (Python 3+)

print (listold,listnew)
"""

"""
#practice list
matrix = [[0.4,0.6],[0.3,0.7]]
print (matrix[0])
"""

"""
#Practice enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list = list(enumerate(seasons))
print(list)

#Practice Next:
list = [0,1,2,3,4,5,6,7,8,9,10]
print(next(x[0] for x in enumerate(list) if x[1] > 5))
"""

"""
#practice matrices

v = 0
Q = [[-1.916, 0.541, 0.787, 0.588], 
	[0.148, -1.069, 0.415, 0.506], 
	[0.286, 0.170, -0.591, 0.135], 
	[0.525, 0.236, 0.594, -1.355]]
Q = np.matrix(Q)
#probmat = ratemat**(2)
probmat = expm(Q * v)
print(probmat)


class contMarkov(object):
	def __init__(self, bases = ['A','C','G','T'], Q = [[-1.916, 0.541, 0.787, 0.588],[0.148, -1.069, 0.415, 0.506],[0.286, 0.170, -0.591, 0.135],[0.525, 0.236, 0.594, -1.355]],v = 1.0, nsims = 1000):	
		self.Q = Q
		self.v = v
		
	
	#Calculate marginal probabilities of rate matrix
	def margprob(self):
		ratemat = np.matrix(Q)
		probmat = expm(ratemat * v)
		return probmat
model = contMarkov()
print (model.margprob())


list1 = ['c', 'a','a', 'b', 'c', 'a', 'b', 'c', 'a', 'b','c', 'a']
list2 = ['c', 'a','a', 'b', 'c', 'a', 'b', 'c', 'a', 'b','c', 'a']
list3 = [i+j for i,j in zip(list1, list2)]
counter = Counter(list3)
print (counter)
temp,dlist = [],[]
for key, value in counter.items():
    temp = [key,value]
    dlist.append(temp)
dlist.sort()
print (dlist)

"""
row = [-1.916, 0.541, 0.787, 0.588]
probs = [x if x > 0 else -x for x in row]
print ("probs",probs)

#creates cumulative list (cumprobs) from old list (row)
cumprobs = (np.cumsum(probs))
print("cumprobs",cumprobs)

tot = cumprobs[-1]
print ("total",tot)
num = random.uniform(0.0,tot)
print ("randomnum",num)
	
#goes to next element (x) in list (cumprobs) if statement is true (x > num)
#& returns it's index (next() function)
index = next(x[0] for x in enumerate(cumprobs) if x[1] > num)	
print ("index",index)