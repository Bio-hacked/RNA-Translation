from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

#def RNA():
#    pass

def RNAtranslation():

   

    RNA_sequence = ''
    
    Protein_code = { 

   "F": ["UUU", "UUC"],
   "L":["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
   "I": ["AUU", "AUC", "AUA"],
   "M": ["AUG"],
   "V": ["GUU", "GUC", "GUA", "GUG"],
   "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], 
   "P": ["CCU", "CCC", "CCA", "CCG"],
   "T": ["ACU", "ACC", "ACA", "ACG"],
   "A": ["GCU", "GCC", "GCA", "GCG"],
   "Y": ["UAU", "UAC"],
   "Stop": ["UAA", "UAG", "UGA"],
   "H": ["CAU", "CAC"],
   "Q": ["CAA", "CAG"],
   "N": ["AAU", "AAC"],
   "K": ["AAA", "AAG"],
   "D": ["GAU", "GAC"],
   "E": ["GAA", "GAG"],
   "C": ["UGU", "UGC"],
   "W": ["UGG"],
   "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
   "G": ["GGU", "GGC", "GGA", "GGG"], 

  }
  
   #now that the codon table is created, create a loop that is able to iterate through the RNA sequence as a strings
    Amino_string = ""

    if request.method == 'POST' and 'RNA_sequence' in request.form:
        RNA_sequence = request.form.get('RNA_sequence')
        
   #Begin by making a for loop that skips to the 3rd character after current index
        for iteration in range(0, len(RNA_sequence), 3):
    # Now build a piece of code that checks if the current index plus the next 2 characters are in the library 

            for iteration_2 in Protein_code:
      

      # Now I want to iterate through the lists contained in each dictionary keyword
                for iteration_3 in Protein_code[iteration_2]:

                    if RNA_sequence[iteration: iteration + 3] == iteration_3:
                        Amino_string += iteration_2
                    elif RNA_sequence[iteration: iteration + 3] in Protein_code["Stop"]:
                        " Stop codon reached"
                        break
    
    return render_template('index.html',Amino_string=Amino_string, RNA_sequence=RNA_sequence)


app.run()