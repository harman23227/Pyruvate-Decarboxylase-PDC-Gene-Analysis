

from Bio import Entrez, SeqIO

def retrieve_nucleotide_sequence(ncbi_id, output_fasta):
   
    Entrez.email = "harmankumar120206@gmail.com"


    with Entrez.efetch(db="nucleotide", id=ncbi_id, rettype="fasta", retmode="text") as response:
        sequence_data = response.read()


    with open(output_fasta, "w") as out_file:
        out_file.write(sequence_data)

if __name__ == "__main__":

    reference_id = "NM_001181931.1"


    fasta_filename = "PDC1_mRNA_sequence.fasta"


    retrieve_nucleotide_sequence(reference_id, fasta_filename)

 







