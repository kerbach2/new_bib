# new_bib
Program for taking a tex file and a master bib file and producing a new bib file that contains only the citations from the tex file.

How it works:
This program asks for the name of the tex file you'd like to generate a bib file for, then parses the tex file and compiles a list of citation IDs.

The program then asks for the master bib file you would like to search through for the entries of you new bib file. The bib file you name is parsed using bibtexparser (https://bibtexparser.readthedocs.io/en/master/index.html)

The program then asks for the name you'd like to give your new file and creates it from the list of citation IDs in the given tex file and the corresponding entries in the master bib file.

*Many apologies for how terrible tis code might be! This is my first coding project in a long time and I'm doing it to re-learn Python.*
