This assignment focuses on analyzing the Saccharomyces cerevisiae Pyruvate Decarboxylase gene (PDC) using various bioinformatics tools. The primary objectives are:

Retrieve the PDC gene sequence from NCBI.
Perform BLAST against different yeast strains to identify single nucleotide polymorphisms (SNPs).
Translate both the reference and SNP-containing sequences into amino acids.
Predict the functional impact of selected SNPs using SIFT (or PolyPhen).
The overarching goal is to determine whether certain SNPs in the PDC gene affect protein function (deleterious) or are likely tolerated/neutral.

2. Step-by-Step Overview
2.1 Step 1: Choosing the Reference Sequence (Why NM_001181931.1?)
Gene Selection: We focused on the PDC1 gene because PDC1 is the major isoform among PDC1, PDC5, and PDC6, responsible for a large share of pyruvate decarboxylase activity in yeast.
NCBI Entry: We used NCBI (https://www.ncbi.nlm.nih.gov/) to locate the mRNA sequence for S. cerevisiae PDC1 and selected NM_001181931.1 because it is a well-annotated partial mRNA entry for the indolepyruvate decarboxylase 1 gene in strain S288C.
Key Points:

This entry was chosen for clarity, completeness, and its popularity in existing literature on S. cerevisiae PDC1.
Downloaded using a short Python script (or EntrezDirect) to ensure reproducibility.
2.2 Step 2: BLAST Parameters and SNP Selection
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
3. Final Results: SNP Effects
Below is a concise table of nucleotide-level SNPs identified, the resulting amino acid changes (if any), and predicted functional effect from SIFT:

Nucleotide Position	Nucleotide Change	AA Position	AA Change	SIFT/Functional Impact
163	G → C	55	A → P	Tolerated
164	C → G	55	A → G	Tolerated
316	G → T	106	A → S	Tolerated
617	C → T	206	A → V	Tolerated
618	T → C	– (synonymous)	None	No effect (synonymous)
623	T → C	208	V → A	Tolerated
624	C → T	– (synonymous)	None	No effect (synonymous)
757	G → A	253	D → N	Affects protein function (Deleterious)
758	A → G	253	D → G	Affects protein function (Deleterious)
1007	C → A	336	T → N	Tolerated
1521	T → C	– (synonymous)	None	No effect (synonymous)
1611	A → G	– (synonymous)	None	No effect (synonymous)
1612	A → G	538	I → V	Tolerated
1614	C → T	– (synonymous)	None	No effect (synonymous)
Key Observations:

Most SNPs are either synonymous (no amino acid change) or Tolerated (SIFT indicates minimal functional impact).
Two SNPs at nucleotide positions 757 (G → A) and 758 (A → G) affect the same codon (amino acid 253: D → N or D → G). These changes are predicted to affect protein function (likely deleterious).
4. Conclusion
Sequence Retrieval: We chose NM_001181931.1 because it is the partial mRNA for PDC1 in S. cerevisiae strain S288C and is widely cited.
BLAST & SNPs: By comparing this reference to multiple yeast strains via BLAST, we identified several SNPs. We focused on those recurring in multiple strains to ensure significance.
Reading Frame: We used the biologically relevant open reading frame (matching the annotated PDC1 start codon).
SNP Impact:
Most substitutions are either synonymous or Tolerated.
Two particular substitutions (nucleotide positions 757 and 758) produce changes in the same amino acid (253) that SIFT predicts to be deleterious, likely affecting PDC1 enzyme function.
Overall, these findings demonstrate that while S. cerevisiae PDC1 harbors many SNPs across different strains, only a minority are predicted to adversely impact the enzyme’s activity.

5. Files and Organization
code.py: Python script using Biopython Entrez.efetch to download the PDC1 mRNA from NCBI.
PDC1_mRNA_sequence.fasta: FASTA file of the reference PDC1 gene.
Blast_results_.txt: Output from BLASTN showing top alignments and identified SNP positions.
modified_sequences.txt: Reference plus SNP-substituted sequences at the nucleotide level.
aa_comparison_full_results.txt: Detailed amino acid translations and SIFT predictions.
README (this file): Summarizes the methodology, results, and final conclusions.
