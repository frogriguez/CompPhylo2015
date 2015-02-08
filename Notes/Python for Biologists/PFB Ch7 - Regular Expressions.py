"""
Jones - Python for Biologists
Chapter 7 - Regular Expressions
02-08-2015
"""


"""
7.1 Regular Expressions
"""

#first you must import the regular expression module
import re

"""
7.2 Search function
"""

#search with search function
re.search(pattern,string)

#to ignore special characters in a string, use raw 'r' expression
print (r"\t\n") #this will not print new tab/line, but print "\t\n"

	"""7.2.2 Alterations"""

#use alternation (or) with "|"
dna = "ATCGCGAATTCAC"
if re.search(r"GG(A|T)CC", dna):
	print("restriction site found!")

#character groups can be used with lists
dna = "ATCGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna):
	print("restriction site found!")
	#The 3rd character can be any base

	"""7.2.3 Character Groups"""
	
#Use "." to search anything
dna = "ATCGCGAATTCAC"
if re.search(r"GC.GC", dna):
	print("restriction site found!")

#Use ^ to exclude characters
dna = "GCFGC, GC&GC and GC9GC"
if re.search(r"GC[^F&9]GC", dna):
	print("restriction site found!")

	"""7.2.4 Quantifiers"""
	
#Use "?" to match zero or one character
re.search(r"GAT?C",dna)
	#T is optional, and the pattern will match either GATCor GAC
re.search(r"GGG(AAA)?TTT",dna)	
	#AAA is optional and will match GGGAAATTT or GGGTTT
	
#Use '+' to match a number of repeated characters
re.search(r"GGGA+TTT",dna)	
	#This will return GGGATTT, GGGAATTT, ...., but NOT GGGTTT

#Use '*' to search zero or multiple instances of a character
re.search(r"GGGA*TTT",dna)
	#will match three Gs, followed by zero or more As, followed by three Ts. So it will match GGGTTT, GGGATTT, GGGAATTT, etc. 
	
#Use '{}' to indicate a specific number of repeats
GA{5}T 
	#will match only GAAAAAT
GA{2,4}T
	#will match an acceptable range of repeats
	
	"""7.2.5 Positions"""

#Use '^' to signify the start of a string
^AAA will return AAATTT, but not GGGAAATTT

#Use '$' to match the end of the string
GGG$ will return AAAGGG, but not AAAGGGCCC

	"""7.2.6 Combing"""

#You can combine multiple regular expressions
^ATG[ATGC]{30,1000}A{5,10}$
	#This must match all of the following conditions:
		#• an ATG start codon at the beginning of the sequence
		#• followed by between 30 and 1000 bases which can be A, T, G or C
		#• followed by a poly-A tail of between 5 and 10 bases at the end of the sequence


"""
7.3 Extracting a part of a string
"""

#The search function doesn't return the data itself, but information about it
#Use the group method to extract the string itself

dna = "ATGACGTACGTACGACTG"
# store the match object in the variable m 
m = re.search(r"GA[ATGC]{3}AC", dna)
print(m.group())

#Use () to capture different bits of pattern
dna = "ATGACGTACGTACGACTG"
GA[ATGC]{3}AC[ATGC]{2}AC
"""That's GA, followed by three bases, followed by AC, followed by two bases, followed 
by ACagain. We can surround the bits of the pattern that we want to extract with 
parentheses – this is called capturingit:"""
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC",dna)
print("entire match: " + m.group())
print("first bit: " + m.group(1))
print("second bit: " + m.group(2))
	"""
	entire match: GACGTACGTAC 
	first bit: CGT 
	second bit: GT
	"""

#You can use .start() & .end() to get beggining & end of a string
dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))
	"""
	start: 2
	end: 13
	"""

"""
7.4 Getting Positional info
"""
	
#We can get position of different groups by supplying a number
dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))
print("group one start: " + str(m.start(1)))
print("group one end: " + str(m.end(1)))
print("group two start: " + str(m.start(2)))
print("group two end: " + str(m.end(2)))
	"""
	start: 2
	end: 13
	group one start: 4
	group one end: 7
	group two start: 9
	group two end: 11
	"""

"""
7.5 Splitting Strings
"""

#Use re.split() function to split string based on a delimiter
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs) 
	"""
	NOTE: '^[ATCG] = everything but ATCG is a delimiter
	['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']
	"""
	
"""
7.6 Multiple Matches
"""

#use .findall() to return all matches
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r"[AT]{4,100}", dna)
print(runs)
	"""
	['ATTATAT', 'AAATTATA']
	"""

#Use .finditer to do more complicated things with multiple matches
	#NOTE: .finditer() returns a list, so we need to use a loop to get everything in it
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"[AT]{3,100}", dna)
for match in runs:
	run_start = match.start()
	run_end = match.end()
	print("AT rich region from " + str(run_start) + " to " + str(run_end))
	"""
	AT rich region from 5 to 12 
	AT rich region from 18 to 26 
	"""