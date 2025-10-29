#!/bin/bash -e

# Set up LocalColabFold directory
CURRENTPATH=$(pwd)
COLABFOLDDIR="${CURRENTPATH}/localcolabfold"
mkdir -p "${COLABFOLDDIR}"

# Create conda environment
conda update -n base conda -y
conda create -n localcolabfold -c conda-forge -c bioconda \
    python=3.10 openmm==7.7.0 pdbfixer==1.8.1 \
    kalign2=2.04 hhsuite=3.3.0 mmseqs2=15.6f452 -y
conda activate localcolabfold

# Install ColabFold and Jaxlib
pip install --no-warn-conflicts \
    "colabfold[alphafold-minus-jax] @ git+https://github.com/sokrypton/ColabFold"
pip install "colabfold[alphafold]"
pip install --upgrade "jax[cuda12]"==0.4.28
pip install --upgrade tensorflow
pip install silence_tensorflow

# Fix LocalColabFold
pushd "$(conda info --base)/envs/localcolabfold/lib/python3.10/site-packages/colabfold"
# Use 'Agg' for non-GUI backend
sed -i -e "s#from matplotlib import pyplot as plt#import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt#g" plot.py
# modify the default params directory
sed -i -e "s#appdirs.user_cache_dir(__package__ or \"colabfold\")#\"${COLABFOLDDIR}/colabfold\"#g" download.py
# suppress warnings related to tensorflow
sed -i -e "s#from io import StringIO#from io import StringIO\nfrom silence_tensorflow import silence_tensorflow\nsilence_tensorflow()#g" batch.py
# remove cache directory
rm -rf __pycache__
popd

# Download weights
python -m colabfold.download
