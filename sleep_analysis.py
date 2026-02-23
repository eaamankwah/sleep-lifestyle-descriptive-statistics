"""
Sleep Health & Lifestyle Dataset – Statistical Analysis
Sections: Variable Types, Physical Activity, Daily Steps, Heart Rate Distribution
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ── 0. Load Data ──────────────────────────────────────────────────────────────
df = pd.read_csv("sleep_health_and_lifestyle_dataset.csv")
print("Dataset shape:", df.shape)
print(df.dtypes)

# ── 1. Variable Types ─────────────────────────────────────────────────────────
# Continuous  : Sleep Duration, Age
# Integer     : Physical Activity Level, Daily Steps
# Ordinal     : Quality of Sleep (1-10 scale), Stress Level (1-10 scale)
# Nominal     : Gender, Occupation, BMI Category, Sleep Disorder

# ── 2. Physical Activity – Measures of Center ─────────────────────────────────
pa = df['Physical Activity Level']
print("\n=== Physical Activity (minutes) ===")
print(f"  Mean   : {pa.mean():.2f}")
print(f"  Median : {pa.median():.2f}")
print(f"  Mode   : {pa.mode().values}")
print(f"  Skewness: {pa.skew():.4f}")

# ── 3. Daily Steps – Measures of Spread ──────────────────────────────────────
steps = df['Daily Steps']
Q1_s = steps.quantile(0.25)
Q3_s = steps.quantile(0.75)
print("\n=== Daily Steps ===")
print(f"  Mean        : {steps.mean():.2f}")
print(f"  Median      : {steps.median():.2f}")
print(f"  Std Dev     : {steps.std():.2f}")
print(f"  Variance    : {steps.var():.2f}")
print(f"  Minimum     : {steps.min()}")
print(f"  Maximum     : {steps.max()}")
print(f"  Range       : {steps.max() - steps.min()}")
print(f"  Q1          : {Q1_s}")
print(f"  Q3          : {Q3_s}")
print(f"  IQR         : {Q3_s - Q1_s}")
print(f"  Skewness    : {steps.skew():.4f}")

# ── 4. Heart Rate – Distribution + Outliers ───────────────────────────────────
hr = df['Heart Rate']
Q1_h = hr.quantile(0.25)
Q3_h = hr.quantile(0.75)
IQR_h = Q3_h - Q1_h
upper_fence = Q3_h + 1.5 * IQR_h
lower_fence = Q1_h - 1.5 * IQR_h
outliers = hr[(hr < lower_fence) | (hr > upper_fence)]
print("\n=== Heart Rate ===")
print(f"  Mean     : {hr.mean():.2f}")
print(f"  Median   : {hr.median():.2f}")
print(f"  Std Dev  : {hr.std():.2f}")
print(f"  Min      : {hr.min()},  Max: {hr.max()}")
print(f"  IQR      : {IQR_h}")
print(f"  Skewness : {hr.skew():.4f}")
print(f"  Outliers (> {upper_fence} bpm): {len(outliers)} values")

# ── 5. Plots ──────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sleep Health & Lifestyle – Statistical Analysis', fontsize=15, fontweight='bold')

# (A) Heart Rate Histogram
ax = axes[0, 0]
ax.hist(hr, bins=15, color='steelblue', edgecolor='white', alpha=0.85)
ax.axvline(hr.mean(),   color='red',    linestyle='--', linewidth=1.8, label=f'Mean={hr.mean():.1f}')
ax.axvline(hr.median(), color='orange', linestyle='-',  linewidth=1.8, label=f'Median={hr.median():.1f}')
ax.set_title('Heart Rate – Histogram', fontweight='bold')
ax.set_xlabel('Heart Rate (bpm)')
ax.set_ylabel('Frequency')
ax.legend()

# (B) Heart Rate Boxplot
ax = axes[0, 1]
bp = ax.boxplot(hr, patch_artist=True,
                boxprops=dict(facecolor='steelblue', alpha=0.7),
                medianprops=dict(color='orange', linewidth=2),
                flierprops=dict(marker='o', color='red', markersize=7))
ax.set_title('Heart Rate – Box Plot', fontweight='bold')
ax.set_ylabel('Heart Rate (bpm)')
ax.set_xticks([1]); ax.set_xticklabels(['Heart Rate'])
ax.annotate(f'{len(outliers)} outliers\nabove {upper_fence} bpm',
            xy=(1.05, hr.max()), fontsize=9, color='red')

# (C) Physical Activity Histogram
ax = axes[1, 0]
ax.hist(pa, bins=15, color='mediumseagreen', edgecolor='white', alpha=0.85)
ax.axvline(pa.mean(),   color='red',    linestyle='--', linewidth=1.8, label=f'Mean={pa.mean():.1f}')
ax.axvline(pa.median(), color='orange', linestyle='-',  linewidth=1.8, label=f'Median={pa.median():.1f}')
ax.axvline(pa.mode()[0],color='purple', linestyle=':',  linewidth=1.8, label=f'Mode={pa.mode()[0]}')
ax.set_title('Physical Activity – Histogram', fontweight='bold')
ax.set_xlabel('Minutes of Physical Activity')
ax.set_ylabel('Frequency')
ax.legend()

# (D) Daily Steps Boxplot
ax = axes[1, 1]
ax.boxplot(steps, patch_artist=True,
           boxprops=dict(facecolor='salmon', alpha=0.7),
           medianprops=dict(color='darkred', linewidth=2),
           flierprops=dict(marker='o', color='red', markersize=7))
ax.set_title('Daily Steps – Box Plot', fontweight='bold')
ax.set_ylabel('Daily Steps')
ax.set_xticks([1]); ax.set_xticklabels(['Daily Steps'])

plt.tight_layout()
plt.savefig('sleep_analysis_plots.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nPlot saved as sleep_analysis_plots.png")
