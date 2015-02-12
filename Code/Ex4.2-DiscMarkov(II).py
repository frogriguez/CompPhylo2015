"""
Zachary Rodriguez
CompPhylo 2015
Ex4 - Discrete Markov Chains
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

def markov(n,states,matrix):
	chain = [random.choice(states)]	#creates random seed by picking random element from list of states
	print ("seed:",chain)
	
	#takes the last element in list "chain" and returns it's index from states
	#& appends new sample (see above) in chain, (n) number of times
	[chain.append(sample(states.index(chain[-1]),states,matrix)) for x in range(1,n)]	
	return chain

matrix = [[0.25,0.25,0.25],[0.25,0.25,0.25],[0.25,0.25,0.25],[0.25,0.25,0.25]]	#creates 4x4 matrix of equal probabilities
print (matrix)

bases = ["A,T,C,G"]

[print ("\nChain #",i,markov(100,bases,matrix)) for i in range (0,100)]















