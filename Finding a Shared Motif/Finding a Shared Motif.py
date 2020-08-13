
import re

def file_reader(file):
    """open a fasta file, discard the headers and add the strings"""
    fasta_list = []
    holdstring = ""
    for line in file.readlines():
        if line.startswith(">") and holdstring != "":

            fasta_list.append(holdstring)
            holdstring = ""
        elif line.startswith(">") == False:
            holdstring = holdstring + line.replace("\n","")
    fasta_list.append(holdstring)
    print(fasta_list)
    return fasta_list

def common_substring(seq_list):
    """I did not completely come up with this myself"""
    longest_substring = ""

    full_string = seq_list[0]
    # The first sequence form the list is taken and sliced in all different
    # possible lengths and checked to be in all sequences of the list
    for i in range(len(full_string)):
        for j in range(i+1, len(full_string)+1):
            substring = full_string[i:j]
            # print(i,j)
            print(substring)
            in_all = True
            for seq in seq_list:
                if substring not in seq:
                    in_all = False
                    break
            # check if the current match is longer than any of the previous
            # matches
            if in_all and len(substring) > len(longest_substring):
                longest_substring = substring

    # print("Longest common substring:\n", longest_substring)

if __name__ == '__main__':
    file = open("Motiftestdata.txt.txt")
    fasta_list = file_reader(file)
    common_substring(fasta_list)
    # the first result is printed as it is sufficient to answer the problem
