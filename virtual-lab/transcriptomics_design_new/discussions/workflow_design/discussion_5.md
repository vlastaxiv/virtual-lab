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


Based on the project specification, selected tools, and implementation assignments, design a detailed step-by-step workflow for the transcriptomics analysis.

The workflow should cover:
1. Data preparation and quality control
2. Statistical analysis (DESeq2 multi-factorial model)
3. Functional annotation (pathway enrichment)
4. Putative protein characterization
5. Visualization and reporting

Provide a clear, modular, and reproducible workflow with inputs, outputs, and quality checks for each step.


Here are the agenda questions that must be answered:

1. What is the complete step-by-step workflow for the analysis?

2. What are the inputs and outputs for each major step?

3. What quality control checks should be performed at each stage?

4. How will the different analysis components integrate together?

5. What are the key decision points and how should they be handled?

Principal Investigator, please provide your response to the agenda.

## Principal Investigator

To address the challenges outlined in the analysis of RNA-seq data for identifying genes associated with metronidazole resistance in Giardia intestinalis, we propose a detailed and modular workflow. This workflow will ensure robust statistical analysis, proper biological interpretation, and clear identification of candidate resistance genes for further validation. Here's the plan:

### Step-by-Step Workflow for RNA-seq Data Analysis

#### 1. **Data Preparation and Quality Control**

**Inputs:**
- `A2_count_matrix.txt`: Raw gene count matrix
- `sample_metadata_forDEseq2_prednorm.csv`: Sample metadata
- `242114199_multiqc_report.html`: QC report
- `genome_annotation/`: Giardia intestinalis genome annotation files

**Steps:**
- **Raw Data Validation:** Ensure the alignment metrics (e.g., mapping rates) reported in the QC report are consistent with expectations.
- **Normalization Check:** Verify count matrix normalization to correct for library size differences.
  
**Quality Control Checks:**
- Ensure high mapping rates (93-97%) are consistent across samples.
- Examine the RIN scores (≥9.5) to confirm RNA quality.
- Verify data preprocessing integrity (e.g., check for outliers using PCA).

**Outputs:**
- Validated count matrix and metadata ready for statistical analysis.

#### 2. **Statistical Analysis using DESeq2 Multi-Factorial Model**

**Inputs:**
- Normalized count matrix
- Sample metadata with factors: strain identity and treatment condition

**Steps:**
- **Multi-factorial Model Setup:** Use DESeq2 to set up a model accounting for genotype (resistant vs. sensitive), treatment (control vs. treated), and their interaction.
- **Contrast Definition:** Define contrasts to isolate constitutive resistance (BER vs. sensitive lines at baseline) and treatment-induced changes.
- **Adjust for Multiple Testing:** Apply FDR correction (e.g., Benjamini-Hochberg method) to control false positives.
- **Determine Significance Cutoffs:** Define biologically relevant log2 fold change thresholds (e.g., > ±1.5) for differential expression.

**Quality Control Checks:**
- Evaluate dispersion estimates and model fit diagnostics.
- Check residual plots for model assumptions.
- Perform sensitivity analysis for different FDR thresholds.

**Outputs:**
- List of differentially expressed genes with statistical significance adjusted for multiple testing.

#### 3. **Functional Annotation and Pathway Enrichment**

**Inputs:**
- List of differentially expressed genes
- Giardia intestinalis genome annotation

**Steps:**
- **Gene Ontology (GO) Analysis:** Identify enriched biological processes, cellular components, and molecular functions.
- **Pathway Enrichment (KEGG, Reactome):** Identify pathways significantly enriched among DEGs.
- **Functional Annotation:** Use databases like InterPro and Pfam for protein domain analysis.

**Quality Control Checks:**
- Compare with known literature to validate biological relevance.
- Perform cross-validation with different enrichment tools to ensure consistency.

**Outputs:**
- Enrichment analysis report with significant pathways and GO terms.

#### 4. **Putative Protein Characterization**

**Inputs:**
- List of candidate genes from functional annotation

**Steps:**
- **Protein Domain Analysis:** Identify and characterize domains using InterProScan.
- **Homology Modeling:** Predict protein structure/function with tools like Phyre2 or SWISS-MODEL.

**Quality Control Checks:**
- Validate domain predictions against known protein structures.
- Check for consistency across different characterization tools.

**Outputs:**
- Characterization report of proteins coded by candidate resistance genes.

#### 5. **Visualization and Reporting**

**Inputs:**
- Results from differential expression, enrichment, and characterization analyses

**Steps:**
- **Visualization:** Create volcano plots, heatmaps, and pathway diagrams.
- **Reporting:** Compile a comprehensive report detailing methods, results, and interpretations.

**Quality Control Checks:**
- Ensure visualizations accurately represent the data.
- Review report for clarity and completeness.

**Outputs:**
- Visualizations and a detailed report for publication or presentation.

### Integration and Decision Points

- **Integration:** Use reproducible analysis pipelines (e.g., Snakemake or Nextflow) to ensure all steps are interconnected and automated.
- **Decision Points:**
  - Choice of statistical thresholds (handle by assessing sensitivity-specificity trade-offs).
  - Selection of tools for functional annotation (based on database comprehensiveness and update frequency).
  - Validation of candidate genes (prioritize based on pathway involvement and literature support).

By following this workflow, we aim to identify robust candidate genes associated with metronidazole resistance and provide a strong foundation for further experimental validation.

