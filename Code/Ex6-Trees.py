"""
Exercise 6 - Creating and Using node and Tree Classes
@author: zachrodriguez
03-13-15
"""

# ---> Defining node and Tree classes <---

  
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



#import ctmc
# We'll need this later, I promise. It's always better to put import statements
# outside of class definitions. In fact, it's best to put them all at the top
# of a file. This imports the ctmc class that we previously defined.

class Tree:
	def __init__(self):
		"""
		The constructor really needs to be more flexible, but for now we're 
		going to define the whole tree structure by hand. This just uses
		the same statements we used above. By next Thurs (3/19), see if you can
		write a constructor that takes a parenthetical tree as its argument and 
		builds the corresponding tree in memory. 
		"""
		self.root = node("root") 
		self.spC = node("SpeciesC",parent=self.root)
		self.root.children.append(self.spC)
		
		self.ancAB = node("ancAB",parent=self.root)
		self.root.children.append(self.ancAB)

		self.spA = node("SpeciesA",parent=self.ancAB)
		self.spB = node("SpeciesB",parent=self.ancAB)
		self.ancAB.children.append(self.spA)
		self.ancAB.children.append(self.spB)
		
		# Next, add branch lengths to nodes
		self.spA.brl = 0.1
		self.spB.brl = 0.1
		self.spC.brl = 0.2
		self.ancAB.brl = 0.1
		self.root.brl = 0
		
		# Create lists to hold simulated seqs
		self.spA.seq = []
		self.spB.seq = []
		self.spC.seq = []
		self.ancAB.seq = []
		self.root.seq = []
		self.setModels(self.root)

	# Write a recursive function that takes the root node and prints all terminal nodes
	def printTips(self,node):
        	#if node has children		
		if self.child != None:
			for child in self.children:
				self.treeRec(child)
		else:
			print (self.children.name)			
			return (self.children.name)
			
	#Recursive fx to calculate tree leng (sum of branches)
	def treeLength(self,node):
		print ("function under development...")
 
 

	# Write a recursive function that takes the root node as one of its arguments
	# and prints out a parenthetical (Newick) tree string. Due next Tues (3/17).
    
	def newick(self,node):
		print ("function under development...")						



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
		print ("function under development...")	
	
	def simulate(self,node):
		"""
		This method simulates evolution along the branches of a tree, taking
		the root node as its initial argument.
		"""
		print ("function under development...")	
	          
	def printSeqs(self,node):
		"""
		This method prints out the names of the tips and their associated
		sequences as an alignment (matrix).
		"""
		print ("function under development...")	
        




