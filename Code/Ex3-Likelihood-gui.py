"""
CompPhylo2015
Ex3 - Intro To Likelihood
29 Jan 2015
Zachary Rodriguez
"""

#My Imports
import scipy
from scipy.stats import binom
from numpy import random
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure as plot
from tkinter import *
from tkinter import messagebox
import time


#create Widget Grid (gui) named "gui"
gui = Tk()
gui.title("Likelihood Exercises!") #grid title


#defines user entry spots
entryn = Entry(gui)
entryn.grid(row=0,column=1)	#entry for 'n' in (0,1)
	
entryk = Entry(gui)
entryk.grid(row=1,column=1)	#entry for 'k' in (1,1)

	
entryp = Entry(gui)
entryp.grid(row=2,column=1)	#entry for 'p' in (2,1)

entryg = Entry(gui)
entryg.grid(row=3,column=1)	#entry for 'guess'

#Creates & plots labels in the gui
Label(gui, text="Number of trials (n):").grid(row=0,column=0)   #Labels entry2: "n"
Label(gui, text="0 = random").grid(row=0,column=2)  
Label(gui, text="Number of successes (k):").grid(row=1,column=0)   #Labels for user entry "k"
Label(gui, text="0 = random").grid(row=1,column=2)  
Label(gui, text="Probability (p):").grid(row=2,column=0)  #Labels for user entry "p"
Label(gui, text="0 = random, 1 = generate list").grid(row=2,column=2) 
Label(gui, text="<---Put your guess in here").grid(row=3,column=2)

def probs(step=0.05):
	p_list = []
	p = 0
	while p <= 1.001:		#range function doesn't take floats
		p_list.append(p)
		p += step
	#print("Here is your list of probabilities:",[print (p) for p in p_list])
	return (p_list)

def getn():
	n = entryn.get()
	if n == 0:
		n = random.random()
	elif n ==1:
		n = probs()
	else:
		n = n
	return n
		
def getk():
	k = entryk.get()
	if k == 0:
		k = random.random()
	elif k ==1:
		k = probs()
	else:
		k = k
	return k
	
def getp():
	p = entryp.get()
	if p == 0:
		p = random.random()
	elif p ==1:
		p = probs()
	else:
		p = p
	return p

	
	
def in_class():
	messagebox.showinfo("Instructions:    ", "You have 2 seconds to fill the trials (n) field!")
	time.sleep(3)
	n = int(getn())
	p = random.random()	#gives (p) a random value between 0 & 1
	k = binom.rvs(n,p)	#draws from a binomial distribution based on (n,p), returns # of successes
	message = str("For ("+str(n)+") trials, The number of successes was: "+str(k)+"\nWhat you think the probability was?\n(Press 'OK', then you have 5 seconds to put your answer in the guess box)")
	messagebox.showinfo("Guestimate!:                       ", message)
	time.sleep(5)
	guess = float(entryg.get())	#queries the user for a guess
	if guess > 1:
		guess /= 100
	else:
		guess = guess
	error = 100*(abs(p-guess)/p)
	if error < 5:
		message =  str("Sweet! The probability was: "+str(p)+"\nYou're %error was: "+error+"\nGo Buy a lotto ticket!")
	elif error < 20:
		message = str("So Close! The probability was: "+str(p)+"\nYou're %error was: "+str(error))
	else:
		message = str("womp womp... The probability was: "+str(p)+"\nYou're %error was:"+str(error)+"\nTry increasing number of trials")
	messagebox.showinfo("Results:                          ", message)

	

#This function sets up a list of probabilities from 0 -> 1 over a defined interval


"""
#a calculation necessary for the binomial coefficient
def multiply(min=1, max=10):
	total = 1
	for num in range(max,min-1,-1):	#iterates through range: max -> min, stepping -1 each time
		total *= num
	return (total)
"""

#Calculates the Binomial Coefficient (n choose k)
def bincoef(n,k):
	total = 1
	for num in range(n,(n-k),-1):	#iterates through range
		total *= num 
	bcf = total/math.factorial(k)
	#print ("Your binomial coefficient is:",bcf,"given (",n,"choose",k,")")
	return bcf

#Calculates the Binomial PMF
def bpmf(n,k,p):
	bc = bincoef(n,k)
	pmf = bc*pow(p,k)*pow(1-p,n-k)
	#print ("Your binomial pmf is:",pmf,"given",n,"trials,",k,"successes and a probability of:",p)
	return pmf

#Calculates likelihood scores
def likelihood(n,k,p):
	pmf = bpmf(n,k,p)
	bc = bincoef(n,k)
	l = pmf/bc
	#print ("Your Likelihood score for p =",p,"is:",l,",given",n,"trials and",k,"successes")
	return l

#calculates maximum likelihood
def ml(n,k):
	lscores,lratios = [],[]
	p_list = probs()
	[lscores.append(likelihood(n,k,p)) for p in p_list]	#calculates likelihood score for each prob
	maxl = max(lscores)
	lindex = lscores.index(maxl)
	maxp = p_list[lindex] 
	for l in lscores:
		ratio = abs(l-maxl)/maxl
		lratios.append(ratio)
	print ("Your ML score for p =",maxp,",is:",maxl,",given (",n,") trials and (",k,") successes")
	return lscores,maxl,lratios,maxp

#These Are Tests----------------
#in_class(100)
#probs()
#bpmf(5,1,.5)
#likelihood(5,1,.5)
#ml(100,20)

"""
this bit of code is not working, cuz zeros n stuff
def loglihood(lscores):
	logs = []
	for l in lscores:
		log = math.log(l[10])
		logs.append(log)
	print ("Here is your list of loglihoods:",logs)
"""

"""
#Old graph (without gui)
def graph(x,y):
	plt.plot(x, y)
	plt.xlabel("Probabilities")
	plt.ylabel("Likelihoods")
	plt.show()
"""

def graph():
	n,k,p = int(getn()),int(getk()),(getp())
	lscores,maxl,lratios,maxp = ml(n,k)
	x = probs()
	y = lscores
	a = fig.add_subplot(111)
	a.clear()    #clear figure so you can graph again
	a.plot(x,y)
	a.set_title("Likelihood")
	a.set_xlabel("Probabilities")
	a.set_ylabel("Likelihood Scores")
	canvas.show()

#Makes buttons
Button(gui, text='Graph', command=graph).grid(row=4, column=0, sticky=W, pady=4)  #creates a graph button, executes simulation function on press
Button(gui, text='Play', command=in_class).grid(row=4, column=1, sticky=W, pady=4)  #creates a graph button, executes simulation function on press
Button(gui, text='Quit', command=gui.quit).grid(row=4, column=2, sticky=W, pady=4)  #Creates a quit button


#creates figure frame
frame=Frame(gui)
frame.grid(row=0,rowspan=4, column=4)
fig = plot(figsize=(6,5), dpi=100)

#Plots figure (graph) into gui
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

gui.mainloop( )















