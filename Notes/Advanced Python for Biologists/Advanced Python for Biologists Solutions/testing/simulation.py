from __future__ import division
import random
import unittest

class Individual(object):
    """This class represents a single individual in the population."""

    def __init__(self, alleles):
        """Constructor for the Individual class, takes a list of Allele objects."""
        self.alleles = alleles

    def get_fitness(self):
        """Returns the fitness of the individual as a float"""
        final_fitness = 1
        for a in self.alleles:
            final_fitness = final_fitness * a.fitness
        return final_fitness

    def get_genotype(self):
        """Returns a string representing the genotype of the individual"""
        result = ''
        for a in self.alleles:
            result = result + a.name
        return result

class Allele(object):
    """This class represents a particular allele at a locus"""

    def __init__(self, name, fitness):
        """The Allele constructor takes a name (string) and fitness (float)"""
        self.name = name
        self.fitness = fitness

class Locus(object):
    """This class represents a locus"""

    def __init__(self, name):
        """The Locus constructor takes a string representing the locus name"""
        self.name = name
        self.alleles = []

    def add_allele(self, allele):
        """Add an Allele object to the list of alleles for this locus"""
        self.alleles.append(allele)

    def get_random_allele(self):
        """Return a randomly picked Allele from the list of possible alleles at this locus"""
        return random.choice(self.alleles)

def create_individual(loci):
    """Create and return a new Individual with alleles randomly picked from a list of loci"""
    alleles_for_individual = []
    # pick one allele at random from each locus
    for locus in loci:
        alleles_for_individual.append(locus.get_random_allele())
    # use the list of alleles to construct a new Individual
    i = Individual(alleles_for_individual)
    return i



def create_population(size, loci):
    """Return a list of Individuals of the given size with alleles randomly picked from a list of loci"""
    all_individuals = []
    for i in range(size):
        all_individuals.append(create_individual(loci))
    return all_individuals


def summarize_alleles_header(loci, output_file):
    """Write a comma-separated list of allele names for a list of loci to a File object."""
    for locus in loci:
        for allele in locus.alleles:
            output_file.write(allele.name + ' , ')
    output_file.write('\n')

def summarize_alleles(population, loci, output_file):
    """Write a comma-separated list of allele frequencies for a list of loci to a File object"""
    for locus in loci:
        for allele in locus.alleles:
            freq = get_allele_frequency(population, allele)
            output_file.write(str(freq) + ', ')
    output_file.write('\n')

def get_allele_frequency(population, allele):
    """Return the frequency of a given allele in a list of individuals as a float."""
    allele_count = 0
    for individual in population:
        if allele in individual.alleles:
            allele_count += 1
    return allele_count / len(population)

def individual_from_population(population, loci):
    """Return a new individual with alleles picked from a population pool"""
    individual_alleles = []
    for locus in loci:
        # pick an allele from the population for this locus
        all_alleles = []
        for individual in population:
            for allele in individual.alleles:
                if allele in locus.alleles:
                    all_alleles.append(allele)
        # now all_alleles contains all the alleles in the population for this locus
        # pick a random one
        this_allele = random.choice(all_alleles)
        individual_alleles.append(this_allele)
    # now individual_alleles contains all the alleles for our new individual
    # one allele for each locus
    return Individual(individual_alleles)

# function to run a single generation of the simulation
def single_generation(population, all_loci):
    """Given a list of individuals, run a single generation of the simulation.
    Remove individuals from the population with a probability inversely proportional
    to their fitness, and replace them with new individuals with alleles
    picked from the remaining population."""
    # first iterate over each individual and decide whether or not they should die
    for individual in population:
        if random.random() > individual.get_fitness():
            population.remove(individual)
    # then create new individuals and add them to the population until the size is back to 100
    for i in range(100 - len(population)):
        population.append(individual_from_population(population, all_loci))

class TestIndividual(unittest.TestCase):

    def setUp(self):
        allele_one = Allele('A', 0.8)
        allele_two = Allele('B', 0.7)
        self.i = Individual([allele_one, allele_two])

    def testFitness(self):
        self.assertEqual(self.i.get_fitness(), 0.8*0.7)

    def testGenotype(self):
        self.assertEqual(self.i.get_genotype(), 'AB')


class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.locus1 = Locus('locus one')
        self.locus1.add_allele(Allele('A', 1))
        self.locus1.add_allele(Allele('a', 0.94))
        self.locus2 = Locus('locus two')
        self.locus2.add_allele(Allele('B', 1))
        self.locus2.add_allele(Allele('b', 0.76))
        self.pop = create_population(100, [self.locus1, self.locus2])

    def testCorrectPopulationSize(self):
        self.assertEqual(len(self.pop), 100)

    def testAlleleFrequencies(self):
        for locus in [self.locus1, self.locus2]:
            for allele in locus.alleles:
                allele_frequency = get_allele_frequency(self.pop, allele)
                self.assertGreaterEqual(allele_frequency, 0)
                self.assertLessEqual(allele_frequency, 1)



if __name__ == '__main__':
    unittest.main()

