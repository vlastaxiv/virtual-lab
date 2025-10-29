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

Certainly! Below is a detailed step-by-step workflow for the transcriptomic analysis to identify genes associated with metronidazole resistance in Giardia intestinalis. This workflow is designed to address the limitations of the previous analysis and ensure a comprehensive and accurate study.

### Step 1: Data Preparation and Quality Control
**Objective:** Prepare and validate data for differential expression analysis.

#### Inputs:
- `A2_count_matrix.txt`
- `raw_counts_matrix_forDEseq2_prednorm.csv`
- `sample_metadata_forDEseq2_prednorm.csv`
- Quality control reports (`242114199_multiqc_report.html`, `SEQme-NGS_report-Order_no_242114199.pdf`)
- Reference genome annotation files (`genome_annotation/`)

#### Outputs:
- Cleaned, normalized count matrices
- Quality control report

#### Procedure:
1. **Read Data and Metadata:**
   - Load count data and sample metadata.
   
2. **Quality Control:**
   - Confirm mapping rates and RIN scores are consistent across samples.
   - Check library size, gene count distributions, and batch effects using PCA and clustering.
   - Validate alignment files using `multiqc_report.html`.
   - Confirm sample integrity (no outliers) using visualizations like PCA and heatmaps.

3. **Normalization:**
   - Use DESeq2's normalization method to adjust for sequencing depth and RNA composition.
   - Validate normalization by plotting density distributions of normalized counts.

4. **Output QC Report:**
   - Document quality checks and normalization results.

### Step 2: Statistical Analysis using DESeq2
**Objective:** Perform differential expression analysis using a multi-factorial model.

#### Inputs:
- Normalized count matrix
- Sample metadata (`sample_metadata_forDEseq2_prednorm.csv`)

#### Outputs:
- Differential expression results with adjusted p-values
- Interaction terms for genotype and treatment

#### Procedure:
1. **Define DESeq2 Model:**
   - Implement a multi-factorial design: `~ strain + treatment + strain:treatment`
   - This model captures main effects (strain, treatment) and their interaction (resistance mechanisms).

2. **Run DESeq2 Analysis:**
   - Calculate differential expression with FDR-adjusted p-values.
   - Identify genes with significant interaction effects (indicative of resistance mechanisms).

3. **Quality Check:**
   - Validate model fit by inspecting dispersion estimates and sample distances.
   - Use MA plots and volcano plots to visualize differential expression results.

### Step 3: Functional Annotation and Pathway Enrichment
**Objective:** Understand the biological context of differentially expressed genes.

#### Inputs:
- List of significantly differentially expressed genes

#### Outputs:
- Pathway enrichment results
- Functional annotation summaries

#### Procedure:
1. **Gene Annotation:**
   - Map differentially expressed genes to known functions using available annotations.

2. **Pathway Enrichment Analysis:**
   - Perform KEGG, GO, and Reactome enrichment analyses.
   - Identify pathways significantly enriched among differentially expressed genes.

3. **Quality Check:**
   - Verify functional relevance by cross-referencing known resistance pathways.

### Step 4: Putative Protein Characterization
**Objective:** Characterize the proteins encoded by candidate genes.

#### Inputs:
- Candidate resistance genes

#### Outputs:
- Functional prediction reports
- Protein interaction networks

#### Procedure:
1. **Protein Function Prediction:**
   - Use tools like InterProScan to predict protein domains and functions.

2. **Protein-Protein Interaction Networks:**
   - Use STRING or similar databases to identify potential interaction partners.

3. **Quality Check:**
   - Validate predictions against known protein functions in Giardia and related species.

### Step 5: Visualization and Reporting
**Objective:** Summarize and communicate findings effectively.

#### Inputs:
- Comprehensive analysis results

#### Outputs:
- Visualizations: heatmaps, pathway diagrams, interaction networks
- Final report with actionable insights

#### Procedure:
1. **Visualization:**
   - Create gene expression heatmaps, pathway diagrams, and interaction networks.
   - Use visualization tools to present results clearly and effectively.

2. **Reporting:**
   - Compile comprehensive report including methodology, findings, and biological implications.
   - Provide ranked list of candidate genes for experimental validation.

3. **Quality Check:**
   - Ensure all visualizations accurately reflect data and analysis results.

### Integration of Analysis Components
- **Data Preparation:** Ensures robust input for statistical analysis.
- **Statistical Analysis:** Feeds into functional annotation for biological insights.
- **Functional and Protein Characterization:** Provides context for visualization and reporting.
- **Visualization and Reporting:** Integrates all findings for comprehensive communication.

### Key Decision Points
- **Model Selection:** Ensure multi-factorial design addresses interaction effects.
- **Thresholds for Significance:** Use FDR-adjusted p-values to reduce false positives.
- **Candidate Gene Selection:** Prioritize based on statistical and biological relevance.

This workflow is designed to be modular and reproducible, with clear documentation and quality checks to ensure the reliability of each step. Adjustments may be made as necessary based on intermediate findings and feedback from the research team.

