# -*- coding: utf-8 -*-
"""
Ex8 - Intro to MCMC
Created on Thu Apr  2 10:56:34 2015
@author: Frogriguez
"""

#------------------------------------
# Imports

testPrior = False

from scipy.stats import binom
from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import random

#---------------------------------------
# Data Set

p-true = 0.5
n = 20	
data = binom.rvs(n, p-true) # draws 'data set'
p = random.random()

"""
--------------------------------------------------------------------
                           FUNCTIONS
--------------------------------------------------------------------
"""


#---------------------------------------------------------
# PRIOR

def prior(pin):
	# return prior density for given p
	# samples from pdf, given the input, from 0 --> 1	
	return uniform.pdf(pin, 0, 1)
	
#---------------------------------------------------------
# LIKELIHOOD FUNCTION

#Returns the likelihood score for given p
def likelihood(pin):
#Returns the likelihood score for given p
	
	if (testprior): # test prior & ignore data
		return 1
	elif(not testprior):
		if pin >= 0 and p:
			return binom.pmf(data, n, pin)
			
	