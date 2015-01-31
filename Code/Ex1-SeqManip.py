"""
Zachary Rodriguez (zachrodriguez)
CompPhylo
Exercise 1 - Sequence Manipulation
01-20-15
"""

"""
(1) Create a new Python script (text file)
	At the beginning of the script, define a DNA sequence (taken from 
	https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)
"""

#Opens 'CodingSeq.txt' as a readable file called 'cds'
cds = open('CodingSeq.txt','r')

#creates a string:'dna', by reading in from the file, then closing
dna = cds.read()
cds.close()
#makes string:'dna' uppercase
dna = dna.upper()

"""
(2) Print the length of the sequence to the screen along with text explaining 
	the value
"""

#this will print the sequence length (len(seq)) and the cds to the screen
print ("Here is the",len(dna),"bp","nucleotide sequence:\n",dna)

"""
(3) Create and store the RNA equivalent of the sequence, then print to screen.
"""

#creates a writeable file: 'RNAseq.txt'
rna = open('RNAseq.txt','w')

#replaces T->U in string: 'dna', names it 'cds'
cds = dna.replace("T","U")

#writes string: 'cds' to file: 'RNAseq.txt'
rna.write(cds)
rna.close()

"""
(4) Create and store the reverse complement of your sequence, then print to 
	screen.
"""
#iteratively (?) replaces each nucleotide with it's lowercase complement
dnaa = dna.replace("A","t")
dnat = dnaa.replace("T","a")
dnac = dnat.replace("C","g")
dnag = dnac.replace("G","c")
dna_comp = dnag.upper()
print ("\n The reverse complement of your DNA sequence is:\n",dna_comp,"\n")

"""
(5) Extract the bases corresponding to the 13rd and 14th codons from the 
	sequence, then print them to the screen.
"""
#extracts the 13th (36-39) & 14th (39-42) codon in the original dna cds
#	Note: in string[x,y] - x is inclusive, y is exclusive
codon13 = dna[36:39]
codon14 = dna[39:42]
print ("The 13th codon in your sequence:",codon13)
print ("The 14th codon in your sequence:",codon14)

"""
(6)Create a function to translate the nucleotide sequence to amino acids 
	using the vertebrate mitochondrial genetic code (available from 
	https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt).
	Translate the sequence and print it to the screen.
	Be sure you've added comments to explain what this script is and what the 
	different bits of code mean.
	Save this script as "seqManip.py" and commit it to your class GitHub repo
"""

#creates a list: 'bases' containing the 4 nucleotides
bases = ["T", "C", "A", "G"]	

#assembles a list of codons called 'codons' by iterating through the 4 bases from T -> G
#	that will serve as the keys
codons = [a + b + c for a in bases for b in bases for c in bases]

#creates a string of amino acids: 'aminoacids' in order with regards to the vert 
#	genetic code table that will serve as values
aminoacids = "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"

#maps a dictionary by zipping together the two lists (keys-values)
genetic_code = dict(zip(codons,aminoacids))
print ("Your genetic code dictionary is:\n",genetic_code)

#This script uses the created dictionary containing the genetic code and takes the key (codon)
#	and returns the value (amino acid)

prot = ""								#creates an empty string: 'prot'
for x in range(0,len(dna),3):			#loops in range from 0, to length of sequence, in steps of 3
	codon = dna[x:x+3]					#extracts codon from x (inclusive) -> next 3 (not inclusive)
	aa = genetic_code.get(codon, "*")	#passes codon as an key to the dict: 'genetic_code', returns aa as string
#	print (codon,":",aa)				#just a check
	prot += aa					#appends amino acid to the 'prot' string
print ("\n Your translated amino acid sequence:\n",prot)

