"""
CompPhylo2015
Ex3 - Intro To Likelihood
29 Jan 2015
Zachary Rodriguez
"""

#My Imports
import scipy
from scipy.stats import binom
from numpy import random
import math
import matplotlib.pyplot as plt

"""
This function takes the number of trials as an argument (n),
assigns a random probability, then draws from a binomial distribution based on (n,p) 
then queries the user to estimate the prob, based on # of successes (k)
"""

#This function takes a random prob, samples from a binomial dist, and prompts the user to guess the p value based on success.
def in_class(n=5,p=0.5):
	p = random.random()	#gives (p) a random value between 0 & 1
	k = binom.rvs(n,p)	#draws from a binomial distribution based on (n,p), returns # of successes
	print ("For (",n,") trials, the number of successes was:",k)
	guess = float(input("What do you think the probability was?"))	#queries the user for a guess
	if guess > 1:
		guess /= 100
	else:
		guess = guess
	error = 100*(abs(p-guess)/p)
	if error < 5:
		print ("Sweet! The probability was:",p,"\nYou're %error was:",error,"\nGo Buy a lotto ticket!")
	elif error < 20:
		print ("So Close! The probability was:",p,"\nYou're %error was:",error,"\nYou should try again.")
	else:
		print ("womp womp... The probability was:",p,"\nYou're %error was:",error,"\nBetter luck next time!")

#This function sets up a list of probabilities from 0 -> 1 over a defined interval
def probs(step=0.05):
	p_list = []
	p = 0
	while p <= 1.001:		#range function doesn't take floats
		p_list.append(p)
		p += step
	#print("Here is your list of probabilities:",[print (p) for p in p_list])
	return (p_list)
		
"""
#a calculation necessary for the binomial coefficient
def multiply(min=1, max=10):
	total = 1
	for num in range(max,min-1,-1):	#iterates through range: max -> min, stepping -1 each time
		total *= num
	return (total)
"""

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

#These Are Tests----------------
#in_class(100)
#probs()
#bpmf(5,1,.5)
#likelihood(5,1,.5)
#ml(100,20)

"""
this bit of code is not working, cuz zeros n stuff
def loglihood(lscores):
	logs = []
	for l in lscores:
		log = math.log(l[10])
		logs.append(log)
	print ("Here is your list of loglihoods:",logs)
"""
#Plots probabilities & likelihood values
def graph(x,y):
	plt.plot(x, y)
	plt.xlabel("Probabilities")
	plt.ylabel("Likelihoods")
	plt.show()
	

lscores,maxl,lratios,maxlr,maxp = ml(5,4)
x = probs()
y = lratios
graph(x,y)
#loglihood(lscores)











