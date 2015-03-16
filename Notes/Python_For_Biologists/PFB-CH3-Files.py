"""
Python for Biologists
Ch3 - Files
01-20-15
"""


"""
3.1 Reading Text from a file
"""
#you must open a file before we can read what's inside

#.open("string") - function that takes a string as the file name
my_file = open("dna.txt")

#read contents into a variable (such as a string) using the .read() method
my_file_contents = my_file.read()

"""
3.2 Files, Contents, File names
"""

#Generally, you will work with file contents, not the file object
file_name = dna'txt"
file = open(file_name)
print(file) #will return an error
contents = file_name.read() #correct

"""
3.3 New Lines
"""
file = open("dna.txt")
contents = file.read()

#remove newline from end of contents
new_contents = contents.rstrip("\n")
#alternatively stack your methods:
new_contents = file.read().rstrip("\n")

"""
3.4 Writing text
"""

#Use second argument in .open() method to tell Python what you want
file = open("dna.txt",'argument')
	#argument = 'r' (read, default), 'w' (write), 'a' (append)
	
#Use the .write("string") method to write to a file
file = open("out.txt", "w")
file.write("Hello world")

"""
3.5 Closing files
"""

#close your files with the .close() method
file = open("out.txt", "w")
file.write("Hello world")
file.close()	#always remember to close your file to avoid bugs

"""
3.6 Paths/Folders
"""

#you can open a file in another folder:
file = open(r"c:\windows\Desktop\myfolder\myfile.txt")
	#NOTE: the 'r' is needed to prevent python from interpreting the first backslash
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

