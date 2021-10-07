# Hugo Colenbradner 23-8-2020
"""
I took the protein masses as a text file form the link in the assignment
then a for loop to add up the protein weight values from the dictionary I
created out of this text file
"""
protein = "DSMKNSGTCDEGQHMYSMLFPFWLANGDDYQLATISAHQLWYDDSQVMGTDMGNYMHFWCPGIKGKLVKGIGRFLVDNFMWTIDTDYIWGMLELFMQMGHPPFGPATSIIKPVQVAPAMIIDHLHSCKYCIELHLIGPTESDSHGFMRGYEAYRDDRPPWIFWSEFDTYFWWPHLPPPDNPLRPLFVARQNLIFQKQSGFGCAFRIDVDGVRWWVNKLFSWRMVQLKGLFKGSYNNLYTIWFDYWNHWRNVFKRKVDDYNAPEWVCPENWIANWKGASMITIRHKKAKEDIQNLRMSKRDFYSQPEKAQPPISDRCITLLSARWMLLMVVIHILPIERDCPLTRGLSSMGFVSHNHVQSHYGASVYHFMFEYVVRSKPKDVRWFSKKSVRKEPDPEYWYSHYTRAMGCLVTVPYHFMRFNAWENDMFGDTDTAIYSLARQHGEYDSSSNKQVYPPVPLNGECPRHMMHIIDHELSGEFDNREQYRYPPAHFWINSEQSTVYFPPNELKMLNWYRHNVKQWAMIKMNRHVDACYCKFLWWVGPARGCICACMWPAHCYWKCGMEENPLHSRQLHHLTWWRNPYSHVRKYYAPTLSTFHYGFENKQTFRYPSMLGYGTHIDGCHARCWGCITDSEMHRQDVVLQRMVDYPYSSPHPHKIDIFGIGTRVMQNSCLECTDIVPMWMANFWVNLLETKVHVDGWIKIDRFMKLDECWMWWIFHSIFVFYNDKHQPGMAILEIWMDFFDNPQNQAYISDNHKYKFIIQGCIICDEQSHQGKWKVMNDHWYAYHWFIGNWKQFMSAKNVHEVTWLSFVWHVAVIRFNLLSCVAELCGWE"
proteinweight = 0
proteindict = {}

with open('Proteinmasslist') as f:

    for line in f.readlines():
        m = line.replace("\n",'').split()
        print(m)
        proteindict[m[0]] = m[1]

for c in protein:
    proteinweight += float(proteindict[c])

print(round(proteinweight,3))