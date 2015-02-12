"""
Zachary Rodriguez
CompPhylo 2015
Ex4.2 - In Class Markov Chain Exercise
02/10/2015
"""

#Imports
import numpy as np
import random
#import scipy U(0,1)

"""
This function takes the index (0,1) of the element, looks down the 
corresponding row, and returns a new state based on a random sample from
the probabilities. 
"""

def sample(index,states,matrix):
	num = random.random()
	
	#assigns a row in the matrix, according to the index of the state space
	row = matrix[index]	
	
	#creates cumulative list (cumprobs) from old list (row)
	cumprobs = np.cumsum(row)	
	
	#goes to next element (x) in list (cumprobs) if statement is true (x > num)
	#& returns it's it's index (next() function)
	index = next(x[0] for x in enumerate(cumprobs) if x[1] > num)
	
	#print("probs:",row,"cumprobs: ",cumprobs,"chosen state: ",states[index])	#Check
	return states[index]
	
	
"""
This function takes number of steps (n), list of states (states),
and a conditional probability matrix (matrix), samples from the matrix (sample)
and appends the value to a list (n) number of times.
"""

def markov(s,states,matrix):
	chain = [random.choice(states)]	#creates random seed by picking random element from list of states
	print ("seed:",chain)
	
	#takes the last element in list "chain" and returns it's index from states
	#& appends new sample (see above) in chain, (n) number of times
	[chain.append(sample(states.index(chain[-1]),states,matrix)) for x in range(s)]	
	return chain

"""
This function converts your original matrix into a numpy matrix,
which can perform transitional matrix multiplication.
"""
def nstep(matrix,i,j,s):
	matrix = np.matrix(matrix)
	stepmat = matrix**(s) #not sure if this function includes zero (0)
	print (s,"- step probability matrix:",stepmat)
	return (stepmat[i][j])
	
	
	
probmat = [[0.7,0.3],[0.5,0.6]]	#creates 2x2 matrix of probabilities for row 'A' and row 'B'

states = ("A","B")

#simulate 1 chain of 3 steps:
s = 3
chain = (markov(s,states,probmat))
print ("You're chain of",s,"steps:",chain)

#calculate n-step transitional probability:

ival = chain[0]
i = states.index(ival)

jval = chain[s-1]
j = states.index(jval)

print("i=",i,"j=",j)

prob = nstep(probmat,i,j,s)
print("Probability that j =",jval,"in",s,"steps, given that i =",ival,"is:",prob)






	











