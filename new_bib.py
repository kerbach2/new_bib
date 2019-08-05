#README
# Read a .tex file
## Create a list of all citation IDs 
# Read master bibliography
# Write a new .bib file that contains only the entires listed in the .tex file


## Create a list of all citation IDs 

# Read a .tex file

print("What is the tex file you'd like to scan?  (Don't forget to include the extension.)")

tex = input()


with open(tex, encoding="utf8") as openedtex:
	read_texFile = openedtex.read()
	
#print(read_texFile) # prints the tex file

words = read_texFile.split()

citations = []

for word in words:
	if word[0:6] == "\cite{" or word[0:7] == "\citep{":
		citations.append(word)
	#need to figure out how to take care of citations with page numbers---e.g. \citep[p. 23]{acquavia2008}
	#if word[0:6] == "\cite[" or word[0:7] == "\citep[":
	#	citations.append(word)
	# for letter in word:
		# if letter == "\\":
			# print(word)

IDS1 = []
IDS2 = []
IDS3 = []
IDS4 = []
IDS5 = []
multiples = []
multiples_space = []
multiples_split = []

for item in citations:
	IDS1.append(item.replace("\cite{", ""))

for item in IDS1:
	IDS2.append(item.replace("\citep{", ""))

for item in IDS2: 
	IDS3.append(item.replace("},", ""))

for item in IDS3: 
	IDS4.append(item.replace("}.", ""))

for item in IDS4: 
	IDS5.append(item.replace("}", ""))

for item in IDS5:
	for letter in item:
		if letter == ",":
			multiples.append(item)

	
for item in IDS5[:]: #iterates over a copy of the list IDS5
	if item in multiples:
		IDS5.remove(item)

for item in multiples:
	multiples_space.append(item.replace(",", " "))

for item in multiples_space:
	multiples_split.append(item.split())


flat_list = []
for sublist in multiples_split:
    for item in sublist:
        flat_list.append(item)

for item in flat_list:
	IDS5.append(item)

#remove duplicates in a list by first converting it to a dictionary, which is not supposed to allow two items with the same key

temp_dict = {}
temp_dict = dict.fromkeys(IDS5) #turns the list into a dictionary, which does remove items with the same key
final_list = []
final_list = list(temp_dict) #turns the dictionary back into a list


#print(final_list)




# Read master bibliography

import bibtexparser #bibtexparser is a python package for parsing bibtex files

print("What is the bib file you'd like to scan? (Don't forget to include the extension.)")

bib = input()

import bibtexparser #bibtexparser is a python package for parsing bibtex files

with open(bib, encoding="utf8") as bibtex_file: #opens the bib file
  bib_database = bibtexparser.load(bibtex_file) #parses the bib file's entries as a list of dictionaries

#print(bib_database.entries) #prints the list of dictionaries

# Write a new .bib file that contains only the entires listed in the .tex file

#make a new list of dictionaries that contains only the dictionaries who's key 'ID' has a value that is equivalent to one of the items in final_list


new_bib = []

for item in bib_database.entries:
	if item['ID'] in final_list:
		new_bib.append(item)

#print(new_bib)


#make the new list of dictionaries into a bib file
#from bibtexparser README: https://bibtexparser.readthedocs.io/en/master/tutorial.html#step-1-prepare-a-bibtex-file


from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

db = BibDatabase()
db.entries = new_bib

print("What would you like to call your new bib file? (Don't forget to include the extension.)")

new_bib_file = input()

writer = BibTexWriter()
with open(new_bib_file, 'w') as bibfile:
    bibfile.write(writer.write(db))

print("Your new tex file has been created!")



