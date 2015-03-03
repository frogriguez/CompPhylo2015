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
import scipy as sp
from scipy.stats import binom
from scipy.linalg import expm
from scipy.stats import expon

#first define a class for continuous Markov Chain
class contMarkov(object):
    def __init__(self, bases = ['A','C','G','T'],
					#From Huelsenbeck 2015
					Q = [[-1.916, 0.541, 0.787, 0.588], 
						[0.148, -1.069, 0.415, 0.506], 
						[0.286, 0.170, -0.591, 0.135], 
						[0.525, 0.236, 0.594, -1.355]],
					v = 1.0, nsims = 1000):	
                                 
		self.bases = bases	#sets state space (nucleotides)
		self.Q = Q      #sets rate matrix
		self.v = v      #time being looked at (branch length)
		self.chain = {}	#list to hold states from Markov chain
		self.times = {}	#list to hold amount of time until state change
		self.nsims = nsims		#why is this not self?
		for base in bases:
			row = Q[sequence.index(base)]
			diag[base] = -1*min(row)
			values[base] = [x/(min(row)*-1) for x in row]
		self.values = values
		self.diag = diag
		runQT = self.calcMargProb()
		self.statfreq = runQT[0]
	
	def sim (self,index,):
		
	
	
	
	
	
	
	
	