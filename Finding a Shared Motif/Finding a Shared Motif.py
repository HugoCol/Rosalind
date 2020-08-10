
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


def substringsearch(list):
    """Compare the first two strings and search for matches
    Every time a match is found the search is extended from that location to
    find the longest match
    When that fails to match we start attempting to match the next single
    character and repeat the extension until all matches are found
    """
    right = 1
    holder = 0
    matches = []
    # print(list)
    for i in range(len(list[0])):

        m = re.search(list[0][(i-holder):right],list[1])
        if m:
            # if a match is found with character, attempt to match a longer
            # string
            # right extends the length of the re pattern
            right = right + 1
            # holder keeps the iteration location in check
            holder = holder + 1
            matches.append(m.group(0))
        else:
            # if the longer string does not match, reset the length and
            # start with the next character
            right=i
            holder=0
    print(matches)
    return matches

def matchpruning(match_list,fasta_list):
    """In the next part, the found matches are compared to the other strings
    of all the universal matches, the match == to the longest found match
    are returned"""

    confirmed_matches = []
    for i in (match_list):

        for f in fasta_list:
            # check all potention universal matches
            m = re.search(i,f)
        if m:
            # if they are true, they are added to a list
            confirmed_matches.append(m.group(0))
            # the length of the longest match is defined
    maxlength = max(map(len,confirmed_matches))
    print(maxlength)
    # all the matched equal to this length are added to the results
    result = [longest for longest in confirmed_matches if len(longest) == \
                                                         maxlength]

    return result

if __name__ == '__main__':
    file = open("Motiftestdata.txt.txt")
    fasta_list = file_reader(file)
    match_list = substringsearch(fasta_list)

    result = matchpruning(match_list,fasta_list)
    # the first result is printed as it is sufficient to answer the problem
    print(result[0])