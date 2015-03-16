# -*- coding: utf-8 -*-
"""
CompPhylo Notes
Nucleotide Substitution Models
Yang CH1
Created on Tue Mar  3 15:39:43 2015

@author: Frogriguez
"""

JC model has zero free paramaters
	but we are usually estimating branch length
r = relative propensity for one base to change to another 

K80 = similar to JC, but has different rates of transitions/transversion
	same as K2P
	has 1 more free parameter. We still scale the mean to one
		we are also estimating alpha and beta (transitions/transversions)
		but because we are setting the mean to one, we can calculate the alpha from the beta

We usually estimate the parameters of the Q matrix from the data, rather than the other way around
We scale the Q matrix from the branch lengths to have a mean of 1.0

F80
	stationary frequencies are the same (Pi)
		probability of changing to an A is only based on the stationary frequency and it 
		doesn't matter if you were in a C, G, or T
		
HKY85 / F84
	Combines K80 and F80
	Different stationary frequencies and different rates of transitions / transversions
		
These are all reversible models

Timura Nei 93 = TN93
	adds one more tweak beyond HKY85 / F84
	Two alphas = different rates of transitions
	transversions have the same

Most general model!
GTR = general time reversible 
	every type of change is different
	every stationary frequency is different
	Pi have to sum to one = 3 free parameters
	r = 5 free parameters, because we can always figure out the sixth one
	total = 8 free parameters
	
You loose one free parameter when you scale the Q matrix to one, because you can figure out the last one

UNREST model 
	TA != AT
	Non-reversible model
	Imposing directionality, so you can potentially estimate the root
	
More general models ALWAYS give better likelihood values, as long as the models are nested

check figure 1.4 in Yang


There is one more generality that we add to these models.
What variation is true for all models that we don't capture?
	All sites are changing at the same rate / sites that don't change
	Rates are constant over time / across the tree
	
Yang developed models for changing rates across sites
Invariant sites and gamma parameter

Invariant = haven't observed changes
Invariable = sites can't change

gamma-distributed rates
	parameter = alpha = controls the shape of the distribution
	plot of gamma density vs. rate
		set alpha = beta, makes the mean = 1.0
		we usually think about alpha
		alpha can take any value from 0 to infinity
		Invariable sites model sets some sites at zero on this model
		when alpha -> 0, gamma becomes the exponential distribution
			because the mean is still 1.0, we get a long tail = a few hyper-variable sites
		when alpha -> infinity = rate variation centered around 1.0 = low rate variation
		
Look into the program ModelTest

identifiablity
	parameters have to be identifiable
	when two different models have the same explanatory power with different parameter estimates
		= non-identifiable
		

rates and times are often not identifiable 

HW:
estimate branch lengths using the marginal probabilities 