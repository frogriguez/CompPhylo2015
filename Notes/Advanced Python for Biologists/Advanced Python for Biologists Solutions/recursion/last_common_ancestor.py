
# create the dict to store the child -> parent relationships
tax_dict = {
    'Pan troglodytes' : 'Hominoidea',       'Pongo abelii' : 'Hominoidea',
    'Hominoidea' :  'Simiiformes',          'Simiiformes' : 'Haplorrhini',
    'Tarsius tarsier' : 'Tarsiiformes',     'Haplorrhini' : 'Primates',
    'Tarsiiformes' : 'Haplorrhini',         'Loris tardigradus' : 'Lorisidae',
    'Lorisidae' : 'Strepsirrhini',          'Strepsirrhini' : 'Primates',
    'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' : 'Strepsirrhini',
    'Galago alleni' : 'Lorisiformes',       'Lorisiformes' : 'Strepsirrhini',
    'Galago moholi' : ' Lorisiformes'}

# a recursive function to get the list of ancestors for a single taxon
def get_ancestors_rec(taxon):
    # if the single taxon is Primates, then just return it as a one-element list
    if taxon == 'Primates':
        return [taxon]
    # if the single taxon is not Primates....
    else:
        # ...get the parent of this taxon...
        parent = tax_dict.get(taxon)
        # ...and find the ancestors of the parent
        parent_ancestors = get_ancestors_rec(parent)
        # the result is the taxon, its parent, and the parent's ancestors
        return [taxon, parent] + parent_ancestors

# an iterative function to get the list of ancestors for a single taxon
def get_ancestors(taxon):
    # start of with a list containing the taxon itself
    result = [taxon]
    # keep looping as long as the current taxon is not Primates
    while taxon != 'Primates':
        # look up the parent for the current taxon and append it to the result list
        result.append(tax_dict.get(taxon))
        # now set the new taxon to be the parent of the old taxon
        taxon = tax_dict.get(taxon)
    return result

# a function to return the last common ancestor of two taxa
def get_lca(taxon1, taxon2):
   # calculate the list of taxon1 ancestors
    taxon1_ancestors = [taxon1] + get_ancestors_rec(taxon1)
    # return the first element in the list of taxon2 ancestors that is also in the list of taxon1 ancestors
    for taxon in [taxon2] + get_ancestors_rec(taxon2):
        if taxon in taxon1_ancestors:
            return taxon

# iterative function to get the last common ancestor of a list of taxa
def get_lca_list(taxa):
    # remove the last taxon from the list and call it taxon1
    taxon1 = taxa.pop()
    # keep looping as long as the list of taxa is greater than zero
    while len(taxa) > 0:
        # remove the last taxon from the list and call it taxon2
        taxon2 = taxa.pop()
        # get the last common ancestor of taxon1 and taxon2
        lca = get_lca_rec(taxon1, taxon2)
        print('LCA of ' + taxon1 + ' and ' + taxon2 + ' is ' + lca)
        #set taxon1 to be the last common ancestor and go back to the start of the list
        taxon1 = lca
    return taxon1

# recursive function to get the last common ancestor of a list of taxa
def get_lca_list_rec(taxa):
    print("getting lca for " + str(taxa))
    # if there are only two taxa in the list, then the result is their last common ancestor
    if len(taxa) == 2:
        return get_lca(taxa[0], taxa[1])
    # there there are more than two taxa....
    else:
        # ...remove the last taxon from the list...
        taxon1 = taxa.pop()
        # ...and calculate the last common ancestor of the remaining taxa in the list
        taxon2 = get_lca_list_rec(taxa)
        # the result is the last common ancestor of the last taxon in the list and the last common ancestor of the remaining taxa in the list
        return get_lca(taxon1, taxon2)


print(get_lca_list_rec(['Pan troglodytes','Tarsius tarsier', 'Pongo abelii']))

