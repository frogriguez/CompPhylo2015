"""
Zachary Rodriguez
CompPhylo 2015
Ex5 - Continuous MC using Objects
02/24/2015

Goals: Run continuous Markov Chains using object-oriented python scripts.
(1) estimate likelihood scores
(2) estimate branch lengths
(3) Calculate ML
"""



#Imports
import numpy as np
import random
from collections import Counter
import scipy as sp
from scipy.stats import binom
from scipy.linalg import expm
from scipy.stats import expon

#first define a class for continuous Markov Chain
class contMarkov(object):
	def __init__(self, bases = ['A','C','G','T'], 
				Q = [[-1.916, 0.541, 0.787, 0.588],
				     [0.148, -1.069, 0.415, 0.506],
                            [0.286, 0.170, -0.591, 0.135],
			           [0.525, 0.236, 0.594, -1.355]],
                       v = 1.0, nsims = 100):
		self.bases = bases	#sets state space (nucleotides)
		self.Q = Q      #sets rate matrix
		self.v = v      #time being looked at (branch length)
		self.chain = []	#list to hold states from Markov chain
		self.times = []	#list to hold amount of time until state change
		self.nsims = nsims	
		self.bases = bases
	
	
	
	#Calculate marginal probabilities of rate matrix
	def margprob(self,v):
		ratemat = np.matrix(self.Q)
		probmat = expm(ratemat * v)
		return probmat
	"""
	This function takes the index (0,1,2,3) of the nucleotide, looks down the 
	corresponding row, and returns a new state based on a random sample from
	the probabilities. 
	"""	
	def sample(self,base):
		row = self.Q[self.bases.index(base)]
		lamb = min(row)*-1
		beta = 1/lamb
		time = random.expovariate(beta)
		
		num = random.random()
			
		#assigns a row in the matrix, according to the index of the nucleotide
		probmat = self.margprob(self.v)
		row = probmat[self.bases.index(base)]
			
		#creates cumulative list (cumprobs) from old list (row)
		cumprobs = np.cumsum(row)	
			
		#goes to next element (x) in list (cumprobs) if statement is true (x > num)
		#& returns it's it's index (next() function)
		index = next(x[0] for x in enumerate(cumprobs) if x[1] > num)
		return self.bases[index],time
	
	"""
	This function initiates a Markov Chain, continuing to sample nucleotides as long as the defined branch length is not exceeded
	"""
	def MC(self,i):
		states = []	
		states.append(i)
		elapsed = 0.0
		while elapsed < self.v:
			i = states[-1]
			j,vcurr = self.sample(i)
			states.append(j)
			elapsed += vcurr	
		return states
	
	def simulation(self,i):
		[self.chain.append(self.MC(i)) for x in range(self.nsims)]
		return self.chain
	
	def substitutions(self):
		ilist,jlist,freqs,temp = [],[],[],[]
		
		#creates lists for initial (i) and ending (j) states		
		for subs in self.chain:
			i,j = subs[0],subs[-1]
			ilist.append(i)
			jlist.append(j)		
		
		#Zips elements from both lists together (ilist("A") & jlist('T') --> combined_list("AT")
		subs = [x+y for x,y in zip(ilist, jlist)]
		counter = Counter(subs) #Creates dictionary of keys (ij's) & values (tallies)
		print (counter)
		subs = []
		for key,value in counter.items():   #creates list from dictionary
			temp = [key,value]
			subs.append(temp)
		subs.sort()
		[freqs.append(k[1]) for k in subs]    #Makes a list from the 2nd element in each list 
		print (freqs)
		freqs = [k/self.nsims for k in freqs]	#divides each element by number of simulations
		print (freqs)
		freqs = [freqs[x:x+4] for x in range(0,len(freqs),4)]    #Creates sublist for every 4 values
		print (freqs)
		return freqs
model = contMarkov(nsims = 1000)
chain = model.simulation("T")
model.substitutions()
#print (model.sample("T"))
#print (model.MC(i="T"))
