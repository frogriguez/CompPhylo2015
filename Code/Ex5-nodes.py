# -*- coding: utf-8 -*-
"""
Ex6 - Creating and Using Node & Tree Classes
Created on Mon Mar  9 18:48:05 2015

@author: Frogriguez
"""

# - - - class Tree - - -

# - - - class Node - - -
class node(object):
	def __init__(self, name = "", parent = None, child = None):
		self.name = name
		self.parent = parent		
		if child is None:
			self.child = []
		else:
			self.child = child
	
	def treeRec(self,node):
		#if node has children		
		if self.child != None:
			for child in self.children:
				self.treeRec(child)
		else:
			print (self.children.name)			
			return (self.children.name)	
		
# Define the root node to start. It currently has no parents or children.
root = node("root") 
#print (root) #root is just a pointer in memory

# Define a node for species C. It is a direct descendant of the root.
spC = node("Species C",parent=root)
root.children.append(spC)   # Adds spC as a child of the root

# Define a node for the ancestor of species A and B, descending from the root.
ancAB = node("ancAB",parent=root)
root.children.append(ancAB)

spA = node("Species A",parent=ancAB) # Creates spA with ancAB as its parent.
spB = node("Species B",parent=ancAB) # Creates spB with ancAB as its parent.
ancAB.children.append(spA)
ancAB.children.append(spB)

root.treeRec(root)
"""
print("")
print("root's children: ")
for child in root.child:
	print (child.name)

print("\nancAB's children: ")
for child in ancAB.child:
	print (child.name)
"""

				

    



