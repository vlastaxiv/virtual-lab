"""Constants for the transcriptomics design project."""

from pathlib import Path
from virtual_lab.agent import Agent
from virtual_lab.prompts import SCIENTIFIC_CRITIC

# Meetings constants
num_iterations = 5
num_rounds = 3

# Models
model = "gpt-4o-2024-08-06"
model_mini = "gpt-4o-mini-2024-07-18"

# Discussion paths
discussions_dir = Path("discussions")
workflow_phases = [
    "team_selection",
    "project_specification",
    "tools_selection",
    "implementation_agent_selection",
    "workflow_design",
]

human_eval_phases = ["human_eval"]
phases = workflow_phases + human_eval_phases
discussions_phase_to_dir = {phase: discussions_dir / phase for phase in phases}

# Prompts
background_prompt = """
You are working on a transcriptomic research project to identify genes associated with metronidazole resistance in the human parasite Giardia intestinalis.

You have a unique resistant line named BER, derived from a human patient, which has maintained stable resistance for years in culture. You also have five sensitive lines: isolates 2, 8, 40, 41, and 24.

For each isolate (both resistant BER and sensitive lines), you have RNA-seq data from control samples (without metronidazole) and from treated samples (with the same metronidazole concentration), all cultured under identical microaerobic conditions.

The goal is to identify the true molecular mechanisms of metronidazole resistance and distinguish them from general drug responses and baseline strain differences.
"""
transcriptomics_prompt = "Your team previously finished wet lab work. It has RNAseq results from Illumina isntrument with basic pre-processing."

experimental_results_prompt = """
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
"""


# Set up agents

# Team lead
principal_investigator = Agent(
    title="Principal Investigator",
    expertise="applying artificial intelligence to biomedical research, transcriptomics, RNA-seq analysis, microbial drug resistance, Giardia intestinalis biology, experimental design for multi-factorial studies",
    goal="identify the molecular mechanisms of metronidazole resistance in Giardia intestinalis by properly analyzing transcriptomic data and distinguishing true resistance from confounding factors and perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to re-analyze the RNA-seq data using artificial intelligence for biomedicine, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
    model=model,
)

# Scientific critic
scientific_critic = SCIENTIFIC_CRITIC

# Specialized science agents
statistician = Agent(
        title="Bioinformatics Statistician",
        expertise="multi-factorial statistical modeling, RNA-seq analysis, DESeq2, edgeR",
        goal="develop and implement a robust multi-factorial model to distinguish resistance-specific expression changes from baseline strain differences and general drug responses",
        role="perform differential expression analysis using advanced statistical methodologies, ensuring robust control for confounding variables and appropriate statistical thresholds",
        model=model,
    )

parasitologist = Agent(
        title="Molecular Parasitologist",
        expertise="Giardia intestinalis biology, protozoan drug resistance mechanisms, transcriptomics",
        goal="interpret gene expression changes in the context of Giardia biology and elucidate potential resistance mechanisms",
        role="provide biological insights and context for the transcriptomic data, ensuring relevance to Giardia physiology and pathology",
        model=model,
    )

computational_biologist = Agent(
        title="Computational Biologist",
        expertise="R/Bioconductor, Python, functional annotation, protein function prediction",
        goal="execute computational analyses and annotate Giardia genes, including putative and hypothetical proteins",
        role="perform functional annotation and prediction using sequence homology, domain analysis, and comparative genomics tools",
        model=model,
    )

software_developer = Agent(
        title="Bioinformatics Software Developer",
        expertise="R/Bioconductor, Python, data processing automation, visualization",
        goal="develop and maintain scripts and pipelines for RNA-seq data processing and visualization, ensuring reproducibility",
        role="implement the statistical models and data visualization tools, automating workflows for efficient data analysis",
        model=model,
    )

# Team members
team_members = (
        statistician,
        parasitologist,
        computational_biologist,
        software_developer,
    )