# Hugo Colenbrander 25-7-2020
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# # #
# # # Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# # # Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
# # # please see the note on absolute error below.

def file_reader(file):
    """
    Read a fasta file and add it to a dictionary

    """
    dict = {}
    # if a line starts with a > it is a header and should be a key
    # file.readlines()
    # file = file.readlines()
    file = file.readlines()

    for line in file:
        if line.startswith('>'):
            dict[line.strip()] = ''
            current = line.strip()
         # if it does not start with >, is is a line of sequence and need to be added to the previously created key
        else:
            dict[current] += line.strip()

    return dict

def gc_calc(gcdictionary):
    """
    This function opens a dictionary with headers as keys and dna sequences as values
    calculates the GC percentage of every dna sequence
    and returns the header(key) and dna-sequence(value) of the dna-sequence with the highest GC percentage
    :return:
    """
    value = 0
    comparevalue = 0
    for keys in gcdictionary.keys():
        # count all the ACTG character in the string
        a = gcdictionary[keys].count('A')
        c = gcdictionary[keys].count('C')
        g = gcdictionary[keys].count('G')
        t = gcdictionary[keys].count('T')
        total = a + c + g + t #calculate gc percentage
        value = (c + g)/(total)*100
        # if the gc percentage is higher than the previous record, make this the new record, else pass
        if value >= comparevalue:

            comparevalue = value
            highkey = keys
            highsequence = (f"{comparevalue:.6f}")
        else:
            pass
    # print(highkey,highsequence)
    return highkey,highsequence
def file_writer(highkey,highsequence):
    """This function takes two strings and adds them to a .txt while while separeted by an enter"""
    highkey = highkey.strip('>') # strip the > as it was required in the assignment
    f = open("highestgcpercentageanswer.txt","w") # create a file to be written
    f.writelines([highkey,'\n',str(highsequence)]) # write the strings to the file as a list
    f.close() # close the file
    f = open("highestgcpercentageanswer.txt","r") # check if it is written correctly
    print(f.read())

if __name__ == '__main__':
    # file = "C:\Users\Hugo\Documents\PycharmFiles\Rosalind\testdatasetgcpercentage.fasta"
    file = open(r"C:\Users\Hugo\Documents\PycharmFiles\Rosalind\rosalind_gc.txt")
    fastafile = file_reader(file)
    highkey,highsequence = gc_calc(fastafile)
    file_writer(highkey,highsequence)
