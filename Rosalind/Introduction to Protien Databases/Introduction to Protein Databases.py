# Hugo Colenbrander 15/8/2020
import urllib.request

"""
After being unable to connect with the Uniprot database with the given 
information and modules I decided to download the required data as .txt 
from uniprot and us some for loops to get cut down the lines until the 
required information is left
I recommennd lotting at the printed information to see this progress happening

Edit: Awkward part, I can't download the dataset to post an answer to 
Rosalind. Maybe another time.
"""

ID = 'Q5SLP9'
# get the site info as .txt
url = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + ID +
                             ".txt").read()
filtered_list = []
# turn the byte information to normal text
info_list = (url.decode("utf-8").split("\n"))
for i in info_list:
    # if p: is in the line it contains information about protein function
    if 'P:' in i:
        a = i.split(":") # cut it down
        print(a)
        for j in a:
            # cut it down a little more
            m = j.split(";")
            print(m)
            filtered_list.append(m)

for i in filtered_list:
    # exception needed as not all items in the list has two strings
    try:
        if 'IEA' in i[1]:
            print(i[0])
    except IndexError:
        pass
