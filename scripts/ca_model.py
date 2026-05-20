import numpy as np

EMPTY = 0
PROLIFERATING = 1
QUIESCENT = 2
NECROTIC = 3

PROLIF_PROB = 0.6
NUTRIENT_PROLIF = 0.5
NUTRIENT_QUIESC = 0.2
NUTRIENT_DECAY = 0.05   

def initialize_grid(size=101):
    grid = np.zeros((size, size), dtype=int)
    center = size // 2
    grid[center, center] = PROLIFERATING
    return grid

def compute_nutrients(grid):
    size = grid.shape[0]
    nutrients = np.ones((size, size))
    tumor_mask = grid > 0

    from scipy.ndimage import distance_transform_edt
    dist = distance_transform_edt(tumor_mask)

    nutrients = np.exp(-NUTRIENT_DECAY * dist)
    return nutrients

def get_empty_neighbors(grid, x, y):
    size = grid.shape[0]
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if grid[nx, ny] == EMPTY:
                    neighbors.append((nx, ny))
    return neighbors

def update_grid(grid):
    nutrients = compute_nutrients(grid)
    new_grid = grid.copy()
    size = grid.shape[0]

    for x in range(size):
        for y in range(size):
            if grid[x, y] == EMPTY or grid[x, y] == NECROTIC:
                continue

            n = nutrients[x, y]

            if n >= NUTRIENT_PROLIF:
                new_grid[x, y] = PROLIFERATING
            elif n >= NUTRIENT_QUIESC:
                new_grid[x, y] = QUIESCENT
            else:
                new_grid[x, y] = NECROTIC

            if new_grid[x, y] == PROLIFERATING:
                if np.random.random() < PROLIF_PROB:
                    neighbors = get_empty_neighbors(grid, x, y)
                    if neighbors:
                        nx, ny = neighbors[np.random.randint(len(neighbors))]
                        new_grid[nx, ny] = PROLIFERATING

    return new_grid

def count_cells(grid):
    return {
        'total': np.sum(grid > 0),
        'proliferating': np.sum(grid == PROLIFERATING),
        'quiescent': np.sum(grid == QUIESCENT),
        'necrotic': np.sum(grid == NECROTIC)
    }