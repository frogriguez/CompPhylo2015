"""
CompPhylo2015
Ex3 - Intro To Likelihood
29 Jan 2015
Zachary Rodriguez
"""

#My Imports



#1
def bpmf(n,k,p):
	bcf1,elapsed = bcf_easy(400,2)
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
