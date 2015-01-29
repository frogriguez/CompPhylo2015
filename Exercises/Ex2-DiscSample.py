"""
Zachary Rodriguez
CompPhylo 2015
Exercise 2 - Discrete Sampling Practice
01-26-15
"""

#MY imports
import time
import random

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
#This function calculates the binomial PMF, not 100% understood
def bin(n,k,p):
	bcf1,elapsed = bcf_easy(400,2)
	bpmf = bcf1*pow(p,k)*pow(1-p,n-k)
	return (bpmf)

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

#This function generates a sequence from equal parts, type 1 & type 2
def seq_gen():
	ac,gt = ['A','C'],['G','T']
	seq = []
	for x in range(0,200):
		base = random.choice(ac)
		seq.append(base)
	for x in range(0,200):
		base = random.choice(gt)
		seq.append(base)
	return (seq)

print ("\nYour original sequence is:",seq_gen())
	
#This function generates a new sequence by sampling from another sequence
	#and returns the counts for the 2 types
def counts():
	type1,type2 = 0,0
	seq = seq_gen()
	new = []
	for x in seq:
		base = random.choice(seq)
		if base == 'A':		#an 'A' or 'C' counts as type 1
			type1 += 1
		elif base == 'C': 	
			type1 += 1
		else: 				#a 'G' or 'T' counts as type 2
			type2 += 1
		new.append(base)
	return (type1,type2,new)

print ("\nYour new seq:",counts())

#This function will calculate the proportion of type1
	#	& type2 bases in the sequence 100x--then store them in a list
def proportion():
	list1,list2 = [],[]
	for x in range(0,100):
		type1,type2,seq = counts()
		prop1 = type1/400
		list1.append(prop1)
		prop2 = type2/400
		list2.append(prop2)
	return (list1,list2)

list1,list2 = proportion()
print ("\nProportions of type1:",list1,"\n\n Proportions of type2:",list2)

def PMF():
	pmfs = []
	list1,list2 = proportion()
	for x in list1:
		pmf = bin(400,2,x)
		pmfs.append(pmf)
	return (pmfs)

print ("\nYour probabilities:",PMF())
