"""
CompPhylo2015
Ex3 - Intro To Likelihood (II)
03 Feb 2015
Zachary Rodriguez
"""

#My Imports
import scipy
from scipy.stats import binom
from numpy import random
import math
import matplotlib.pyplot as plt

#This function sets up a list of probabilities from 0 -> 1 over a defined interval
def probs(step=0.05):
	p_list = []
	p = 0
	while p <= 1.001:		#range function doesn't take floats
		p_list.append(p)
		p += step
	#print("Here is your list of probabilities:",[print (p) for p in p_list])
	return (p_list)

#Calculates the Binomial Coefficient (n choose k)
def bincoef(n,k):
	total = 1
	for num in range(n,(n-k),-1):	#iterates through range
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

#Calculates likelihood scores
def likelihood(n,k,p):
	pmf = bpmf(n,k,p)
	bc = bincoef(n,k)
	l = pmf/bc
	#print ("Your Likelihood score for p =",p,"is:",l,",given",n,"trials and",k,"successes")
	return l

#calculates maximum likelihood
def ml(n,k):
	lscores,lratios = [],[]
	p_list = probs()
	[lscores.append(likelihood(n,k,p)) for p in p_list]	#calculates likelihood score for each prob
	maxl = max(lscores)
	lindex = lscores.index(maxl)
	maxp = p_list[lindex] 
	for l in lscores:
		LR = l/maxl
		lratios.append(LR)
	maxlr = lratios[lindex]
	print ("Given (",n,") trials and (",k,") successes,/nYour probability:",maxp,"\nYour ML is:",maxl,"Your ML:","\nYour LR is:",maxlr)
	return lscores,maxl,lratios,maxlr,maxp
