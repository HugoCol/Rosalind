# Hugo Colenbrander 27-07-2020
# Given: Three positive integers k, m, and n,
# representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor,
# m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will
# produce an individual possessing a dominant allele (and thus displaying
# the dominant phenotype).
# Assume that any two organisms can mate.


# amount in population
khomo = 24
mhetero = 30
nrec = 27
# sum of population
total = khomo + mhetero + nrec

# if the first step is homozygote
phomox1 = khomo / total
phomox = (khomo - 1) / (total - 1)
pheterox = mhetero / (total - 1)
probreccessivex = nrec / (total - 1)

# if the first step is heterozygote
probheteroy1 = mhetero / total
phomoy = khomo / (total - 1)
probheteroy = (mhetero - 1) / (total - 1)
probreccessivey = nrec / (total - 1)

# if the first step is reccessive
probreccessivez1 = nrec / total
phomoz = khomo / (total - 1)
probheteroz = mhetero / (total - 1)
probreccessivez = (nrec - 1) / (total - 1)
# add up all the probabilities that a parent is chosen multiplied by
# the probability that it gives the F1 a dominant allel
prob_dominant = phomox1 + (probheteroy1 * phomoy) + (
            probheteroy1 * probheteroy * 0.75) + (
                        probheteroy1 * 0.5 * probreccessivey) + (
                            probreccessivez1 * phomoz) + (
                            probreccessivez1 * probheteroz * 0.5)

# find out the probability of any parents making a child with a dominant allel
print(prob_dominant)