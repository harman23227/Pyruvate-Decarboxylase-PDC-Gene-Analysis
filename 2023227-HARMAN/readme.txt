BLAST Parameters and SNP Selection
BLAST Program: We used BLASTN to compare the PDC1 mRNA sequence against the core_nt database.

Parameters:

Word size: 28
Expect value: 0.05
Match/Mismatch: default
Low Complexity Filter: yes
Gap costs: default
Selecting Strains: We took the top hits (e.g., ~10 strains) from BLAST results.

Identifying SNPs:

We examined alignment mismatches across the top yeast strains.
Only mismatches consistently appearing in multiple strains were marked as SNPs.
We ignored rare single occurrences in one strain.
Key Points:

We used a threshold that SNPs found in at least ~50% of the top hits were considered “significant.”
This helps ensure we analyze functionally relevant or commonly occurring variants.
2.3 Step 3: Justifying the Reading Frame
Reading Frame: Since PDC1 is a coding gene, we aligned it with the known start codon (ATG) and used the annotated frame from the NCBI record (the official open reading frame).
Translation: We used an online tool (e.g., ExPASy Translate) or Biopython to convert the reference mRNA (and each SNP variant) into protein sequences.
Why One Frame? Because only one of the six possible frames corresponds to the actual PDC1 protein. The other five frames do not match the known biologically functional reading frame.
2.4 Step 4: SIFT Analysis and SNP Impact
SIFT (Sorting Intolerant From Tolerant) predicts whether an amino acid substitution affects protein function based on sequence homology and the physical properties of amino acids.
Approach:
We took each SNP that caused a nonsynonymous codon change.
Created a modified protein sequence (i.e., introducing that single substitution).
Submitted it to SIFT (or a local version if available) to assess whether the substitution is Tolerated or Deleterious (“Affects Protein Function”).
Interpretation:
“Tolerated” means the substitution is unlikely to disrupt protein function.
“Deleterious” or “Affects protein function” indicates the SNP might impair or alter protein function significantly.
 
 Key Observations:

Most SNPs are either synonymous (no amino acid change) or Tolerated (SIFT indicates minimal functional impact).
Two SNPs at nucleotide positions 757 (G → A) and 758 (A → G) affect the same codon (amino acid 253: D → N or D → G). These changes are predicted to affect protein function (likely deleterious).
. Conclusion
Sequence Retrieval: We chose NM_001181931.1 because it is the partial mRNA for PDC1 in S. cerevisiae strain S288C and is widely cited.
BLAST & SNPs: By comparing this reference to multiple yeast strains via BLAST, we identified several SNPs. We focused on those recurring in multiple strains to ensure significance.
Reading Frame: We used the biologically relevant open reading frame (matching the annotated PDC1 start codon).
SNP Impact:
Most substitutions are either synonymous or Tolerated.
Two particular substitutions (nucleotide positions 757 and 758) produce changes in the same amino acid (253) that SIFT predicts to be deleterious, likely affecting PDC1 enzyme function.
Overall, these findings demonstrate that while S. cerevisiae PDC1 harbors many SNPs across different strains, only a minority are predicted to adversely impact the enzyme’s activity.
