import random

POPULATION_SIZE = 100
CHROMOSOME_SIZE = 40
MAGIC_NUMBER = 42
RECOMBINATION_RATE = 0.7
MUTATION_RATE = 0.001

def split_every(s, n):
	split = []
	while len(s) >= n:
		split.append(s[:n])
		s = s[n:]
	return split
def fitness(chrom):
	value = parse_chromosome(chrom)
	if value == MAGIC_NUMBER:
		return 2 #maximum fitness
	return 1.0 / (MAGIC_NUMBER - value)
def make_chromosome():
	return "".join([random.choice(['0', '1']) for _ in range(CHROMOSOME_SIZE)])
def parse_chromosome(chrom):
	last = None
	total = 0
	takes_num = True
	chromosome = [int(i, 2) for i in split_every(chrom, 4)]
	print chromosome
	for gene in chromosome:
		if (last == None and gene > 9) or gene > 13:
			pass
		elif last == None:
			print 'START',
			last = gene
			total = gene
			takes_num = False
			print gene,
		elif takes_num and last > 9 and gene <= 9:
			if last == 10: #+
				print '+',
				total += gene
			elif last == 11: #-
				print '-',
				total -= gene
			elif last == 12: #*
				print '*',
				total *= gene
			elif last == 13: #/
				print '/',
				total /= gene
			else:
				print 'PROGRAMERROR',
			print gene,
			last = gene
			takes_num = False
		elif not takes_num and gene > 9:
			takes_num = True
			last = gene
		elif not takes_num:
			pass
	print 'END',
	return total
if __name__ == "__main__":
	chromosomes = [make_chromosome() for _ in range(POPULATION_SIZE)]
	chromosomes = alg_iter(chromosomes)
	i = 0
	while 2 not chromosomes:
		chromosomes = alg_iter(chromosomes)
		i += 1
		print "{0} iterations.".format(i)