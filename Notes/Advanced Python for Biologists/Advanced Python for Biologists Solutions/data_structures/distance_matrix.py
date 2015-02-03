from __future__ import division

# define our gene set data to work on
gene_sets = {
        'arsenic' : {1,2,3,4,5,6,8,12},
        'cadmium' : {2,12,6,4},
        'copper' : {7,6,10,4,8},
        'mercury' : {3,2,4,5,1}
}

# we can get a similarity score for any two gene sets
set1 = gene_sets['arsenic']
set2 = gene_sets['mercury']
similarity = len(set1.intersection(set2)) / len(set1.union(set2))
print(similarity)

# print all pairwise similarity scores
for condition1, set1 in gene_sets.items():
    for condition2, set2 in gene_sets.items():
        if condition1 != condition2:
            similarity = len(set1.intersection(set2)) / len(set1.union(set2))
            print(condition1, condition2, similarity)

# assemble a dict of dicts to hold similarity scores
similarity_scores = {}
for condition1, set1 in gene_sets.items():
    similarity_scores[condition1] = {}
    for condition2, set2 in gene_sets.items():
        if condition1 != condition2:
            similarity = len(set1.intersection(set2)) / len(set1.union(set2))
            similarity_scores[condition1][condition2] = similarity
print(similarity_scores)

# another way of writing the above, using a temporary dict
for condition1, set1 in gene_sets.items():
    single_similarity = {}
    for condition2, set2 in gene_sets.items():
        if condition1 != condition2:
            similarity = len(set1.intersection(set2)) / len(set1.union(set2))
            single_similarity[condition2] = similarity
    similarity_scores[condition1] = single_similarity
print(similarity_scores)

# another way of writing the above, using a dict comprehension
for condition1, set1 in gene_sets.items():
    ss = {condition2 : len(set1.intersection(set2)) / len(set1.union(set2)) for condition2,set2 in gene_sets.items() if condition1 != condition2}
    similarity_scores[condition1] = ss
print(similarity_scores)

# a very concise way of writing the above, using a nested dict comprehension
ss = {c1: {c2 : len(s1.intersection(s2)) / len(s1.union(s2)) for c2,s2 in gene_sets.items() if c1 != c2} for c1,s1 in gene_sets.items()}
print(ss)
