# Tp2_GL
import sys
import os
ADN_LIST=("A","C","G","T")
def fasta_read(fastafile):
    extension = os.path.splitext(fastafile)
    if extension == '.fasta' or '.fa':
        with open(fastafile,"r") as file:
            lines = file.readlines()
            print(lines)
            counter = 0
            header = ""
            for line in lines:
                counter += 1

                if line[0] == ">":
                    header = line.strip()
                else:
                    line = line.strip()
                    line = line.upper()
                    column_counter = 0
                    for char in line:
                        column_counter += 1
                        if char not in ADN_LIST:
                            print( char  + " It's not a nucl in line " + str(counter) +
                            " and column " + str(column_counter)+ " for sequence "+header[1:])
                            
    else : 
        ("Error tjis is not a fasta file")
                    

print(sys.argv)
for arg in sys.argv[1:]:
   fasta_read("/home/mahitasoa/Bureau/Prgrammation/PROJET_PYTHON/AFO/essai.fasta")
