'''
Gegeven: zes positieve integers die correleren met de aantallen genetypen in
de populatie:
1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

terug: het verwachte aantal kinderen die het dominante genotype hebben
onder de aanname dat ieder stel twee kinderen heeft

voorbeeld:
1 0 0 1 0 1

output: 3.5
'''

parent_genotype = "AaAa"
kids = ""
genotypes = []
for i in range(len(parent_genotype)):
    for c in parent_genotype:
        passing_genotype = c + parent_genotype[i]
        print(passing_genotype)
        genotypes.append(passing_genotype)


D_counter = 0
t_counter = 0
for g in genotypes:
    if 'AA' in g:
        print("hey")
        D_counter += 1
    elif 'A' in g:
        print("hey2")
        D_counter += 1
    else:
        t_counter +=1

print(D_counter)
print(t_counter)