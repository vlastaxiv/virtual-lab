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

To ensure a comprehensive and scientifically rigorous re-analysis of the RNA-seq data for identifying genes associated with metronidazole resistance in Giardia intestinalis, we will adopt the following modular workflow. This approach addresses the limitations in the original analysis and leverages a multi-factorial model to separate true resistance mechanisms from general drug responses and baseline strain differences.

### 1. Data Preparation and Quality Control

#### Step 1: Data Import and Initial QC
- **Input:** 
  - `A2_count_matrix.txt` (raw gene count matrix)
  - `sample_metadata_forDEseq2_prednorm.csv` (sample metadata)
  - `242114199_multiqc_report.html` (QC report)

- **Output:**
  - Detailed report of data integrity and initial exploratory data analysis (EDA) results

- **Quality Checks:**
  - Verify data import accuracy and completeness
  - Check sample consistency with metadata
  - Confirm QC metrics from the multiqc report (e.g., read quality, mapping rates)

### 2. Statistical Analysis

#### Step 2: Data Normalization
- **Input:** Raw count matrix
- **Output:** Normalized count data suitable for differential expression analysis

- **Quality Checks:**
  - Evaluate normalization effectiveness by assessing distribution of expression values across samples

#### Step 3: Multi-Factorial Differential Expression Analysis
- **Design:**
  - Use DESeq2 with a multi-factorial model to incorporate genotype, treatment, and their interaction.
  - Model formula: `~ Genotype + Treatment + Genotype:Treatment`
  - Contrast focus: Identify genes differentially expressed in BER vs. sensitive lines (both under control and treated conditions)

- **Input:** 
  - Normalized count data
  - Experimental design matrix

- **Output:**
  - List of differentially expressed genes with adjusted p-values and log2 fold changes

- **Quality Checks:**
  - Examination of model fit via residual analysis
  - Check for significant interaction terms indicating resistance-specific effects

### 3. Functional Annotation and Enrichment Analysis

#### Step 4: Functional Enrichment
- **Input:**
  - List of differentially expressed genes

- **Output:**
  - Pathway and Gene Ontology (GO) enrichment reports

- **Quality Checks:**
  - Validate enrichment results with established biological knowledge
  - Cross-verify with multiple databases (KEGG, Reactome)

### 4. Putative Protein Characterization

#### Step 5: Protein Function Annotation
- **Input:** Differentially expressed genes list
- **Output:** Characterization of gene products (e.g., predicted protein functions, domains)

- **Quality Checks:**
  - Use multiple annotation sources for cross-validation (e.g., UniProt, Pfam)

### 5. Visualization and Reporting

#### Step 6: Visualization
- **Input:** Results from differential expression and enrichment analyses
- **Output:** Comprehensive visual report including:
  - Heatmaps, volcano plots, and MA plots (for DE genes)
  - Network diagrams for enriched pathways

- **Quality Checks:**
  - Ensure visualizations accurately represent data findings
  - Cross-reference visual outputs with statistical results

### Integration and Key Decision Points

- **Integration Strategy:**
  - Each step outputs data to be utilized by subsequent analyses, ensuring seamless workflow progression
  - Employ scripting (e.g., R scripts) to automate data flow and maintain reproducibility

- **Key Decision Points:**
  - Selection of FDR threshold for significant genes: decide based on balance between statistical rigor and biological relevance
  - Interpretation of interaction terms: ensure biological plausibility of resistance-specific findings
  - Choice of enrichment analysis databases: verify consistency across multiple sources

By following this structured workflow, we aim to address the limitations of the previous analysis and provide a robust identification of the genetic basis for metronidazole resistance in Giardia intestinalis.

