# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:53:19 2015

@author: Frogriguez
"""

#--------------------------------------
# Imports
import numpy as np
import random
from scipy.linalg import expm


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
			
	def newickParser(self, nwk):
		#find the root
		if nwk.startswith("(") and nwk.endswith(";"):
			root = nwk.split("(")[1]
			root = root.replace(",","")
			self.root.brl = root.split(":")[1]
			self.root.name = root.split(":")[0]
			print("root:",root)
		else:
			for internal_node in nwk.split(",")[0]:
				
			
		"""		
		parse = nwk.split(",", maxsplit=1)
		for element in parse:
			if "," not in char:
				#this is a terminal node
				pass
			else:
				#this is an internal node
				pass
		
		pcount = 0
		ccount = 0
		for c in nwk:
			if c == "(":
				pcount += 1
			elif c == ")":
				pcount -= 1
			elif c == ",":
				ccount +=1
			else:
				#start taking node name
				pass
		"""	
nwk = "(C:0.3,(A:02,B:0.1):0.4);"
tree = Tree()
tree.newickParser(nwk)
#root = tree.root
#tree.printNodes(root)