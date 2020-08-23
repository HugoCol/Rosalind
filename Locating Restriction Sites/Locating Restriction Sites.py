"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.

"""


DNA_string = "TCAATGCATGCGGGTCTATATGCAT"

DNA_dict = {"A":"T","T":"A","G":"C","C":"G",}
compliment_string = ""
for i in DNA_string:
    compliment_string+=(DNA_dict[i])

print(DNA_string)
print(DNA_string::-1)
# print(compliment_string[::-1])
# print(compliment_string)
