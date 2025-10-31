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

To address the agenda for the meeting and ensure a comprehensive approach to uncovering the molecular basis of metronidazole resistance in Giardia intestinalis, I'll select a team of four scientists with complementary expertise and skills. This team will address the analytical challenges and contribute to an integrative, biologically meaningful analysis. Here is the proposed team:

```python
team = [
    Agent(
        title="Biostatistician",
        expertise="multi-factorial statistical modeling, RNA-seq analysis, DESeq2, edgeR",
        goal="develop robust statistical models to separate resistance effects from confounding factors and ensure accurate differential expression results",
        role="design and implement the statistical framework for the RNA-seq analysis, including FDR correction and meaningful log2FC cutoffs",
        model=model,
    ),
    Agent(
        title="Computational Biologist",
        expertise="Giardia intestinalis biology, protozoan drug resistance mechanisms, functional genomics",
        goal="interpret differential expression results in the context of Giardia biology and identify key resistance pathways",
        role="conduct enrichment and pathway analysis (GO, KEGG, Reactome) and rank candidate resistance genes for validation",
        model=model,
    ),
    Agent(
        title="Bioinformatics Software Engineer",
        expertise="automated workflows, R/Bioconductor, Python, reproducible research",
        goal="develop and maintain reproducible, automated pipelines for RNA-seq analysis and visualization",
        role="implement the analysis pipeline, ensuring seamless integration of R and Python code, and produce publication-quality visualizations",
        model=model,
    ),
    Agent(
        title="Protein Function Prediction Specialist",
        expertise="protein function prediction, sequence homology, domain analysis, structural prediction",
        goal="annotate and characterize putative/hypothetical proteins linked to resistance",
        role="apply AI-assisted prediction tools and comparative genomics to infer functions of unknown genes, and perform literature mining for functional insights",
        model=model,
    ),
]
```

This team will work collaboratively to address the re-analysis requirements, ensuring that we achieve a statistically sound, biologically interpretable, and reproducible analysis of the RNA-seq data. We will prioritize the identification of transcriptomic changes and pathways specific to natural metronidazole resistance, aiming to uncover new insights and hypotheses that can drive further experimental validation.

