import numpy as np
import matplotlib.pyplot as plt
import os

total = np.load(snakemake.input[0])
steps = range(len(total))

os.makedirs('results/figures', exist_ok=True)

plt.figure(figsize=(10, 6))
plt.plot(steps, total, color='black', linewidth=2)
plt.xlabel('Simulation step', fontsize=13)
plt.ylabel('Total cell count', fontsize=13)
plt.title('Tumor growth curve no treatment', fontsize=15)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(snakemake.output[0], dpi=150)
plt.close()