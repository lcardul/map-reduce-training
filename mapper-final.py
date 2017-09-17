#! /usr/bin/env python
import sys

# Legge un file
in_file = open("test.txt","r")
text = in_file.read()
in_file.close()

# Scrive output su file
out_file = open("out-mapper.txt","w")

#input comes from STDIN
#remove leading and trailing whitespace
#line=line.strip()
#split the line into words
words=text.split()
	
#increase counters
print ('\n stampa a video e poi su file out-mapper.txt \n')
for word in words:
    print (word,1)
	#scrittura sul file di output 
    out_file.write('%s\t%s \n' %(word, 1))
out_file.close()