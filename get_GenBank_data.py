# Get GenBank data for a list of record IDs

from Bio import Entrez

id_list = ['OL546428', 'OL546425', 'MN809507', 'OR115609', 'KY313829',
           'MN809506', 'MT132131', 'MN809502', 'KY313849', 'KY197997',
           'KY313856']

# Set your email address for NCBI API
Entrez.email = "aubreymoore2013@gmail.com"

for id in id_list:
    print(id)
    stream = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    with open(f'{id}.txt', 'w') as f:
        f.write(stream.read())
    stream.close()

