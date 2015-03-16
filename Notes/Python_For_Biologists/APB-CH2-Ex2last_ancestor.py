# Advanced Python for Biologists CH2 Exercise
# Exercise: Last Common Ancestor

# Take 2 arguments (dictionary of relationships & list of taxons)
# and return the last common ancestor. Try iterative & recursive.

#Creates dictionary of child -> parent relationships
tax_dict = {
    'Pan troglodytes' : 'Hominoidea',       'Pongo abelii' : 'Hominoidea',
    'Hominoidea' :  'Simiiformes',          'Simiiformes' : 'Haplorrhini',
    'Tarsius tarsier' : 'Tarsiiformes',     'Haplorrhini' : 'Primates',
    'Tarsiiformes' : 'Haplorrhini',         'Loris tardigradus' : 'Lorisidae',
    'Lorisidae' : 'Strepsirrhini',          'Strepsirrhini' : 'Primates',
    'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' : 'Strepsirrhini',
    'Galago alleni' : 'Lorisiformes',       'Lorisiformes' : 'Strepsirrhini',
    'Galago moholi' : ' Lorisiformes'}
	
#Recursive Method:
def get_lca_rec:

#Iterative Method:
def get_lca_it:

#iterative fx to list parents of given taxon
def get_ancestors_it(taxon)
	parent = [taxon]
	while taxon != 'Primates':
		parent.append(tax_dict.get(taxon))
		taxon = tax_dict.get(taxon)
	return parent

# recursive fx to list parents of given taxon
def get_ancestors_rec(taxon)
	if taxon == "Primates":
		return [taxon]
	else:
		parent = tax_dict.get(taxon)
		parent_ancestors = get_ancestors_rec(parent)
		return [parent] + parent_ancestors