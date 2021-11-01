import random


class Genes():
    def __init__(self):
        self.num = random.randint(0, 1)


class Chromosomes(Genes):
    def __init__(self):
        self.list_chromosome = []

        for i in range(10):
            genes = Genes()
            self.list_chromosome.append(genes.num)
        self.mutation_choro()

    def mutation_choro(self):
        num = random.randint(0, len(self.list_chromosome))
        for x in range(num):
            if random.randint(0, 1) == 0:
                if self.list_chromosome[x] == 0:
                    self.list_chromosome[x] = 1
                else:
                    self.list_chromosome[x] = 0


class DNA(Chromosomes):
    def __init__(self):
        self.list_DNA = []
        for i in range(10):
            chromosome = Chromosomes()
            self.list_DNA.append(chromosome)

    def TString(self):
        for x in self.list_DNA:
            print(x.list_chromosome)

    def mutation_DNA(self):
        self = DNA()
        return self


class Organism(DNA):
    def __init__(self, environment, dna=""):
        super().__init__()
        self.environment = environment
        self.dna = DNA()

    def mutan(self):
        num = random.randint(0, 100)
        print(num)
        print(self.environment)
        if (num < self.environment):
            return DNA()
        else:
            return self


# choro = Organism(100)
choro = DNA()

# choro = choro.mutation_Dna()
# print("-------")
# choro.TString()
