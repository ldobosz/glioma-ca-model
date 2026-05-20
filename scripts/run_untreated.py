import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from run_simulation import run_simulation

grid, history = run_simulation(n_steps=100, grid_size=201, treatment_start=None, seed=42)

os.makedirs('results', exist_ok=True)
np.save(snakemake.output[0], history['total'])
np.save(snakemake.output[0].replace('.npy', '_grid.npy'), grid)