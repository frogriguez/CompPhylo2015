"""
Python for Biologists
Ch4 - Lists & Loops
01-20-15
"""


"""
4.1 Lists
"""
# use brackets [] to make a list
apes= ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]

#each item is called an "element". To get a single element use its "index"
print (apes[0])

#to obtain the index, use the .index() function:
chimp_index = apes.index("Pan troglodytes")
print (chimp_index)	#this will return 1

#use -index to go in the other direction
last_element = apes[-1]	#this will return the last element in the list

#you can grab a range using ':'
apes2 = apes[0:2]
	#Note: numbers are 'inclusive' at the beginning, 'exclusive' at the end

"""
4.2 Working With Lists
"""

#use .append() function to add to a list
apes.append("Pan paniscus")

#use len() function to get length of a list
print (len(apes))
	#this will return 4
	
#concatenate lists with '+'
apes= ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates"

#To attach one list to another use .extend('list')
apes.extend(monkeys)

#You can use .reverse() and .sort()
ranks = ["kingdom","phylum", "class", "order", "family"]
print("at the start : " + str(ranks))
ranks.reverse()
print("after reversing : " + str(ranks))
ranks.sort()
print("after sorting : " + str(ranks))

"""
4.3 Loops
"""

#loops

apes= ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]

for x in y:
	#do some function
	#y is the name of the loop
	#x is the name used for the current element each time around the loop
		#x only exists in the loop - it is created & deleted within the loop
		#the for loop is the variable 'x's 'scope'

"""
4.4 strings as lists
"""

#you can use loop to process a string as a list
name = "martin"
for character in name:
	print("one character is " + character)
#repeating a set of instructions for each element in a list
# (or char in a str) is called 'iteration'

"""
4.5 splitting a String Into A List
"""

#split takes a variable (eg: a string) and splits it into a list using a 'delimiter'
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))
# ['melanogaster', 'simulans', 'yakuba', 'ananassae']

"""
4.6 Lines in a File
"""

file = open("some_input.txt")
for line in file:
# do something with the line

# NOTE: Python keeps track of its position in each file, 
#	so if you read the contents of a file object using the read
#	method, and then later try to process it one line at a time with a 
#	loop, you won't get any input because Python thinks it's already 
#	at the end of the file. Use .open(), and .close() before the loop to get around

"""
4.7 Looping & Ranges
"""

#with a for loop to print 3-9
protein = "vlspadktnv"
stop_positions = [3,4,5,6,7,8,9]
for stop in stop_positions:
	substring = protein[0:stop]
	print(substring)

#instead use range
protein = "vlspadktnv"
for stop in range(3,8):
	substring = str(protein(stop))
	print(substring)

for number in range(3,8):
	print (number)
	
#you can step through a list using range
for number in range (2,14,4):
	print (number)
	#2 is start of range (inclusive)
	#14 is end of range (Exclusive)
	#4 is how many steps to move each time










