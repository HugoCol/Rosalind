# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp
# ) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection.
# (If several possible consensus strings exist,
# then you may return any one of them.)
# Hugo Colenbrander 7/8/2020

def matrix_builder(file):
    """read a fasta file and return a list with sequences"""
    sequence_dictionary = {}

    for line in file:
        if line.startswith('>'):
            k=line.replace('\n','')
            sequence_dictionary[k] = ""
        else:
            sequence_dictionary[k] = sequence_dictionary[k] + line.replace("\n","")
            # sequence_dictionary.append(line)
    print(sequence_dictionary)
    return sequence_dictionary

def scoring(sequence_dictionary):
    """count the amount of amino acid in each colomn of the matrix,
    also return a consensus pattern based on the most common aminoacid in
    each colomn"""
    # start the variables
    a_list = 'A:'
    t_list = 'T:'
    c_list = 'C:'
    g_list = 'G:'
    dict_hold = []
    consensuspattern = ''
    # take the length of the first sequence, which should be equal to all
    # other in a matrix.
    """Still have to get the proper length of the first value in the 
    dictionary"""
    length = range(len(sequence_dictionary))
    print(length)
    # for every column, make add a dictionary to a list
    for i in length:
        dict_hold.append({'A':0,'T':0,'C':0,'G':0})
        # for
        for n in sequence_dictionary.values():
            m = n[i]
            # i is the location in the list and m is the dictionary key
            s = dict_hold[i][m] = dict_hold[i][m] + 1

        a = str(dict_hold[i]['A'])
        t = str(dict_hold[i]['T'])
        c = str(dict_hold[i]['C'])
        g = str(dict_hold[i]['G'])
        # here is the amount of times a nucleotide is counted in a column
        # added to a strings, separated by spaces
        a_list = a_list + " " + str(a)
        t_list = t_list + " " + str(t)
        c_list = c_list + " " + str(c)
        g_list = g_list + " " + str(g)
        consensus_char = (max(a,t,c,g))
        # The nucleotides are counted in variables a,t,c,g. If that amount
        # matches the highest counted number that nucleotide gets added to
        # the consensus pattern
        if a == consensus_char:
            consensuspattern= consensuspattern+'A'
        if t == consensus_char:
            consensuspattern= consensuspattern+'T'
        if c == consensus_char:
            consensuspattern= consensuspattern+'C'
        if g == consensus_char:
            consensuspattern= consensuspattern+'G'


    return a_list,t_list,c_list,g_list,consensuspattern


if __name__ == '__main__':
    file = open('rosalind_cons.txt')
    sequence_list = matrix_builder(file)
    a,t,c,g,consensus = scoring(sequence_list)
    print(consensus)
    print(a)
    print(t)
    print(c)
    print(g)
