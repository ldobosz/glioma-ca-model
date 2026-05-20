TREATMENT_STARTS = [20, 40, 60]

rule all:
    input:
        "results/figures/growth_curve_untreated.png",
        "results/figures/spatial_snapshots.png",
        "results/figures/treatment_comparison.png",
        "results/figures/treated_vs_untreated.png"

rule run_untreated:
    output:
        "results/growth_untreated.npy"
    script:
        "scripts/run_untreated.py"

rule run_treated:
    output:
        "results/growth_treated_{start}.npy"
    wildcard_constraints:
        start="\d+"
    script:
        "scripts/run_treated.py"

rule plot_growth:
    input:
        "results/growth_untreated.npy"
    output:
        "results/figures/growth_curve_untreated.png"
    script:
        "scripts/plot_growth.py"

rule plot_comparison:
    input:
        untreated="results/growth_untreated.npy",
        treated_20="results/growth_treated_20.npy",
        treated_40="results/growth_treated_40.npy",
        treated_60="results/growth_treated_60.npy"
    output:
        "results/figures/treatment_comparison.png",
        "results/figures/treated_vs_untreated.png",
        "results/figures/spatial_snapshots.png"
    script:
        "scripts/plot_comparison.py"