import numpy as np
from ca_model import PROLIFERATING, QUIESCENT, NECROTIC, EMPTY

KILL_PROB_PROLIF = 0.7
KILL_PROB_QUIESC = 0.3

def apply_radiation(grid):
    new_grid = grid.copy()
    size = grid.shape[0]

    for x in range(size):
        for y in range(size):
            if grid[x, y] == PROLIFERATING:
                if np.random.random() < KILL_PROB_PROLIF:
                    new_grid[x, y] = NECROTIC

            elif grid[x, y] == QUIESCENT:
                if np.random.random() < KILL_PROB_QUIESC:
                    new_grid[x, y] = NECROTIC

    return new_grid

def fractionated_radiotherapy(grid, start_step, current_step,
                               fraction_interval=5, n_fractions=6):
    if current_step < start_step:
        return grid, False

    steps_since_start = current_step - start_step
    last_fraction = (n_fractions - 1) * fraction_interval

    if steps_since_start > last_fraction:
        return grid, False

    if steps_since_start % fraction_interval == 0:
        return apply_radiation(grid), True

    return grid, False