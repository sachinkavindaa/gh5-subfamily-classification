#!/bin/bash
#SBATCH --time=24:00:00          # Run time in hh:mm:ss
#SBATCH --mem=100gb       # Maximum memory required per CPU (in megabytes)
#SBATCH --job-name=hmmscan
#SBATCH --error=/work/yinlab/mislam17/course_project_1/part_2/job.%J.err
#SBATCH --output=/work/yinlab/mislam17/course_project_1/part_2/job.%J.out
#SBATCH --partition=yinlab,batch,guest
#SBATCH --mail-user=mislam17@huskers.unl.edu
#SBATCH --mail-type=ALL

ml hmmer/3.3
hmmscan --domtblout gh31_hmmscan.out.dm dbCAN-fam-HMMs.txt.v14 /work/yinlab/mislam17/course_project_1/part_1/batch_protein_sequences.fasta > gh31_hmmscan.out
