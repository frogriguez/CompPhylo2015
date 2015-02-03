import simulation

# create alleles and loci
locus1 = simulation.Locus('locus one')
locus1.add_allele(simulation.Allele('A', 1))
locus1.add_allele(simulation.Allele('a', 0.94))
locus2 = simulation.Locus('locus two')
locus2.add_allele(simulation.Allele('B', 1))
locus2.add_allele(simulation.Allele('b', 0.76))
locus3 = simulation.Locus('locus three')
locus3.add_allele(simulation.Allele('C', 1))
locus3.add_allele(simulation.Allele('c', 0.81))
all_loci = [locus1, locus2, locus3]

# create a population of 100 individuals
my_population = simulation.create_population(100, all_loci)

# open the alleles frequency output file and write the header line
alleles_output = open('alleles.csv', 'w')
simulation.summarize_alleles_header( all_loci, alleles_output)

# for each generation...
for i in range(100):
    # ...write a line of output to the file...
    simulation.summarize_alleles(my_population, all_loci, alleles_output)
    # ...then simulate death and reproduction
    simulation.single_generation(my_population, all_loci)

# close the output file
alleles_output.close()

