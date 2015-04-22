"""
Exercise 6 - Creating and Using node and Tree Classes
@author: zachrodriguez
03-13-15
"""

# ---> Defining node and Tree classes <---


#--------------------------------------
# Imports
import numpy as np
import random
from scipy.linalg import expm
#from __future__ import print_function

#------------------------------------------------------------------
"""
ATTRIBUTES


"""

#-------------------------------------------------------------------------------------------------------------------
# Class Markov - a new class 

#import ctmc
# We'll need this later, I promise. It's always better to put import statements
# outside of class definitions. In fact, it's best to put them all at the top
# of a file. This imports the ctmc class that we previously defined.
#first define a class for continuous Markov Chain

class markov(object):
	def __init__(self, bases = ['A','C','G','T'], 
				Q = [[-1.916, 0.541, 0.787, 0.588],
				     [0.148, -1.069, 0.415, 0.506],
	                         [0.286, 0.170, -0.591, 0.135],
				     [0.525, 0.236, 0.594, -1.355]],
                       v = 10, seqlen = 10):
		self.bases = bases	#sets state space (nucleotides)
		self.Q = Q      #sets rate matrix
		self.v = v      #time being looked at (branch length)
		self.chain = []	#list to hold states from Markov chain
		self.times = []	#list to hold amount of time until state change
		self.seqlen = seqlen	
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
		#print ("probs:", probs)
		#creates cumulative list (cumprobs) from old list (row)
		cumprobs = np.cumsum(probs)
		#print ("cumprobs:", cumprobs)
		#maximum prob (tot) is the last value in the list		
		tot = cumprobs[-1]
		num = random.uniform(0.0,tot) #samples from cum list
		#print ("random number:", num)
		#goes to next element (x) in list (cumprobs) if statement is true (x > num)
		#& returns it's index (next() function)
		index = next(x[0] for x in enumerate(cumprobs) if x[1] > num)
		#print ("index:", index, "base:", self.bases[index])
		return self.bases[index]
	
#--------------------------------------------------------------------------------------------------------------------
# Class Continuous Markov - a class of class markov

class cMC(markov):

	def sim(self, seq1 = None, brl = None):
		
		"""
		This function initiates a continuous Markov Chain, 
		continuing to sample nucleotides as long as the defined branch length is not exceeded
		NEW: Option to pass a starting sequence
		"""	
		
		if brl is None:
			brl = self.v
		
		piQ = self.margprob(100)    #Calculates stationary rate matrix	
		seq2 = []	# creates a list for starting & ending states
		self.times = []	#empty list for storing wait times
		
		if seq1 is None or seq1 == []:
			# If MC is not passed a starting sequence, 
			# simulated one from the stationary distribution (PiQ)			
			seq1 = []
			for x in range(self.seqlen):			
				i = self.dsample(piQ[0])    #Samples initial state from stationary matrix
				seq1.append(i)
		
		# for each nucleotide (nt) in seq1		
		for i in seq1:			
			jlist = [i] # list to hold state changes for each nt in seq1, starts list with initial nt (i)
			idex = self.bases.index(i) # get's index of current state from "bases"
			self.times = []	#list to hold waiting time
			
			while sum(self.times) < brl:	#while the waiting time is less than the branch length
				
				# samples random time from exp dist with mean of diagonal value
				time = random.expovariate(-1/self.Q[self.bases.index(i)][self.bases.index(i)])
				self.times.append(time) 
				
				# If sampled time is less than branch length, perform a substitution					
				if sum(self.times) < brl:
					#samples next state (j) from row (i) in rate matrix (Q), appends to jlist
					j = self.dsample(self.Q[idex])
					jlist.append(j)
					#print("\n| Current time:",sum(self.times),"| Current bl:", brl,"| Substitution executed |")
			
			seq2.append(jlist[-1])	# Append last state in jlist to new sequence
		return seq2		
		
	
	def printseq(self, n1="seq1",n2="seq2",seq1 = None,seq2 = None):
		print ("Your nucleotide substitutions:",n1," --> ",n2)		
		for i in seq1:
			# get's current index in the sequence
			dex = seq1.index(i)
			print(" ",seq1[dex]," --> ",seq2[dex])	
	
	"""
	This function Calculates the likelihood of a sequence 
	of base pair changes, for a given branch length (v)
	"""
	
	def lseq(self,v):
		vals = []	
		for i in self.chain[0]:
			# get's current index in seq1
			dex = self.chain[0].index(i)
			
			# get's index of nucleotide in seq1 from "bases"			
			idex = self.bases.index(i)
			
			#get's nucleotide in seq2
			j = self.chain[1][dex]
			
			# get's index of nucleotide in seq2 from "bases"
			jdex = self.bases.index(j)	
			
			# appends marginal probability (Pij) to vals
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
		#Caclulates marginal prob of i-->j
		# at some time (v) in the future	
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

	def brlen(self,seed=random.random(),diff=0.01,thresh=0.000001):
		vcurr = round(seed,2)
		print ("seed:", vcurr)
		while diff > thresh and vcurr < 25.0 and vcurr > 0:
			lcurr = self.lseq(vcurr)
			#if likelihood of current v < new v, set new v as current v & increase the step by 2x	
			vnew = self.step(vcurr,diff)			
			if lcurr < self.lseq(vnew):
				vcurr = vnew					
				diff *= 2			#if likelihood of current v > new v, divide step by 2 and re-try
			else:	                      
				diff /= 2
			print ("current branch length:",vcurr,"| current likelihood:",lcurr, "| current diff:",diff)
		return vcurr
#------------------------------------------------------------------------------------------------------------------
# Class node - a new class

class node(object):
	def __init__(self, name = "", parent = None, children = None, brl = None, seq = None):
		self.name = name
		self.parent = parent
		self.brl = brl
		self.seq = seq
		self.parent = parent
		if children is None:
			self.children = []
		else:
			self.children = children


#----------------------------------------------------------------------------------------------------------------------------
# Class Tree - a class of class "node"

class Tree(node):
	
	def __init__(self):
		"""
		The constructor really needs to be more flexible, but for now we're 
		going to define the whole tree structure by hand. This just uses
		the same statements we used above. By next Thurs (3/19), see if you can
		write a constructor that takes a parenthetical tree as its argument and 
		builds the corresponding tree in memory. 
		"""
		#Creates an instance of class node for root
		self.root = node(name="root") 
		
		#Creates an instance of class node for spC; makes it child of root
		self.spC = node(name="SpeciesC",parent=self.root)
		self.root.children.append(self.spC)
		
		#Creates an instance of class node for ancAB; makes it child of root
		self.ancAB = node(name="ancAB",parent=self.root)
		self.root.children.append(self.ancAB)

		#Creates an instance of class node for spA & spB; makes them children of ancAB
		self.spA = node(name="SpeciesA",parent=self.ancAB)
		self.spB = node(name="SpeciesB",parent=self.ancAB)
		self.ancAB.children.append(self.spA)
		self.ancAB.children.append(self.spB)
		
		# Next, add branch lengths to nodes
		self.spA.brl = 0.2
		self.spB.brl = 0.3
		self.spC.brl = .4
		self.ancAB.brl = 0.1
		self.root.brl = 0
		
		# Create lists to hold simulated seqs
		self.spA.seq = []
		self.spB.seq = []
		self.spC.seq = []
		self.ancAB.seq = []
		self.root.seq = []
		#self.setModels(self.root)

	# Write a recursive function that takes the root node and prints all nodes
	def printNodes(self, node):
		print (node.name)		
		for child in node.children:							
			self.printNodes(child)
				
	# Write a recursive function that takes the root node and prints all terminal nodes
	def printTips(self, node):
        	#termination condition	
		if not node.children:			
			print (node.name)
		else:
			for child in node.children:				
				self.printTips(child)
				
				
				
	#Recursive fx to calculate tree leng (sum of branches)
	def treeLength(self, node):		
		TL = []		
		if node.children is None:
			return node.brl
		else:		
			TL.append(node.brl)
			for child in node.children:				
				TL.append(self.treeLength(child))
		return sum(TL)			
 
	# Write a recursive function that takes the root node as one of its arguments
	# and prints out a parenthetical (Newick) tree string. Due next Tues (3/17).
    
	def newick(self,node):		
		nwk = "("
		if node.children is None:
			return (node.name + ":" + str(node.brl))
		else:	
			#Getting rid of this next line will not add names, why is that?
			nwk += node.name + ":" + str(node.brl)			
			for child in node.children:
				if node.children[-1] == child:										
					nwk += self.newick(child)
					
				else:
					nwk += self.newick(child) + ","
			nwk += ")"
			return nwk
			
	
		
		
    # Now, let's write a recursive function to simulate sequence evolution along a
    # tree. This amounts to simply simulating evolution along each branch 
    # from the root towards the tips. We'll need to use our ctmc class for setting the 
    # conditions of our simulation, which is why we imported it above our tree 
    # class definition. In this case, we've stored the definition of our ctmc 
    # class in a separate file (ctmc.py) to keep our tree code compact.
    # Now, let's add a ctmc object to each internal node in our tree (except the
    # root). Again, it would be best to add the ctmcs as part of the node
    # constructor, if we know that we'll be simulating data.
    
    # Try to get this simulator and associated functions working by next Thurs. (3/19)    
    
	def setModels(self,node):
		"""
		This method of a Tree object defines a ctmc object associated with all
		nodes that have a branch length (i.e., all but the root).
		"""
		
		for child in node.children:							
			self.printNodes(child)
			
	def simEvo(self,node):
		"""
		This method simulates evolution along the branches of a tree, taking
		the root node as its initial argument.
		"""	
				
		if node.parent is None:					
			anc = self.root			
			self.root.seq = cMC().sim()
			print("\n| Current node:",node.name,"| Ancestor: I AM THE ANCESTOR","| ancestral sequence:",node.seq,"|")
		else:
			anc = node.parent		
			print("\n| Current node:",node.name,"| Ancestor:",anc.name,"| Ancestral sequence:",anc.seq,"|")
			node.seq = cMC().sim(anc.seq,node.brl)
		for child in node.children:				
			self.simEvo(child)		
  
	def printSeqs(self,node):
		"""
		This method prints out the names of the tips and their associated
		sequences as an alignment (matrix).
		"""
		
        	#termination condition	
		if not node.children:			
			print ("| current node:",node.name,"| sequence:",node.seq,"|")
		else:
			for child in node.children:				
				self.printSeqs(child)

#----------------------------------------------------------------------------------------------------------------------------------
# Main
#----------------------------------------------------------------------------------------------------------------------------------

#create an instance of class Tree, called tree		
tree = Tree()	

#sets variable (root) to the root node from the tree & prints it
root = tree.root    
print("\nName of the root of the tree:",root.name)

#prints all nodes of the tree
print("\nNodes of the tree:")
tree.printNodes(root)

#prints the external nodes of the tree
print("\nLeaves of the tree:")
tree.printTips(root)

#prints the length of the tree
TL = tree.treeLength(root)
print("\nTotal Tree Length:",TL)

#prints the newick string
print("\nNewick:",tree.newick(root)+";")


"""
model = cMC()
model.sim()
model.printseq()
model.brlen()
"""

#simulates evolution along the tree
tree.simEvo(root)

#prints the nodes & their sequences:
print("\nNodes & Sequences:")
print ("| Current node:    ",root.name,"| Sequence:",root.seq,"|")
tree.printSeqs(root)


