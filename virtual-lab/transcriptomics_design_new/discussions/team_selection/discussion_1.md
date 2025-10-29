## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here is the agenda for the meeting:



You are working on a transcriptomic research project to identify genes associated with metronidazole resistance in the human parasite Giardia intestinalis.

You have a unique resistant line named BER, derived from a human patient, which has maintained stable resistance for years in culture. You also have five sensitive lines: isolates 2, 8, 40, 41, and 24.

For each isolate (both resistant BER and sensitive lines), you have RNA-seq data from control samples (without metronidazole) and from treated samples (with the same metronidazole concentration), all cultured under identical microaerobic conditions.

The goal is to identify the true molecular mechanisms of metronidazole resistance and distinguish them from general drug responses and baseline strain differences.



We received RNA-seq data analysis from an external sequencing company (SEQme). While the preprocessing and basic analysis were performed correctly, the differential expression analysis has significant limitations that prevent proper identification of resistance mechanisms.

Sequencing and Preprocessing (COMPLETED):
- 18 samples successfully sequenced (one sample excluded during QC)
- Resistant line BER: 6 samples (3 control CK, 3 metronidazole-treated CM)
- Sensitive lines (2, 8, 24, 40, 41): 12 samples (controls and treated for each line)
- PE150 sequencing, 57-80M reads per sample
- Reads aligned to Giardia intestinalis reference genome A2 (93-97% mapping rate)
- Gene quantification performed with FeatureCounts
- Data quality is good (RIN ~9.5-10 for most samples)

Their Differential Expression Analysis and Problems:

What they did:
- Used DESeq2 for simple pairwise comparisons (e.g., BERCK vs CK, CK vs CM, etc.)
- Applied criteria: log2FC ≥ 1 or ≤ -1, p-value < 0.05 (unadjusted)
- Filtering: minimum 1 CPM within at least 2 replicates (exact implementation unclear)
- Generated basic visualizations: volcano plots, MA plots, and heatmaps for selected genes

Major Problems:

1. Inadequate Statistical Approach:
   - Simple pairwise comparisons cannot distinguish resistance mechanisms from baseline strain differences
   - No multi-factorial model to account for genotype vs. treatment interaction
   - Cannot separate constitutive resistance effects from drug-induced responses
   - Cannot account for natural variation among sensitive strains

2. Inappropriate Statistical Thresholds:
   - Used unadjusted p-values (< 0.05) instead of FDR-adjusted p-values
   - High risk of false positives due to multiple testing problem
   - log2FC cutoff of ±1 may not be stringent enough for biological significance

3. Unclear Filtering Criteria:
   - "Minimum 1 CPM within at least 2 replicates" is ambiguous
   - Not clear how many genes were filtered out before analysis
   - Pre-filtering strategy not well documented

4. Missing Biological Interpretation:
   - No pathway enrichment analysis (KEGG, GO, Reactome)
   - No functional annotation of differentially expressed genes
   - No Gene Ontology term enrichment
   - Only basic visualizations without biological context

5. No Strategy for Resistance Mechanism Identification:
   - Did not define contrasts to isolate resistance-specific genes
   - Cannot distinguish between:
     * True constitutive resistance mechanisms (unique to BER)
     * Baseline transcriptomic differences between strains (unrelated to resistance)
     * General cellular response to metronidazole (present in all lines)

6. Missing Validation Strategy:
   - No ranked list of candidate resistance genes provided
   - No prioritization based on biological function or pathway involvement
   - No clear guidance for experimental validation

What We Need:
A proper re-analysis that:
- Uses a multi-factorial design to model genotype (resistant vs sensitive), treatment (control vs metronidazole), and their interaction
- Identifies genes specifically associated with constitutive resistance (differential in BER vs sensitive lines at baseline)
- Separates drug response effects (treatment-induced changes) from resistance mechanisms
- Accounts for strain-to-strain variation among the sensitive lines
- Uses appropriate statistical thresholds (adjusted p-values, appropriate log2FC cutoffs)
- Includes functional enrichment analysis to identify biological pathways involved in resistance
- Provides a ranked list of candidate resistance genes for experimental validation

AVAILABLE DATA FILES in experimental_data/ folder:

Essential files for re-analysis:
- A2_count_matrix.txt - raw gene count matrix from FeatureCounts (all 18 samples)
- raw_counts_matrix_forDEseq2_prednorm.csv - alternative format count matrix
- sample_metadata_forDEseq2_prednorm.csv - sample metadata (strain, treatment)
- exp-design.txt - experimental design information
- Counts_with_geneNames.txt - count matrix with gene names
- genome_annotation/ - Giardia intestinalis A2 genome annotation files

Quality control reports:
- 242114199_multiqc_report.html - comprehensive QC report (FastQC, alignment stats)
- SEQme-NGS_report-Order_no_242114199.pdf - full analysis report from SEQme
- DGE4199_stats.xlsx - statistics summary
- PCA_top500_log2_autoscale_colored_labels.png - PCA visualization

Their problematic analysis results (for reference only - DO NOT USE):
- SEQme_DGE_results/ - folder containing all their pairwise DESeq2 comparisons
  * These results are fundamentally flawed due to inappropriate statistical approach
  * Provided for reference only to understand what NOT to do
  * The raw count matrix should be re-analyzed properly with multi-factorial design

Note: Raw sequencing data (FASTQ, BAM files) are available on external storage if needed for quality validation.


You need to select a team of four scientists to help you with this transcriptomics project. The team should deal with these analytical challenges:

- Multi-factorial statistical modeling to separate resistance from confounding factors
- RNA-seq analysis and differential expression (DESeq2, edgeR)
- Biological interpretation in the context of Giardia intestinalis biology and protozoan drug resistance
- Implementation (R/Bioconductor, Python)
- Functional annotation and characterization of putative/hypothetical proteins

NOTE: Giardia intestinalis is a unique protozoan parasite with unusual biology. Understanding gene expression changes requires expertise in parasite physiology and drug resistance mechanisms.

IMPORTANT: Many Giardia genes are annotated as "putative protein" or "hypothetical protein". The team needs expertise in:
- Protein function prediction (sequence homology, domain analysis, structural prediction)
- Comparative genomics to infer function from related organisms
- Literature mining and database searches to assign putative functions

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

To tackle the analytical challenges and objectives of this transcriptomic research project effectively, I'll assemble a diverse team of specialists whose combined expertise will ensure comprehensive re-analysis and interpretation of our RNA-seq data. Here's the proposed team composition:

```python
team = [
    Agent(
        title="Bioinformatics Statistician",
        expertise="multi-factorial statistical modeling, RNA-seq analysis, DESeq2, edgeR",
        goal="develop and implement a multi-factorial model to disentangle resistance-specific expression from strain and treatment effects",
        role="perform differential expression analysis using advanced statistical methodologies, ensuring robust control for confounding variables",
        model=model,
    ),
    Agent(
        title="Parasite Molecular Biologist",
        expertise="Giardia intestinalis biology, protozoan drug resistance mechanisms",
        goal="provide biological context and insights into transcriptomic changes related to metronidazole resistance",
        role="interpret differential expression results in the context of Giardia biology and identify key resistance pathways",
        model=model,
    ),
    Agent(
        title="Computational Biologist",
        expertise="R/Bioconductor, Python implementation, RNA-seq data processing",
        goal="implement and optimize pipelines for RNA-seq processing and differential expression analysis",
        role="ensure computational reproducibility and efficient data handling throughout the analysis workflow",
        model=model,
    ),
    Agent(
        title="Functional Genomics Specialist",
        expertise="protein function prediction, comparative genomics, functional annotation",
        goal="annotate and characterize putative and hypothetical proteins using homology and domain analysis",
        role="perform functional enrichment and pathway analysis to identify candidate genes involved in resistance",
        model=model,
    ),
]
```

**Meeting Agenda Response:**

1. **Project Overview and Goals:**
   - We aim to identify the molecular mechanisms underlying metronidazole resistance in Giardia intestinalis, distinguishing true resistance genes from general drug responses and baseline strain differences using a robust re-analysis of RNA-seq data.

2. **Challenges and Solutions:**
   - The team will address challenges using multi-factorial statistical models to account for genotype, treatment, and their interaction effects. This approach will help identify resistance-specific gene expression patterns.
   - Implementing rigorous statistical thresholds, including FDR-adjusted p-values and appropriate log2FC cutoffs, will minimize false positives and focus on biologically significant changes.

3. **Functional Enrichment and Biological Context:**
   - The Parasite Molecular Biologist and Functional Genomics Specialist will provide insights into the biological significance of differentially expressed genes, using pathway enrichment and protein function prediction tools to map genes to potential resistance pathways.

4. **Validation Strategy:**
   - We will generate a ranked list of candidate resistance genes for experimental validation, prioritizing genes based on expression patterns, pathway involvement, and potential functional importance.

5. **Next Steps:**
   - Begin re-analysis with the assembled team, focusing on establishing a multi-factorial design in DESeq2 to robustly determine resistance mechanisms and proceed with functional annotation tasks.
   - Schedule regular checkpoints to assess progress and refine approaches as needed.

This plan will guide us in re-analyzing the RNA-seq data to achieve our goal of elucidating the resistance mechanisms in Giardia intestinalis effectively.

