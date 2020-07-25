
dictionariesoutput = {}
outputlist = []

new_file = open('dicionaryoutputlist.txt','w')
with open('rosalind_ini6.txt') as file:
    for i in file.readline().replace('\n','').split(' '):
        try:
            dictionariesoutput[i] +=1
        except KeyError:
            dictionariesoutput[i] = 1


print(outputlist)

for i in dictionariesoutput.keys():
    outputlist.append(i + ' ' + str(dictionariesoutput[i]))

for i in outputlist:
    new_file.write(i +'\n')

print(outputlist)