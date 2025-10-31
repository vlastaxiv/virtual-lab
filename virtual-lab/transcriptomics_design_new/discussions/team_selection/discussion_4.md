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

Below is the selection of team members designed to address the specific analytical challenges of this transcriptomics project. This team combines expertise in statistical modeling, RNA-seq analysis, biological interpretation, and software development, ensuring a comprehensive approach to uncovering the molecular basis of metronidazole resistance in *Giardia intestinalis*.

```python
team = [
    Agent(
        title="Statistical Bioinformatician",
        expertise="multi-factorial statistical modeling, differential expression analysis, DESeq2, edgeR",
        goal="develop a robust statistical framework to differentiate true resistance mechanisms from confounding factors",
        role="design and implement multi-factorial models, ensuring statistical rigor and appropriate control for variability",
        model=model,
    ),
    Agent(
        title="Parasitologist and Protozoan Biologist",
        expertise="Giardia intestinalis biology, protozoan drug resistance mechanisms, gene expression interpretation",
        goal="provide biological insights on gene expression changes and potential resistance mechanisms in Giardia",
        role="interpret the biological relevance of findings, and identify candidate genes associated with resistance",
        model=model,
    ),
    Agent(
        title="Computational Biologist",
        expertise="functional annotation, protein function prediction, comparative genomics, AI-assisted gene function prediction",
        goal="annotate and characterize putative/hypothetical proteins linked to metronidazole resistance",
        role="apply bioinformatics tools and databases to predict protein functions and infer biological pathways",
        model=model,
    ),
    Agent(
        title="Bioinformatics Software Engineer",
        expertise="pipeline development, automation, R/Bioconductor, Python, reproducible research",
        goal="develop a reproducible and automatable analysis pipeline integrating R and Python environments",
        role="implement and maintain code for differential expression analysis, visualization, and functional annotation",
        model=model,
    )
]
```

## Response to the Agenda

1. **Differential Expression Analysis**:
   - I will oversee the design of a robust multi-factorial statistical model to accurately separate resistance mechanisms from confounding factors. This includes working closely with the Statistical Bioinformatician to identify constitutive and induced resistance effects, ensuring the application of appropriate FDR-adjusted thresholds and meaningful log2FC cutoffs.

2. **Functional Analysis**:
   - The Parasitologist and Protozoan Biologist, in collaboration with the Computational Biologist, will focus on identifying enriched pathways and annotating genes. We'll leverage databases like GO, KEGG, and Reactome to elucidate biological processes involved in resistance and highlight candidates for experimental validation.

3. **Integrative and Exploratory Analysis**:
   - We'll apply co-expression and network clustering to explore gene interactions and modules. The Computational Biologist will use AI-assisted tools like AlphaFold for structural predictions to aid functional insights, while the Bioinformatics Software Engineer will ensure pipeline automation and integration.

4. **Deliverables**:
   - The team will develop reproducible R/Python scripts for data analysis, facilitating seamless workflow execution. We will produce publication-quality visualizations and propose biological hypotheses that explain the mechanisms of metronidazole resistance, contributing to a deeper understanding of this clinically relevant issue.

I am looking forward to working with this team to explore and uncover the true molecular underpinnings of metronidazole resistance in *Giardia intestinalis*. Through collaborative efforts, we aim to generate insights with significant implications for protozoan drug resistance research.

