## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here is the agenda for the meeting:



You are part of a research initiative focused on uncovering the molecular basis of metronidazole resistance in the human parasite Giardia intestinalis.

The project investigates one unique, clinically resistant line (BER) and several sensitive lines (2, 8, 24, 40, and 41), all originally isolated from patients. 
BER is exceptional because its metronidazole resistance arose naturally in vivo and has remained stable during long-term culture, unlike laboratory-induced resistant strains. 
This makes BER a rare and biologically valuable model for studying true clinical resistance mechanisms.

The dataset includes all necessary biological controls and allows a comprehensive exploration of resistance mechanisms. 
The goal is to identify transcriptomic changes and pathways specific to natural metronidazole resistance and to highlight putative or uncharacterized genes that may represent new resistance factors.

Your task is to design and implement a complete, reproducible, and automatable analysis pipeline — from statistical modeling to functional interpretation — producing well-documented R or Python code for differential expression, visualization, and annotation. 
You may also apply modern computational tools (e.g., AlphaFold, InterPro, Pfam) to assist in functional prediction of unannotated genes. 
If additional information is required, you are encouraged to ask the project lead. Collaboration and clear reasoning are preferred.



We received RNA-seq analysis results from Illumina instrument from an external provider (SEQme). Preprocessing was correct, but the differential expression analysis was inadequate and failed to identify true resistance mechanisms. A new, statistically sound and biologically interpretable analysis is required.

Experiment summary:
- 18 samples sequenced (1 excluded after QC)
- Resistant line BER: CK (control), CM (metronidazole), plus AK/AM (anaerobic, excluded from main analysis)
- Sensitive lines: 2, 8, 24, 40, 41 — CK and CM
- Reads aligned to the Giardia intestinalis A2 reference genome (93 - 97% mapping)
- Gene quantification performed with FeatureCounts
- Main contrasts: CK vs CM within and between lines

Data location:
All input data are in the experimental_data/ folder (count matrices, metadata, genome annotation, and QC reports). 
Incorrect SEQme analyses are included for reference only (DO NOT USE). 
Raw FASTQ/BAM files are stored externally.

Main issues with SEQme analysis:
- Only pairwise DESeq2 comparisons; no multi-factorial model
- No FDR correction or clear filtering
- Missing pathway or functional interpretation

Required re-analysis:
Re-analyze RNA-seq data using an integrative, multi-layer pipeline combining statistical rigor and biological interpretation.

1. Differential expression
- Multi-factorial model: phenotype (resistant vs sensitive), treatment (control vs metronidazole), and interaction
- Identify constitutive resistance (BER vs sensitive baseline)
- Separate drug-induced vs resistance-specific effects
- Control for variability among sensitive strains
- Apply FDR-adjusted thresholds and meaningful log2FC cutoffs

2. Functional analysis
- Perform enrichment and pathway analysis (GO, KEGG, Reactome)
- Rank candidate resistance genes for validation
- Annotate putative or uncharacterized genes linked to resistance

3. Integrative and exploratory analysis
- Use co-expression or network clustering to find gene modules
- Apply AI-assisted prediction for unknown gene functions (e.g., sequence, domain, or structure-based)

Deliverables:
Provide reproducible R/Python code, publication-quality visualizations (volcano plots, PCA, heatmaps, network maps), and propose new hypotheses explaining metronidazole resistance in Giardia intestinalis.


You need to select a team of four scientists to help you with this transcriptomics project. The team should deal with these analytical challenges:

- Multi-factorial statistical modeling to separate resistance from confounding factors
- RNA-seq analysis and differential expression (DESeq2, edgeR)
- Biological interpretation in the context of Giardia intestinalis biology and protozoan drug resistance
- Implementation and development of automated, reproducible pipelines (R/Bioconductor, Python)
- Functional annotation and characterization of putative/hypothetical proteins

NOTE: Giardia intestinalis is a unique protozoan parasite with unusual biology. Understanding gene expression changes requires expertise in parasite physiology and drug resistance mechanisms.

IMPORTANT: Many Giardia genes are annotated as "putative protein" or "hypothetical protein". The team needs expertise in:
- Protein function prediction (sequence homology, domain analysis, structural prediction)
- Comparative genomics to infer function from related organisms
- Literature mining and database searches to assign putative functions

The team should also include a software-oriented member capable of automating the analysis, maintaining reproducible workflows, and integrating code across R and Python environments.
The selected scientists should complement each others expertise and collaborate as an integrated research team.

Please select the team members in the following format. You should NOT include yourself (Principal Investigator) in the list. Write the team as a Python list of Agent objects with "model=model" as the last parameter.

Agent(
    title="Principal Investigator",
    expertise="transcriptomics, RNA-seq analysis, microbial drug resistance, experimental design",
    goal="identify molecular mechanisms of metronidazole resistance in Giardia intestinalis",
    role="lead a team of experts to properly re-analyze the RNA-seq data and identify validated candidate resistance genes",
    model=model,
)

Principal Investigator, please provide your response.


Principal Investigator, please provide your response to the agenda.

## Principal Investigator

To address the analytical challenges and goals outlined in the meeting agenda, I have selected the following team of scientists with complementary expertise to ensure a thorough and insightful analysis of our RNA-seq data:

```python
team = [
    Agent(
        title="Bioinformatics Statistician",
        expertise="multi-factorial statistical modeling, differential expression analysis using DESeq2 and edgeR, data normalization, FDR correction, and RNA-seq data interpretation",
        goal="develop and implement a robust statistical framework to identify true resistance mechanisms by controlling for confounding factors and variability among samples",
        role="focus on designing and executing the statistical models necessary for differential expression analysis",
        model=model,
    ),
    Agent(
        title="Parasitologist & Drug Resistance Expert",
        expertise="Giardia intestinalis biology, protozoan physiology, drug resistance mechanisms, functional genomics, and pathway analysis",
        goal="provide biological context and interpretation for transcriptomic changes, focusing on resistance pathways",
        role="guide the functional analysis and annotation of resistance-related genes, ensuring biological relevance",
        model=model,
    ),
    Agent(
        title="Computational Biologist",
        expertise="RNA-seq analysis pipeline development, R/Bioconductor, Python scripting, and reproducible research practices",
        goal="create an automated, reproducible analysis pipeline to ensure transparency and scalability of the RNA-seq data analysis",
        role="implement and maintain the pipeline, integrating statistical models with biological data interpretation tools",
        model=model,
    ),
    Agent(
        title="Protein Function Prediction Specialist",
        expertise="protein sequence analysis, domain prediction, structural modeling (using tools like AlphaFold), comparative genomics, and literature mining",
        goal="predict functions of putative and hypothetical proteins in Giardia by leveraging computational tools and database resources",
        role="focus on annotating unknown genes and proteins, providing insights into their potential roles in metronidazole resistance",
        model=model,
    )
]
```

This team is assembled to ensure a comprehensive approach to our research initiative. Each member will bring vital expertise to distinct aspects of the project, from statistical modeling to functional annotation, providing an integrated and cohesive effort to uncover the molecular basis of metronidazole resistance in Giardia intestinalis. Our interdisciplinary collaboration will foster innovative insights and facilitate the joy of scientific discovery.

