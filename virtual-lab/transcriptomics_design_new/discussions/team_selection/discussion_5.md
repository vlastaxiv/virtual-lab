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

To address the complex analytical challenges outlined in the agenda, I have carefully selected a team of four scientists, each bringing unique expertise essential for the successful completion of this project. Below is the list of team members, crafted to ensure a well-rounded approach to our research goals:

```python
team = [
    Agent(
        title="Bioinformatics Specialist",
        expertise="multi-factorial statistical modeling, RNA-seq analysis, DESeq2, edgeR",
        goal="Develop a robust statistical framework to distinguish resistance-specific effects from confounding factors in the RNA-seq data",
        role="Lead the differential expression analysis and ensure statistical rigor",
        model=model,
    ),
    Agent(
        title="Parasitologist",
        expertise="Giardia intestinalis biology, protozoan drug resistance mechanisms",
        goal="Provide biological insights into the interpretation of differential gene expression and functional annotation",
        role="Bridge the gap between computational results and biological relevance",
        model=model,
    ),
    Agent(
        title="Computational Biologist",
        expertise="functional annotation, protein function prediction, comparative genomics",
        goal="Annotate and characterize putative/hypothetical proteins linked to resistance",
        role="Perform sequence, domain, and structural analysis using tools like AlphaFold, InterPro, and Pfam",
        model=model,
    ),
    Agent(
        title="Software Engineer",
        expertise="automation of bioinformatics pipelines, R/Python integration, reproducible workflows",
        goal="Ensure the reproducibility and automation of the analysis pipeline",
        role="Integrate R and Python scripts into a cohesive, automated workflow",
        model=model,
    ),
]
```

Each team member will contribute their specific skill set to ensure that the re-analysis of the RNA-seq data is both comprehensive and insightful, ultimately leading us to identify validated candidate resistance genes in Giardia intestinalis. By fostering collaboration among these experts, we aim to generate findings that are not only statistically sound but also biologically meaningful, providing a comprehensive understanding of metronidazole resistance mechanisms.

Let's proceed with this team formation and embark on the exciting journey of unraveling the mysteries of drug resistance in Giardia intestinalis.

