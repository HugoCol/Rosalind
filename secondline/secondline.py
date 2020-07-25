
counter = 0
new_file = open('evenlinelist.txt','w')

with open('rosalind_ini5.txt') as file:
    for i in file:
        counter +=1
        if counter % 2 == 0:
            new_file.write(i)
            print(i)

