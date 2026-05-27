# glioma-ca-model

final project - Cellular automaton model of glioma growth



\# Cellular automaton model of glioma growth



A 2D cellular automaton (CA) simulation of glioblastoma (GBM) growth, 

replicating the model of Kansal et al. (2000). Extended with a fractionated 

radiotherapy module to investigate how treatment timing affects tumor volume 

and spatial structure.



\## Project Structure



&#x20;   glioma-ca-model/

&#x20;   ├── notebooks/              # Jupyter notebooks with analysis

&#x20;   ├── scripts/                # Python scripts

&#x20;   │   ├── ca\_model.py         # Core CA model

&#x20;   │   ├── radiotherapy.py     # Radiotherapy module

&#x20;   │   ├── run\_simulation.py   # Simulation runner

&#x20;   │   ├── run\_untreated.py    # Snakemake script

&#x20;   │   ├── run\_treated.py      # Snakemake script

&#x20;   │   ├── plot\_growth.py      # Snakemake script

&#x20;   │   └── plot\_comparison.py  # Snakemake script

&#x20;   ├── results/                # Output figures

&#x20;   ├── Snakefile               # Automated workflow

&#x20;   └── environment.yml         # Conda environment



\## Setup



conda env create -f environment.yml

conda activate glioma-env

pip install snakemake scipy



\## Run



snakemake --cores 1



\## results



The model replicates the three-zone tumor structure from Kansal et al.:

\-proliferating outer rim

\-quiescent inner zone

\-necrotic core



Fractionated radiotherapy reduces final tumor size by 22% regardless

of treatment start time, suggesting tumor regrowth capacity dominates

over timing effects.



\## References



A. R. Kansal et al., "Simulated brain tumor growth dynamics using a

three-dimensional cellular automaton", Journal of Theoretical Biology,

vol. 203, no. 4, pp. 367-382, 2000.



\[2] R. Stupp et al., "Radiotherapy plus concomitant and adjuvant temozolomide

for glioblastoma", N. Engl. J. Med., vol. 352, pp. 987-996, 2005.



\[3] R. Rockne et al., "Predicting the efficacy of radiotherapy in individual

glioblastoma patients in vivo: a mathematical modeling approach",

Phys. Med. Biol., vol. 55, pp. 3271-3285, 2010.

