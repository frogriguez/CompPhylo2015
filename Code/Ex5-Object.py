"""
Zachary Rodriguez
CompPhylo 2015
Ex5 - Continuous MC using Objects
02/24/2015

Goals: Run continuous Markov Chains using object-oriented python scripts.
(1) estimate likelihood scores
(2) estimate branch lengths from marginal probs
(3) Calculate ML
"""



#Imports
import numpy as np
import random
from collections import Counter
from scipy.linalg import expm

#first define a class for continuous Markov Chain
class markov(object):
	def __init__(self, bases = ['A','C','G','T'], 
				Q = [[-1.916, 0.541, 0.787, 0.588],
				     [0.148, -1.069, 0.415, 0.506],
                            [0.286, 0.170, -0.591, 0.135],
			           [0.525, 0.236, 0.594, -1.355]],
                       v = 0.5, nsims = 100):
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
	
	def dsample(self, row):
		#multiplies each element in list by -1 if element < 0		
		probs = [x if x > 0 else -x for x in row]
		print ("probs:", probs)
		#creates cumulative list (cumprobs) from old list (row)
		cumprobs = np.cumsum(probs)
		print ("cumprobs:", cumprobs)
		tot = cumprobs[-1]
		num = random.uniform(0.0,tot) #samples from cum list
		print ("random number:", num)
		#goes to next element (x) in list (cumprobs) if statement is true (x > num)
		#& returns it's index (next() function)
		index = next(x[0] for x in enumerate(cumprobs) if x[1] > num)
		print ("index:", index, "base:", self.bases[index])
		return self.bases[index]
	
	"""
	This function initiates a continuous Markov Chain, 
	continuing to sample nucleotides as long as the defined branch length is not exceeded
	"""
class cMC(markov):
	def sim(self):
		piQ = self.margprob(100)    #Calculates stationary rate matrix
		for x in range(self.nsims):
			states = []
			self.times = []
			i = self.dsample(piQ[0])    #Samples i from stationary matrix
			states.append(i)
			time = random.expovariate(-1/self.Q[self.bases.index(i)][self.bases.index(i)])
			self.times.append(time)
			#print ("Current Time:",time)
			while sum(self.times) < self.v:	
				i = states[-1]
				idex = self.bases.index(i)
				#samples random time from exp dist with mean of diagonal value
				time = random.expovariate(-1/self.Q[self.bases.index(i)][self.bases.index(i)])
				print ("Current Time:",time)
				#draw next nt from row of curr nt. in rate matrix (Q)
				
				#margprob(time) or margprob (v) or rate matrix?
				j = self.dsample(self.Q[idex])
				states.append(j)
				self.times.append(time)
			self.chain.append(states)
		return self.chain
	
	"""
	This function Calculates the likelihood of a sequence 
	of base pair changes, for a given branch length (v)
	"""
	
	def lseq(self,v):
		vals = []	
		seq = self.chain[0]
		for element in seq[1:]:
			edex = seq.index(element)			
			i =	seq[edex-1]
			idex = self.bases.index(i)
			jdex = self.bases.index(element)		
			vals.append(self.margprob(v)[idex][jdex])
		lcurr = 1
		for Pij in vals:		
			lcurr *= Pij
		return lcurr
	
	"""
	This function will take a probability (p) as an argument and calculate its likelihood score.
	Next, it will increment & decrement the probability by a defined step (d), then calculate the likelihood of each.
	Finally, it will return the probability with the highest likelihood score of the 3.
	"""
	def step(self,v,d):
		#Caclulates marginal prob of i-->j	 at some arbitrary time (v) in the future	
		lcurr = self.lseq(v)
		
		vup = v + d
		lup = self.lseq(vup)
		
		vdwn = v - d
		ldwn = self.lseq(vdwn)
		if lup > lcurr:
			v = vup
		elif ldwn > lcurr:
			v = vdwn
		else:
			v=v
		
		return v

	"""
	This 'hillclimb' function takes 3 arguments: branch lenfth seed, step (diff), and a threshold (thresh)
	and returns the branchlength (vcurr) with the highest probability within your decimal constraint (thresh)
	given the starting (i) and ending (j) states of a sequence of nt changes
	"""	

	def blength(self,seed=random.random(),diff=0.01,thresh=0.000001):
		vcurr = round(seed,2)
		print ("seed:", vcurr)
		while diff > thresh and vcurr < 25.0:
			lcurr = self.lseq(vcurr)
			#if likelihood of current v < new v, set new v as current v & increase the step by 2x	
			vnew = self.step(vcurr,diff)			
			if lcurr < self.lseq(vnew):
				vcurr = vnew					
				diff *= 2			#if likelihood of current v > new v, divide step by 2 and re-try
			else:	                      
				diff /= 2
			print ("current branch length:",vcurr,"current likelihood:",lcurr, "current diff:",diff)
		return vcurr
	
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

#model = cMC(nsims = 1, v = 5)
#chain = model.sim()
#print ("chain:",chain)
#chain = model.sim("T")
#model.substitutions()
#print (model.sample("T"))
#print (model.cMC(i="T"))
#print ("branchlength given chain of sequence changes:",model.blength())

model = cMC(nsims = 1)
#model.chain = [["A","C","T","A","G"]   #Troubleshoot
blengths = []
#for x in range (100):
#	chain = model.sim()
# 	blengths.append(model.blength())

#blengths.append(model.blength())
print ("estimated branchlengths:",blengths)

chain = model.sim()
print ("Chain:",chain)
blengths = []
blengths.append(model.blength())
print ("estimated branchlengths:",blengths)