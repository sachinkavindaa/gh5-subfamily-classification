#!/bin/bash

#SBATCH --job-name=mafft_job
#SBATCH --output=mafft_output_%j.txt
#SBATCH --error=mafft_error_%j.txt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --mem=50G
#SBATCH --time=48:00:00
#SBATCH --partition=guest,batch
#SBATCH --mail-user=mislam17@huskers.unl.edu
#SBATCH --mail-type=ALL


module load mafft

mafft --localpair --maxiterate 1000 --genafpair --thread 10 phylo_input_fasttree_100.fasta > phylo_mafft_align_1e-100.fasta
