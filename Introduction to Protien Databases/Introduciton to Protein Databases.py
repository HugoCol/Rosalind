from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs
# separated
# by commas

record = SwissProt.parse(handle) # use SwissProt.parse for multiple proteins

records = dir(record)

print(records)