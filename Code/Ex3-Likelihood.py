"""
CompPhylo2015
Ex3 - Intro To Likelihood
29 Jan 2015
Zachary Rodriguez
"""

#My Imports
from scipy.stats import binom


#1
#Calculates the Binomial Coefficient (n choose k)
def bcoef(n,k):
	bcf = multiply((n-k+1),n)/multiply(max=k)
	return bcf

#Calculates the Binomial PMF
def bpmf(n,k,p):
	bcf = bcoef(n,k)
	pmf = bcf1*pow(p,k)*pow(1-p,n-k)
	return (pmf)
	
#This function sets up list of probabilities from 0 ->1, over a defined interval:
def probs(step=0.05)
	p_list = []
	for p in range(0,1,step):
		p_list.append(p)
	print ("Here is your list of probabilities:",p_list,"\n")	#This is a check
	return p_list

probs()	#Executes list

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)