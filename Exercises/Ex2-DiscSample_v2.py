"""
Zachary Rodriguez
CompPhylo 2015
Exercise 2 - Discrete Sampling Practice v2
01-26-15
"""

#MY imports
import time
import random
import matplotlib.pyplot as plot

#This function will multiply a range of numbers together in decreasing order
#sets the defaults min (1) and max (10) if no arguments are given
def multiply(min=1, max=10):
	total = 1
	for num in range(max,min-1,-1):	#iterates through range: max -> min, stepping -1 each time
		total *= num
		#print("Current Number:",num,"Current Total:",total)	#This is a check
		if total == 0:
			print("Idiot Check: your range includes zero,/n therefore, your total is zero")
	return (total)	

multiply(5,8)

#This theorem calculates the BCF, less computationally expensive
def bcf_easy(n,k):
	start = time.time()	#sets variable 'start' as the current time
	bcf = multiply((n-k+1),n)/multiply(max=k)
	end = time.time()	#sets variable 'end' as the current time
	elapsed = end - start	#calculates elapsed time
	return bcf,elapsed

#This theorem is more computationally expensive by calculating 3 factorials
def bcf_hard(n,k):
	start = time.time()	#sets variable 'start' as the current time
	bcf = multiply(max=n)/(multiply(max=n-k)*multiply(max=k))
	end = time.time()	#sets variable 'end' as the current time
	elapsed = end - start	#calculates elapsed time
	return bcf,elapsed

#print ("your bcf:",bcf(1000,2))	#Check bcf
	
bin_coef,elapsed = bcf_easy(10000,2)	
print ("You're coefficient the easy way:",bin_coef,"Elapsed Time:",elapsed)

bin_coef,elapsed = bcf_hard(10000,2)
print ("You're coefficient the hard way:",bin_coef,"Elapsed Time:",elapsed)


"""
(3) Results:
I can see why bcf is less computationally expensive, by only calculating the necessary (2)
factorials, where bcf_full would have to calculate each factorial, then do division. When I ran both programs
with "n choose k: (100,000:2)", the bcf was noticeably faster (~10 seconds). Larger numbers
maxed out both programs (500,000 choose 2). 
"""
#This function calculates the binomial PMF, when passed 
#	n (sample size), k (# of successes), and p (probability of each success)
def bin_pmf(n,k,p):
	bcf1,elapsed = bcf_easy(400,2)
	pmf = bcf1*pow(p,k)*pow(1-p,n-k)
	return (pmf)

#This function takes 2 lists, picks a random event, and prints the event name, with its probability
def sample(events,probs):
	sample = random.choice(events)	#selects a random event from list 'events'
	sampleid = events.index(sample)	#returns index of randomly sampled event
	event = events[sampleid]		#returns string representation of chosen event
	prob = probs[sampleid]			#returns probability associated with event
	print ("\nThe probability of you owning a",event,"is",prob)

#This block of code generates a string from random strings
words = ['frog','cat','dog']
events =  [x + y for x in words for y in words]
probs = []
for x in events:	#generates a random probability for each element in the list 'events'
	probs.append(random.random())

sample(events,probs)

"""
UPDATE:
THE DELETED FUNCTIONS were a convoluted way of approaching the problem.
I REALIZE now that I only need to calculate probability, not generate the actual sequences.
"""

#This function samples a random type with p=0.5, 400x
#	then stores the number of successes of each type (k1 & k2)
def assign():
	k1,k2 = 0,0
	for x in range(0,400):
		num = random.random()	#draws a random float from 0->1
		if num < 0.5:
			k1 += 1
		else:
			k2 += 1
	return (k1,k2)

#This function will calculate total number of successes of type1
	#	& type2 bases in the sequence 100x--then store them in a list
def freq(trials):
	type1,type2 = [],[]
	for x in range(0,trials):
		k1,k2 = assign()
		type1.append(k1)    #Passing the actual number of k's, not proportion
		type2.append(k2)		#don't divide by 400
	return (type1,type2)

#list1,list2 = freq(100)
#print ("\nProportions of type1:",list1,"\n\n Proportions of type2:",list2)

#This function calculates the PMF of each proportion (k = # of successes)
#	in the list received in the freq function, using p=0.5 & n=400
def calc(trials):
	pmf_list = []
	k1,k2 = freq(trials)
	for k in k1:
		pmf = bin_pmf(400,k,0.5)
		pmf_list.append(pmf)
	return (pmf_list)

def histo(trials):
	successes = calc(trials)
	plot.hist(successes, bins=trials)
	plot.xlabel("Number of type 1 successes")
	plot.ylabel("Probability")
	plot.show()

trials = input("Please enter number of trials. Try 100 or 10,000\n")
trials = int(trials)
print ("\nPMF list:",calc(trials),"\n")
#histo(trials)
