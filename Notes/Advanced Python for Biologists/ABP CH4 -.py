"""
Jones - Advanced Python for Biologists
Chapter 3 - Complex Data Structures
01-26-15
"""

"""
3.1 Tuples
"""

#Use parentheticals to define a tuple
t = (4,5,6)

#Use brackets to retreive an element
print t[1]

#tuples are immutable
t[2] = 9 #This will result in an error

#Useful for storing heterogenous data (seq, accession#, genetic code)
t1 = ('actgctagt', 'ABC123', 1)
t2 = ('ttaggttta', 'XYZ456', 1)
t3 = ('cgcgatcgt', 'HIJ789', 5)

"""
3.2 Sets
"""

#Dictionaries are useful for storing info:
processed = {}
	for acc in accessions:
		if not acc in processed:
			# do some processing
			processed[acc] = 1

#However, Sets are better for processing - they store keys instead of the values themselves
processed = set()
	for acc in accessions:
		if not acc in processed:
			# do some processing
			processed.add(acc)

#create an empty set by using {}
set = {4,7,6,12}

"""
3.3 Lists of Lists
"""
#Lists are great:
L1 = [1,2,3,4]	#for values
L2 = ['a', 'b', 'c']	#for strings
L3 = [open('one.txt'), open('two.txt')]	#for file objects
import re	#for regular expressions
L4 = [re.search(r'[^ATGC]', 'ACTRGGT'), re.search(r'[^ATGC]', 'ACTYGGT')]

L5 = [[1,2,3],[4,5,6],[7,8,9]] #Lists of Lists!
# more readably, aka: 2-dimensional list
	[[1,2,3],
	[4,5,6],
	[7,8,9]]

#retrieve an element from a 2D list
lol = [[1,2,3],[4,5,6],[7,8,9]]
print(lol[1][2])

#multidimendional list:
aln = [['A', 'T', '-', 'T', 'G'], 
['A', 'A', 'T', 'A', 'G'], 
['T', '-', 'T', 'T', 'G'], 
['A', 'A', '-', 'T', 'A']] 

#we can retrieve a specific list (sequence):
seq = aln[2]

#or a specific element
char = aln[2][3]

#get an entire column by retrieving a particular position for each inner row
col = [seq[3] for seq in aln]

"""
3.4 Lists of Dicts & Tuples
"""

#useful for storing collections of related records
records = [
{'name' : 'actgctagt', 'accession' : 'ABC123', 'genetic_code' : 1},
{'name' : 'ttaggttta', 'accession' : 'XYZ456', 'genetic_code' : 1},
{'name' : 'cgcgatcgt', 'accession' : 'HIJ789', 'genetic_code' : 5}
]
	#The elements are 'anonymous' - they don't have names
	#Each value is a diff type of info - a mixture of strings and numbers
	#Each dictionary is an element in our list - the keys are simply labels

#We can refer to an entire dict my giving its index in the list:
one_record = records[2]

#The labels-type keys allow a readable way of processing
for record in records:
	print('accession number : ' + record['accession'])
	print('genetic code: ' + str(record['genetic_code']))
		"""
		accession number : ABC123 
		genetic code: 1 
		accession number : XYZ456 
		genetic code: 1 
		accession number : HIJ789 
		genetic code: 5
		"""

#Lists of Tuples are useful for avoiding writing labels, and relying on order:
records = [
('actgctagt', 'ABC123', 1),
('ttaggttta', 'XYZ456', 1),
('cgcgatcgt', 'HIJ789', 5)
]
for record in records:
	print('accession number : ' + record[1])
	print('genetic code: ' + str(record[2]))
	
#We can assign all the elements in a tuple to variables to iterate through them:
	#This is called 'unpacking' the tuple - making it more readable
for record in records:
(this_sequence, this_accession, this_code) = record
	print('accession number : ' + this_accession)
	print('genetic code: ' + str(this_code))
	
"""
3.5 Other Complex Data Sets
"""
#We have learned about: "SEQUENCES" - lists, tuples, tuples of lists, etc..

	"""
	3.5.1 Dicts of Sets
	"""
	
	#We can create
	gene_sets = {
		'arsenic' : {1,2,3,4,5,6,8,12},
		'cadmium' : {2,12,6,4},
		'copper' : {7,6,10,4,8},
		'mercury' : {3,2,4,5,1}
	}
	
	
#TAKE MORE NOTES	
	
