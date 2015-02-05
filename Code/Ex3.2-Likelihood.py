"""
CompPhylo2015
Ex3 - Intro To Likelihood (II)
03 Feb 2015
Zachary Rodriguez
"""


"""
For this excercise we will implement a hill climbing method to find the ML of a parameter, in this case p = prob
"""

#My Imports
import scipy
from scipy.stats import binom
from numpy import random
import math
import cmath #complex math for floats
import matplotlib.pyplot as plt


#Calculates the Binomial Coefficient (n choose k)
def bincoef(n,k):
	total = 1
	n = int(n)
	k = int(k)
	for num in range((n-k),(n+1)):	#iterates through range backwards
		total *= num 
	bcf = total/math.factorial(k)
	#print ("Your binomial coefficient is:",bcf,"given (",n,"choose",k,")")
	return bcf

#Calculates the Binomial PMF
def bpmf(n,k,p):
	bc = bincoef(n,k)
	pmf = bc*pow(p,k)*pow(1-p,n-k)
	#print ("Your binomial pmf is:",pmf,"given",n,"trials,",k,"successes and a probability of:",p)
	return pmf
	
#Calculates the Likelihood
def likelihood(n,k,p):
	bc = bincoef(n,k)
	pmf = bc*pow(p,k)*pow(1-p,n-k)
	#print ("Your binomial pmf is:",pmf,"given",n,"trials,",k,"successes and a probability of:",p)
	return pmf

#Calculates likelihood scores (MAYBE?)
"""
ON LIKELIHOOD SCORE
I am still super confused if we need include the binomial coefficient
I have found several examples online that only calculate the maximum likelihood, (not the LRT)
and do not include the binomial coefficient. (http://nbviewer.ipython.org/github/melund/Python-for-Signal-Processing/blob/master/Maximum_likelihood.ipynb)
I realize that the ML score itself is not important since it's relative anyway, but still..
"""

def likelihood2(n,k,p):
	pmf = bpmf(n,k,p)
	bc = bincoef(n,k)
	l = pmf/bc
	#print ("Your Likelihood score for p =",p,"is:",l,",given",n,"trials and",k,"successes")
	return l

"""
#calculates maximum likelihood from a list of probabilities
def ML(n,k,p,list):
	[lscores.append(likelihood(n,k,p)) for k in list]	#calculates likelihood score for each value
	maxl = max(lscores)
	lindex = lscores.index(maxl)
	maxp = p_list[lindex] 
	for l in lscores:
		LR = l/maxl
		lratios.append(LR)
	maxlr = lratios[lindex]
	#print ("Given (",n,") trials and (",k,") successes,/nYour probability:",maxp,"\nYour ML is:",maxl,"Your ML:","\nYour LR is:",maxlr)
	return lscores,maxl,lratios,maxlr,maxp
"""

"""
This function will take a probability (p) as an argument and calculate its likelihood score.
Next, it will increment & decrement the probability by a defined step (d), then calculate the likelihood of each.
Finally, it will return the probability with the highest likelihood score of the 3.
"""

def step(n,k,p,d):
	l = likelihood(n,k,p)
	pup = p + d
	lup = likelihood(n,k,pup)
	pdwn = p -d
	ldwn = likelihood(n,k,pdwn)
	if lup > l:
		p = pup
	elif ldwn > l:
		p = pdwn
	else:
		p = p
	return p

"""
This 'hillclimb' function takes 2 parameters: #trials (n), number of successes (k)
and 3 arguments: probability seed (p), step (d), and a constraint (c)
and returns the highest likelihood (& its prob) within your decimal constraint (+/- c)
"""

def hillclimb(n,k,seed=random.random(),d=0.1,c=0.00001):
	pcurr = round(seed,2)
	lcurr = likelihood(n,k,pcurr)
	#print ("Probability Seed:",pcurr,"\nLikelihood of seed:",lcurr)
	while d > c:		#This loop will run while the increment/decrement step < given decimal
		lcurr = likelihood(n,k,pcurr)	#calculates likelihood of current probability
		if lcurr < likelihood(n,k,step(n,k,pcurr,d)):	#checks if likelihood of new, optimized probability is > likelihood of current prob
			pcurr = step(n,k,pcurr,d)					#if new > current, new replaces current
			d *= 2										#step is multiplied by 2
		else:	#if likelihood of current > new, optimized probability, decrease step by 2 and re-try
			d /=2
		#print ("\nCurrent prob:",pcurr,"\nCurrent step size:",d)
	#print ("Here are your results given (",n,") trials and (",k,") successes:\nOptimized probability:",pcurr)
	return lcurr,pcurr

#hillclimb(100,1)

"""
This function takes a number of trials (n), a probability (truep), and draws a random
number of successes (k) from a binomial distribution. It then uses a hill-climbing
method to estimate the probability with the Maximized likelihood. 
This simulation runs a simulation (s) number of times, and creates a null distribution of
Likelihood ratios, returning the likelihood ratios that lie in the 95% interval of the distribution.
"""

def sim(n=200,truep=random.random(),s=1000):
	truek = n*truep		#calculates the "true" number of successes
	
	LRs,LRTs = [],[]
	for x in range(0,s+1):	#this function runs (s) # of times
		k = binom.rvs(n,truep)	#draws #successes (k) from a binomial distribution
		L = likelihood(n,k,truep)	#calculates the "true" likelihood
		ML,_ = hillclimb(n,k)	#hillclimb estimate, returns ML
		LR = L/ML				#Calculates Likelihood ratio (LR), appends to list
		LRs.append(LR)
	
	#generates list of LR test statistics [-2ln(LR)] from list of LRs
	LRTs = list(map(lambda x: (-2)*math.log(x),LRs))	
	LRs = sorted(LRs)			
	index = round(len(LRs)*.95)	#finds index of the LR lying at the 95% interval
	LRreject = LRs[index]	
	LRTs = sorted(LRTs)
	LRTreject = LRTs[index]
	#return LRreject,LRTreject
	print("LRs: ",LRs,"\n\n\n\nLRTs: ",LRTs)
	return LRs,LRTs

def graph(x):
	plt.hist(x,bins = 25)
	plt.xlabel("Likelihoods")
	plt.ylabel("LRT scores")
	plt.show()

LRs,LRTs = sim(n=200,truep=0.5)
index = round(len(LRs)*.95)	#finds index of the LR lying at the 95% interval
LRreject = LRs[index]	
LRTs = sorted(LRTs)
LRTreject = LRTs[index]
print(LRreject,LRTreject)
graph(LRTs)
	
	
