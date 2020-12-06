class Individual:
    
    def __init__(self, chromosome_size,dataset):
        self.chromosome_size = chromosome_size
        self.fitness = 0
        self.weight = 0
        self.dataset = dataset
        self.chromosome = []
        self.chromosome.append(dataset.sample())
        while len(self.chromosome) < self.chromosome_size:
            unique = True
            sam = self.dataset.sample()
            for i in self.chromosome:
                if i.index == sam.index:
                    unique = False
                    break
            if unique:
                self.chromosome.append(sam)