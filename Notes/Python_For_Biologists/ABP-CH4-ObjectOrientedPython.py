"""
Jones - Advanced Python for Biologists
Chapter 4 - Object Oriented Python
02-24-15
"""
#Previously:
	#Type - values in Python come in different flavors
	#Thing - reger to a bit of data (string/file)

#Object - created new thing
#Class - type of object (created)
	#***An object is an INSTNACE of class
#Method - Piece of code belonging to an object




"""
4.2 DNA Seq Class
"""

#Create classes to solve groups of related problems, rather than one well-defined problem

def get_AT(my_dna): 
	length = len(my_dna) 
	a_count = my_dna.count('A') 
	t_count = my_dna.count('T') 
	at_content = (a_count + t_count) / length 
	return at_content 

def complement(my_dna): 
	replacement1 = my_dna.replace('A', 't') 
	replacement2 = replacement1.replace('T', 'a') 
	replacement3 = replacement2.replace('C', 'g') 
	replacement4 = replacement3.replace('G', 'c') 
	return replacement4.upper() 

dna_sequence = "ACTGATCGTTACGTACGAGTCAT" 
print(get_AT(dna_sequence)) 
print(complement(dna_sequence))
	"""
	0.5652173913043478 
	TGACTAGCAATGCATGCTCAGTA
	"""
	
#Add metadata
dna_sequence = "ACTGATCGTTACGTACGAGTCAT" 
species = "Drosophila melanogaster"
gene_name = "ABC1"
print("Looking at the " + species " " + gene_name + " gene")
print("AT content is " + str(get_AT(dna_sequence)))
print("complement is " + complement(dna_sequence)) '
#Need something different to solve this problem

#Instance variables - variables that belong to a particular object
class DNARecord(object): 
	#define define 3 attributes of class DNARecord
	sequence = 'ACGTAGCTGACGATC'
	gene_name = 'ABC1'
	species_name = 'Drosophila melanogaster'
	
	#define method of class DNARecord
	def complement(self): 
		replacement1 = self.sequence.replace('A', 't') 
		replacement2 = replacement1.replace('T', 'a') 
		replacement3 = replacement2.replace('C', 'g') 
		replacement4 = replacement3.replace('G', 'c') 
		return replacement4.upper() 
	def get_AT(self): 
		length = len(self.sequence) 
		a_count = self.sequence.count('A') 
		t_count = self.sequence.count('T') 
		at_content = (a_count + t_count) / length 
		return at_content 
d = DNARecord()
print('Created a record for ' + d.gene_name + ' from ' + d.species_name)
print('AT is ' + str(d.get_AT()))
print('complement is ' + d.complement())




