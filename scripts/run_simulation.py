import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ca_model import initialize_grid, update_grid, count_cells
from radiotherapy import fractionated_radiotherapy

def run_simulation(n_steps=150, grid_size=101, 
                   treatment_start=None, seed=42):
    np.random.seed(seed)
    grid = initialize_grid(grid_size)
    
    history = {
        'total': [],
        'proliferating': [],
        'quiescent': [],
        'necrotic': [],
        'radiation_steps': []
    }

    for step in range(n_steps):
        # Aplikuj radioterapię jeśli włączona
        if treatment_start is not None:
            grid, radiated = fractionated_radiotherapy(
                grid, 
                start_step=treatment_start, 
                current_step=step
            )
            if radiated:
                history['radiation_steps'].append(step)

        grid = update_grid(grid)

        counts = count_cells(grid)
        history['total'].append(counts['total'])
        history['proliferating'].append(counts['proliferating'])
        history['quiescent'].append(counts['quiescent'])
        history['necrotic'].append(counts['necrotic'])

    return grid, history


if __name__ == "__main__":
    print("Loading simulation")
    grid, history = run_simulation(n_steps=50, grid_size=51)
    print(f"Step50 - number of cells: {history['total'][-1]}")
    print("Test ready")