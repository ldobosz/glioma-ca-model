import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from run_simulation import run_simulation

os.makedirs('results/figures', exist_ok=True)

none   = np.load(snakemake.input.untreated)
early  = np.load(snakemake.input.treated_20)
mid    = np.load(snakemake.input.treated_40)
late   = np.load(snakemake.input.treated_60)
steps  = range(len(none))

# Wykres porównawczy
plt.figure(figsize=(11, 6))
plt.plot(steps, none,  label='No treatment',    color='black',  linewidth=2)
plt.plot(steps, early, label='Early (step 20)', color='green',  linewidth=2)
plt.plot(steps, mid,   label='Mid (step 40)',   color='orange', linewidth=2)
plt.plot(steps, late,  label='Late (step 60)',  color='red',    linewidth=2)
plt.axvline(x=20, color='green',  linestyle='--', alpha=0.4)
plt.axvline(x=40, color='orange', linestyle='--', alpha=0.4)
plt.axvline(x=60, color='red',    linestyle='--', alpha=0.4)
plt.xlabel('Simulation step', fontsize=13)
plt.ylabel('Total cell count', fontsize=13)
plt.title('Tumor growth: treated vs untreated', fontsize=15)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(snakemake.output[0], dpi=150)
plt.close()

# Snapshoty przestrzenne
cmap = ListedColormap(['white', 'red', 'orange', 'dimgray'])
grid_none,  _ = run_simulation(n_steps=100, grid_size=201, treatment_start=None, seed=42)
grid_early, _ = run_simulation(n_steps=100, grid_size=201, treatment_start=20,   seed=42)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(grid_none,  cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
axes[0].set_title('No treatment (step 100)', fontsize=13)
axes[0].axis('off')
axes[1].imshow(grid_early, cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
axes[1].set_title('Early treatment - start step 20- step 100', fontsize=13)
axes[1].axis('off')
legend_elements = [
    Patch(facecolor='red',     label='Proliferating'),
    Patch(facecolor='orange',  label='Quiescent'),
    Patch(facecolor='dimgray', label='Necrotic'),
    Patch(facecolor='white', edgecolor='black', label='Empty')
]
fig.legend(handles=legend_elements, loc='lower center', ncol=4, fontsize=11)
plt.suptitle('Tumor structure: treated vs untreated', fontsize=15)
plt.tight_layout()
plt.savefig(snakemake.output[1], dpi=150)
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, n_steps in enumerate([30, 60, 100]):
    grid_snap, _ = run_simulation(n_steps=n_steps, grid_size=201, treatment_start=None, seed=42)
    axes[i].imshow(grid_snap, cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
    axes[i].set_title(f'Step {n_steps}', fontsize=13)
    axes[i].axis('off')
fig.legend(handles=legend_elements, loc='lower center', ncol=4, fontsize=11)
plt.suptitle('Tumor spatial structure over time', fontsize=15)
plt.tight_layout()
plt.savefig(snakemake.output[2], dpi=150)
plt.close()