"""
Jones - Python for Biologists
Chapter 5 - Functions
01-26-15
"""
# Create your own function to do a particular job

"""
5.1 Defining
"""

#Define a function with def():
def get_at_content(dna): 
	length = len(dna) 
	a_count = dna.count('A') 
	t_count = dna.count('T') 
	at_content = (a_count + t_count) / length 
	return at_content
	#This is the function 'body'
	
#execute a function by calling it:
get_at_content(ATGACTGGACCA)
	#However, it will vanish after its been calculated

#we need to store the result somehow
at_content = get_at_content(ATGACTGGACCA)

#you can call it directly
print("AT content is " + str(get_at_content("ATGACTGGACCA")))
	#remember: any variables we create as part of the fx only exist inside the fx

"""
5.2 Calling Functions
"""
#run a program to troubleshoot
def get_at_content(dna): 
	length = len(dna) 
	a_count = dna.count('A') 
	t_count = dna.count('T') 
	at_content = (a_count + t_count) / length 
	return at_content 
my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))
	"""	
	#This is what prints - doesn't look too hot
	0.45 
	0.5294117647058824 
	0.0
	"""
#Improve the function with the round function & UPPER
def get_at_content(dna): 
	length = len(dna) 
	a_count = dna.upper().count('A') 
	t_count = dna.upper().count('T') 
	at_content = (a_count + t_count) / length 
	return round(at_content, 2)

#Make it even better by taking number of SigFigs as an argument
def get_at_content(dna, sig_figs): 
	length = len(dna) 
	a_count = dna.upper().count('A') 
	t_count = dna.upper().count('T') 
	at_content = (a_count + t_count) / length 
	return round(at_content, sig_figs) 
test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))
	
"""
5.3 Encapsulation
"""
#Encapsulation - dividing up complex program into little bits
#	that we can work on independently

#In previous example, we had to troubleshoot 2 different parts: function & Execution

"""
5.4 Functions & Arguments
"""
#functions don't need to take in arguments
def get_a_number():
	return 42

#OR:
def get_at_content(): 
	length = len(dna) 
	a_count = dna.upper().count('A') 
	t_count = dna.upper().count('T') 
	at_content = (a_count + t_count) / length 
	return round(at_content, 2) 
dna = "ACTGATCGATCG"
print(get_at_content())

#This code will only work if there is a variable called 'dna' within the code

"""
5.5 Functions & Return
"""
#Functions don't always have to return a value
def print_at_content(dna): 
	length = len(dna) 
	a_count = dna.upper().count('A') 
	t_count = dna.upper().count('T') 
	at_content = (a_count + t_count) / length 
	print(str(round(at_content, 2)))

	#Try partitioning your finctions so that they only perform one job
	#if you wanted to do a calculation - write a separate fx

"""
5.6 Function Calling & Arguments
"""
#Instead of relying on the ORDER of arguments:
get_at_content("ATCGTGACTCG", 2)
 
#use 'KEYWORD ARGUMENTS':
get_at_content(dna="ATCGTGACTCG", sig_figs=2)
get_at_content(sig_figs=2, dna="ATCGTGACTCG")	#Either of these will behave the same

#You can mix & match
get_at_content("ATCGTGACTCG", 2)
get_at_content(dna="ATCGTGACTCG", sig_figs=2)
get_at_content("ATCGTGACTCG", sig_figs=2)
	#These are all Identical

"""
5.7 Function Argument Defaults
"""
#We can set defaults to arguments if none are specified:
def get_at_content(dna, sig_figs=2): 	#the default SigFigs is 2
	length = len(dna) 
	a_count = dna.upper().count('A') 
	t_count = dna.upper().count('T') 
	at_content = (a_count + t_count) / length 
	return round(at_content, sig_figs)

get_at_content("ATCGTGACTCG")
get_at_content("ATCGTGACTCG", 3)
get_at_content("ATCGTGACTCG", sig_figs=4)
	"""
	0.45
	0.455
	0.4545
	"""
#This is only useful for some arguements, setting a default for 'dna' is useless

"""
5.8 Testing Functions
"""
#Test functions periodically

#Use the 'ASSERT' function to test a function
assert get_at_content("ATGC") == 0.5
	#If assert function = false, we will ger: 'AssertionError'
	
