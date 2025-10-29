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

To ensure a robust analysis of the RNA-seq data to identify genes associated with metronidazole resistance in Giardia intestinalis, we need a detailed and structured workflow. This will allow us to address the limitations of the previous analysis and meet our project goals. Below is a comprehensive workflow:

### Step-by-Step Workflow for Transcriptomic Analysis

#### 1. Data Preparation and Quality Control

**Inputs:**
- `A2_count_matrix.txt`
- `sample_metadata_forDEseq2_prednorm.csv`
- `genome_annotation/`

**Outputs:**
- Cleaned and normalized count matrix
- QC reports

**Steps:**
1. **Load and Process Count Data:**
   - Import the raw count matrix and sample metadata.
   - Verify data integrity by cross-referencing sample labels and conditions with metadata.

2. **Initial Quality Control:**
   - Use tools like FastQC and MultiQC to generate quality reports for raw and mapped reads (check `242114199_multiqc_report.html`).

3. **Normalization:**
   - Normalize counts using the DESeq2 or edgeR package in R to account for library size differences.

4. **Quality Check:**
   - Conduct principal component analysis (PCA) to visualize sample clustering by condition and genotype.
   - Generate density plots and boxplots to assess distribution and detect outliers.

#### 2. Statistical Analysis (DESeq2 Multi-factorial Model)

**Inputs:**
- Normalized count matrix
- Sample metadata

**Outputs:**
- List of differentially expressed genes (DEGs)
- Interaction effect results

**Steps:**
1. **Multi-factorial DESeq2 Analysis:**
   - Set up a multi-factorial model in DESeq2 to evaluate the effects of genotype (resistant vs. sensitive), treatment (control vs. metronidazole), and their interaction.
   - Model: `~ genotype + treatment + genotype:treatment`
   - Focus on interaction terms to identify genes uniquely associated with resistance in the BER line.

2. **Statistical Thresholds:**
   - Apply FDR-adjusted p-values (< 0.05) to control for multiple testing.
   - Use a more stringent log2FC cutoff based on biological relevance after consulting domain-specific literature.

3. **Quality Check:**
   - Generate volcano and MA plots to visually inspect significant DEGs.
   - Examine dispersion estimates and model fit diagnostics.

#### 3. Functional Annotation (Pathway Enrichment)

**Inputs:**
- List of DEGs

**Outputs:**
- Enriched pathways and GO terms

**Steps:**
1. **Functional Enrichment Analysis:**
   - Use databases like KEGG, GO, and Reactome to perform pathway enrichment analysis for significant DEGs.
   - Identify pathways disproportionately represented in the resistant vs. sensitive lines.

2. **Quality Check:**
   - Validate enrichment results by cross-checking with literature for known resistance pathways.

#### 4. Putative Protein Characterization

**Inputs:**
- Genes or proteins of interest (from enriched pathways)

**Outputs:**
- Annotations and functional predictions

**Steps:**
1. **Characterization:**
   - Use BLAST, InterProScan, or similar tools to predict protein domains and motifs.
   - Annotate known and predicted functions of candidate resistance genes.

2. **Quality Check:**
   - Cross-reference predicted protein functions with known databases (e.g., UniProt).

#### 5. Visualization and Reporting

**Inputs:**
- Analysis results (DEGs, enriched pathways)

**Outputs:**
- Comprehensive report and visualizations

**Steps:**
1. **Visualization:**
   - Create heatmaps for expression patterns of key genes.
   - Generate bar plots for enriched pathways.

2. **Reporting:**
   - Compile a detailed report including methods, results, and biological interpretations.
   - Include a table of top candidate resistance genes with prioritization for validation studies.

3. **Quality Check:**
   - Ensure clarity and accuracy in all visualizations.
   - Cross-review the report for consistency and completeness.

### Integration and Key Decision Points

- **Integration:**
  - Each step builds upon the previous, feeding outputs as inputs for subsequent analysis.
  - Ensure interoperability by maintaining consistent data formats and identifiers.

- **Key Decision Points:**
  - Decide on appropriate log2FC thresholds post-initial analysis based on biological significance.
  - Prioritize candidate genes for validation based on pathway involvement, expression consistency, and literature support.

This structured workflow ensures a comprehensive and reproducible analysis to elucidate the molecular mechanisms of metronidazole resistance in Giardia intestinalis.

