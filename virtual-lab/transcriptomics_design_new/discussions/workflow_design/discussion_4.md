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

### Step-by-Step Workflow for Transcriptomics Analysis

#### 1. Data Preparation and Quality Control

**Inputs**:
- Raw gene count matrix: `A2_count_matrix.txt`
- Sample metadata: `sample_metadata_forDEseq2_prednorm.csv`
- Quality control reports: `242114199_multiqc_report.html`, `SEQme-NGS_report-Order_no_242114199.pdf`

**Outputs**:
- Processed count matrix ready for differential expression analysis
- Summary report of quality control

**Steps**:
1. **Data Validation and Import**:
   - Check the integrity and format of input files.
   - Load count matrix and metadata into R for further analysis.

2. **Initial Quality Control**:
   - Review `multiqc_report.html` for sequencing and alignment quality.
   - Assess data distribution and variance using PCA (`PCA_top500_log2_autoscale_colored_labels.png`).
   - Confirm sample metadata accuracy and completeness.

3. **Filtering and Normalization**:
   - Filter out low-expressed genes across all samples (e.g., genes with CPM < 1 in more than half of the samples).
   - Normalize count data using DESeq2’s variance stabilizing transformation (VST) or regularized log transformation (rlog).

4. **Quality Control Post-Filtering**:
   - Re-evaluate data distribution via PCA post-normalization.
   - Generate diagnostic plots (e.g., boxplots of transformed counts) to ensure data is well-normalized.

#### 2. Statistical Analysis (DESeq2 Multi-Factorial Model)

**Inputs**:
- Normalized count matrix
- Sample metadata

**Outputs**:
- Differential expression results with adjusted p-values and log2 fold changes

**Steps**:
1. **Model Design**:
   - Construct a multi-factorial design matrix with factors for genotype (resistant vs. sensitive), treatment (control vs. metronidazole), and their interaction.
   - Formula: `~ genotype + treatment + genotype:treatment`

2. **Differential Expression Analysis**:
   - Fit DESeq2 model to data using the design matrix.
   - Perform likelihood ratio tests to assess the significance of genotype, treatment, and interaction effects.

3. **Result Generation**:
   - Extract results for:
     - Genes differentially expressed due to resistance (BER vs. sensitive lines under control conditions).
     - Genes differentially expressed in response to treatment (comparing treated vs. control within each genotype).
     - Interaction effects to isolate genes with resistance-specific drug responses.

4. **Statistical Significance and Thresholds**:
   - Apply FDR correction (e.g., Benjamini-Hochberg) to account for multiple testing.
   - Set thresholds for significance (adjusted p-value < 0.05) and biological relevance (absolute log2FC > 1.5).

#### 3. Functional Annotation (Pathway Enrichment)

**Inputs**:
- List of differentially expressed genes (DEGs)

**Outputs**:
- Enrichment analysis results for pathways and gene ontology terms

**Steps**:
1. **Gene Set Enrichment Analysis**:
   - Use tools like topGO, clusterProfiler, or Enrichr to perform GO and KEGG pathway enrichment analysis.
   - Identify significantly enriched biological processes, cellular components, and molecular functions among DEGs.

2. **Interpretation and Integration**:
   - Highlight pathways potentially related to drug resistance or response.
   - Identify core genes contributing to enriched pathways.

#### 4. Putative Protein Characterization

**Inputs**:
- List of prioritized candidate genes

**Outputs**:
- Functional and structural annotations of candidate proteins

**Steps**:
1. **Protein Annotation**:
   - Use databases like UniProt and Pfam to retrieve functional annotations.
   - Predict protein domains and motifs using InterProScan.

2. **Structural Analysis**:
   - Use tools like Phyre2 or SWISS-MODEL for protein structure prediction if 3D information could provide insights into function.

3. **Cross-reference with Literature**:
   - Conduct a literature search to correlate candidate genes with known resistance mechanisms or related phenotypes.

#### 5. Visualization and Reporting

**Inputs**:
- Results from differential expression, enrichment, and protein characterization

**Outputs**:
- Comprehensive report with visualizations

**Steps**:
1. **Visualization**:
   - Create volcano plots, heatmaps, and MA plots for DEGs.
   - Illustrate enriched pathways using pathway diagrams.
   - Highlight protein interactions and networks using tools like Cytoscape.

2. **Reporting**:
   - Compile a detailed report summarizing methods, results, and biological interpretations.
   - Include visualizations and tables for key findings.
   - Provide a ranked list of candidate resistance genes with supporting evidence for experimental validation.

### Integration of Components

- **Data Preparation and QC**: Ensures high-quality input data for analysis.
- **Statistical Analysis**: Provides robust identification of DEGs through a multi-factorial model.
- **Functional Annotation and Protein Characterization**: Offers biological context and mechanistic insights into resistance.
- **Visualization and Reporting**: Communicates findings effectively, facilitating further research and validation.

### Key Decision Points

1. **Statistical Model Design**: Ensuring the model accurately reflects the experimental design and addresses potential confounding factors.
2. **Thresholds for Significance and Biological Relevance**: Balancing between detecting true positives and minimizing false positives.
3. **Pathway Enrichment Interpretations**: Distinguishing between significant findings that are of biological relevance and those that may be artifacts.

This workflow, if followed carefully, should provide comprehensive insights into the molecular mechanisms of metronidazole resistance in Giardia intestinalis and guide future experimental validation efforts.

