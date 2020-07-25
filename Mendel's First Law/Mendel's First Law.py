# Given: Three positive integers k, m, and n,
# representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor,
# m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate.

khomo = 11
mhetero = 11
nrec = 11

total = khomo + mhetero + nrec
print(total,khomo)

phomox1 = khomo/total
phomox = (khomo-1)/(total-1)
pheterox = mhetero/(total-1)
probreccessivex = nrec/(total-1)

probheteroy1 = mhetero/total
phomoy = khomo/(total-1)
probheteroy = (mhetero-1)/(total-1)
probreccessivey = nrec/(total-1)


probreccessivez1 = nrec/total
phomoz = (khomo)/(total-1)
probheteroz = mhetero/(total-1)
probreccessivez = (nrec-1)/(total-1)
print(probreccessivez1,phomoz)
print(probreccessivez1*phomoz)
print(phomox1 + phomox)



# print(X,Y)
