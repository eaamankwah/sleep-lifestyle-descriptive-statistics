# 😴 Sleep Health & Lifestyle — Statistical Analysis

> **A complete descriptive statistics pipeline** for exploring sleep quality, physical activity, cardiovascular health, and lifestyle patterns across 374 adults — featuring multi-measure centre & spread analysis, outlier detection, and publication-quality visualisations.

<br>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-1.12-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Key Findings](#-key-findings)
- [Architecture](#-architecture)
- [Repository Structure](#-repository-structure)
- [Installation & Usage](#-installation--usage)
- [Statistical Methods](#-statistical-methods)
- [Visualisations](#-visualisations)
- [Results Summary](#-results-summary)
- [Report](#-report)
- [References](#-references)
- [License](#-license)

---

## 🔍 Project Overview

Sleep disorders and poor sleep quality represent a growing public health crisis — the CDC estimates that over one-third of adults fail to get sufficient sleep each night, with downstream effects on cardiovascular health, cognitive function, and metabolic health.

This project delivers a **rigorous, multi-measure descriptive statistical analysis** of the Sleep Health and Lifestyle Dataset, answering three core analytical questions:

| # | Question | Method |
|---|----------|--------|
| 1 | How are physical activity minutes distributed — symmetric or skewed? | Mean · Median · Mode comparison |
| 2 | What is the true spread of daily step counts? | SD · IQR · Range · Variance |
| 3 | Are there anomalous heart rate values indicating cardiovascular risk? | 1.5 × IQR fence · Boxplot outlier detection |

The analysis goes beyond single-statistic summaries to provide **multiple measures of centre and spread** for every variable, using the mean–median relationship as a reliable distributional shape diagnostic throughout.

---

## 📊 Dataset

**Source:** [Sleep Health and Lifestyle Dataset — Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

| Attribute | Detail |
|-----------|--------|
| **Records** | 374 individuals |
| **Features** | 13 variables |
| **Population** | Working-age adults |
| **Age Range** | 27 – 59 years |
| **Format** | CSV |
| **Missing Values** | None in primary analytical variables |

### Variable Type Classification

| Data Type | Variable(s) | Range / Categories |
|-----------|-------------|-------------------|
| **Continuous** | Sleep Duration, Age | 5.8–8.5 hrs · 27–59 yrs |
| **Integer** | Physical Activity Level, Daily Steps, Heart Rate | 30–90 min · 3,000–10,000 · 65–86 bpm |
| **Ordinal Categorical** | Quality of Sleep, Stress Level | 1–10 ordered scale |
| **Nominal Categorical** | Gender, Occupation, BMI Category, Sleep Disorder | 2 · 11 · 4 · 3 unique values |

### Occupations Represented

`Software Engineer` · `Doctor` · `Nurse` · `Teacher` · `Engineer` · `Accountant` · `Scientist` · `Lawyer` · `Manager` · `Sales Representative` · `Salesperson`

### Sleep Disorder Distribution

`None` · `Insomnia` · `Sleep Apnea`

---

## 💡 Key Findings

### Physical Activity — Near-Perfect Symmetry
> Mean (59.17), Median (60.00), and Mode (60) converge at a single point → **symmetric distribution**, skewness = −0.07. Ideal for parametric modelling.

### Daily Steps — Meaningful Heterogeneity
> SD = **1,618 steps**, IQR = **2,400 steps**, Range = **7,000 steps**. The contrast between range and IQR confirms moderate boundary influence from low-step participants.

### Heart Rate — Right-Skewed with Clinical Outliers
> Skewness = **+1.22**. **15 statistical outliers** detected above the upper IQR fence of 78 bpm (values: 80–86 bpm). Mean (70.17) > Median (70.00) confirms the rightward pull. These individuals may represent elevated cardiovascular risk warranting clinical follow-up.

---

## 🏗️ Architecture

The project follows a clean four-stage data science pipeline — from raw CSV ingestion through to a fully rendered analytical report.

```mermaid
flowchart TD
    %% ── Stage 1: Data Ingestion ──────────────────────────────────────────────
    subgraph S1["🗂️  STAGE 1 · Data Ingestion & Validation"]
        direction TB
        A1(["📁 Raw CSV File\nsleep_health_and_lifestyle_dataset.csv"])
        A2["📥 Load with pandas\nread_csv()"]
        A3["🔍 Structural Audit\n374 rows · 13 columns"]
        A4["🏷️ Variable Classification\nContinuous · Integer\nOrdinal · Nominal"]
        A5{{"✅ Data Valid?\nNo nulls in primary vars"}}
        A1 --> A2 --> A3 --> A4 --> A5
    end

    %% ── Stage 2: Statistical Computation ────────────────────────────────────
    subgraph S2["📐  STAGE 2 · Statistical Computation"]
        direction TB
        B1["📊 Measures of Centre\nMean · Median · Mode"]
        B2["📏 Measures of Spread\nSD · Variance · Range · IQR"]
        B3["📐 Quartile Analysis\nQ1 · Q3 · IQR Fences"]
        B4["⚠️ Outlier Detection\n1.5 × IQR Rule\n15 Heart Rate Outliers Found"]
        B5["📉 Skewness Coefficients\nPhysical Activity: −0.07\nHeart Rate: +1.22\nDaily Steps: +0.18"]
        B6[["🔁 Mean vs Median\nDistribution Shape\nDiagnostic"]]
        B1 --> B3
        B2 --> B3
        B3 --> B4
        B4 --> B5
        B5 --> B6
    end

    %% ── Stage 3: Visualisation ───────────────────────────────────────────────
    subgraph S3["🎨  STAGE 3 · Visualisation"]
        direction LR
        C1["📈 Heart Rate\nHistogram\n+ Mean & Median\nReference Lines"]
        C2["📦 Heart Rate\nBoxplot\n+ Annotated\nOutliers"]
        C3["📈 Physical Activity\nHistogram\n+ Mean, Median\n& Mode Lines"]
        C4["📦 Daily Steps\nBoxplot\n+ IQR Visual"]
        C5(["💾 Export PNG\n150 dpi\nHigh Resolution"])
        C1 & C2 & C3 & C4 --> C5
    end

    %% ── Stage 4: Reporting ───────────────────────────────────────────────────
    subgraph S4["📄  STAGE 4 · Reporting"]
        direction TB
        D1["✍️ Executive Summary\n200–300 words"]
        D2["📝 Problem Statement\n+ Dataset Description"]
        D3["🛠️ Solution Statement\n+ Architecture"]
        D4["📊 Statistical Findings\nTables per Variable"]
        D5["🏁 Conclusion\n+ Value Statement"]
        D6["📚 References\n10 Academic Sources"]
        D7(["📄 sleep_health_report.docx\nFully Formatted Word Report"])
        D1 --> D2 --> D3 --> D4 --> D5 --> D6 --> D7
    end

    %% ── Flow between stages ──────────────────────────────────────────────────
    A5 -- "✅ Pass" --> B1
    A5 -- "✅ Pass" --> B2
    B6 --> C1
    B6 --> C3
    B4 --> C2
    B3 --> C4
    C5 --> D4
    B6 --> D4

    %% ── Styling ──────────────────────────────────────────────────────────────
    classDef stage1Node    fill:#1e3a5f,stroke:#4a9eff,stroke-width:2px,color:#e8f4fd,font-weight:bold
    classDef stage1Input   fill:#0d2137,stroke:#4a9eff,stroke-width:2px,color:#90caf9,font-weight:bold
    classDef stage1Check   fill:#1565c0,stroke:#4a9eff,stroke-width:2px,color:#e3f2fd

    classDef stage2Node    fill:#1b3a2f,stroke:#4caf7d,stroke-width:2px,color:#e8f5e9,font-weight:bold
    classDef stage2Key     fill:#0a2318,stroke:#4caf7d,stroke-width:2px,color:#a5d6a7,font-weight:bold

    classDef stage3Node    fill:#4a1942,stroke:#ce93d8,stroke-width:2px,color:#fce4ec,font-weight:bold
    classDef stage3Output  fill:#2d0f3a,stroke:#ce93d8,stroke-width:2px,color:#e1bee7,font-weight:bold

    classDef stage4Node    fill:#3e2000,stroke:#ffb74d,stroke-width:2px,color:#fff8e1,font-weight:bold
    classDef stage4Output  fill:#1a0d00,stroke:#ffb74d,stroke-width:2px,color:#ffe0b2,font-weight:bold

    classDef subgraphS1 fill:#e8f4fd,stroke:#1e3a5f,stroke-width:3px,color:#0d2137
    classDef subgraphS2 fill:#e8f5e9,stroke:#1b3a2f,stroke-width:3px,color:#0a2318
    classDef subgraphS3 fill:#fce4ec,stroke:#4a1942,stroke-width:3px,color:#2d0f3a
    classDef subgraphS4 fill:#fff8e1,stroke:#3e2000,stroke-width:3px,color:#1a0d00

    class A2,A3,A4 stage1Node
    class A1 stage1Input
    class A5 stage1Check
    class B1,B2,B3,B4,B5 stage2Node
    class B6 stage2Key
    class C1,C2,C3,C4 stage3Node
    class C5 stage3Output
    class D1,D2,D3,D4,D5,D6 stage4Node
    class D7 stage4Output

    style S1 fill:#dbeafe,stroke:#1e3a5f,stroke-width:3px,color:#1e3a5f
    style S2 fill:#dcfce7,stroke:#1b3a2f,stroke-width:3px,color:#1b3a2f
    style S3 fill:#fae8ff,stroke:#4a1942,stroke-width:3px,color:#4a1942
    style S4 fill:#fef9c3,stroke:#3e2000,stroke-width:3px,color:#3e2000
```

### Stage Descriptions

| Stage | Name | Libraries | Output |
|-------|------|-----------|--------|
| **1** | Data Ingestion & Validation | `pandas` | Typed DataFrame, variable classification |
| **2** | Statistical Computation | `pandas`, `numpy`, `scipy.stats` | Summary statistics, outlier detection |
| **3** | Visualisation | `matplotlib` | 4-panel histogram & boxplot PNG |
| **4** | Reporting | `python-docx` | Formatted Word report |

---

## 📁 Repository Structure

```
sleep-health-analysis/
│
├── 📄 README.md                          # This file
│
├── 📊 data/
│   └── sleep_health_and_lifestyle_dataset.csv   # Raw dataset (374 × 13)
│
├── 🐍 sleep_analysis.py                  # Main analysis script
│   ├── Data loading & type classification
│   ├── Measures of centre (mean, median, mode)
│   ├── Measures of spread (SD, variance, range, IQR)
│   ├── Outlier detection (1.5 × IQR fence)
│   └── 4-panel visualisation export
│
├── 📈 outputs/
│   ├── heart_rate_distribution.png       # Histogram + boxplot: Heart Rate
│   ├── physical_activity_distribution.png  # Histogram: Physical Activity
│   ├── daily_steps_boxplot.png           # Boxplot: Daily Steps
│   └── sleep_analysis_plots.png         # Combined 4-panel plot
│
└── 📝 sleep_health_report.docx           # Full analytical report (Word)
    ├── Executive Summary
    ├── Problem Statement
    ├── Dataset Description
    ├── Solution Statement
    ├── Architecture
    ├── Statistical Findings (with tables)
    ├── Conclusion
    ├── Value Statement
    └── References (10 sources)
```

---

## ⚙️ Installation & Usage

### Prerequisites

```bash
Python 3.9+
```

### 1 · Clone the Repository

```bash
git clone https://github.com/your-username/sleep-health-analysis.git
cd sleep-health-analysis
```

### 2 · Install Dependencies

```bash
pip install pandas numpy matplotlib scipy
```

Or using a requirements file:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
pandas>=2.0.0
numpy>=1.26.0
matplotlib>=3.8.0
scipy>=1.12.0
```

### 3 · Place the Dataset

```bash
# Place the CSV in the project root or update the path in sleep_analysis.py
cp /path/to/sleep_health_and_lifestyle_dataset.csv ./data/
```

### 4 · Run the Analysis

```bash
python sleep_analysis.py
```

**Expected console output:**

```
Dataset shape: (374, 13)

=== Physical Activity (minutes) ===
  Mean   : 59.17
  Median : 60.00
  Mode   : [60]
  Skewness: -0.0704

=== Daily Steps ===
  Mean        : 6816.84
  Median      : 7000.00
  Std Dev     : 1617.92
  Variance    : 2617651.14
  Minimum     : 3000
  Maximum     : 10000
  Range       : 7000
  Q1          : 5600.0
  Q3          : 8000.0
  IQR         : 2400.0
  Skewness    : 0.1783

=== Heart Rate ===
  Mean     : 70.17
  Median   : 70.00
  Std Dev  : 4.14
  Min      : 65,  Max: 86
  IQR      : 4.0
  Skewness : 1.2248
  Outliers (> 78.0 bpm): 15 values

Plot saved as sleep_analysis_plots.png
```

---

## 📐 Statistical Methods

### Measures of Centre

The project computes all three measures of centre for each numerical variable, using their relationship as a primary distributional shape diagnostic:

| Relationship | Distribution Shape |
|---|---|
| Mean ≈ Median ≈ Mode | **Symmetric** (normal-like) |
| Mean > Median > Mode | **Right-skewed** (positive) |
| Mean < Median < Mode | **Left-skewed** (negative) |

### Measures of Spread

Multiple spread measures are reported together because each captures a different aspect of variability:

| Measure | Sensitivity to Outliers | Best Used When |
|---------|------------------------|----------------|
| **Range** | Very High | Quick total span reference |
| **Standard Deviation** | High | Symmetric distributions |
| **Variance** | High | Modelling inputs requiring squared units |
| **IQR** | None (robust) | Skewed data or when outliers are present |

### Outlier Detection

The **1.5 × IQR fence rule** is applied to Heart Rate:

```
Lower fence = Q1 − (1.5 × IQR) = 68 − 6 = 62 bpm
Upper fence = Q3 + (1.5 × IQR) = 72 + 6 = 78 bpm

Outliers detected: 15 values between 80 and 86 bpm
```

---

## 📈 Visualisations

The script generates a 4-panel figure (`sleep_analysis_plots.png`) with the following panels:

| Panel | Variable | Chart Type | Key Features |
|-------|----------|------------|--------------|
| A | Heart Rate | Histogram | Mean & Median reference lines |
| B | Heart Rate | Boxplot | Annotated outliers in red |
| C | Physical Activity | Histogram | Mean, Median & Mode reference lines |
| D | Daily Steps | Boxplot | IQR visualised via whiskers |

Individual high-resolution exports are also saved:
- `heart_rate_distribution.png` — Histogram + boxplot side-by-side
- `physical_activity_distribution.png` — Histogram with all three centre measures
- `daily_steps_boxplot.png` — Standalone boxplot

---

## 📋 Results Summary

### Physical Activity Level

| Measure | Value | Type |
|---------|-------|------|
| Mean | **59.17 min** | Centre |
| Median | **60.00 min** | Centre |
| Mode | **60 min** | Centre |
| Standard Deviation | **20.78 min** | Spread |
| Variance | **431.76 min²** | Spread |
| Range | **45 min (30–75)** | Spread |
| IQR | **30 min (Q1=45, Q3=75)** | Spread |
| Skewness | **−0.07 (symmetric)** | Shape |

### Daily Steps

| Measure | Value | Type |
|---------|-------|------|
| Mean | **6,816.84 steps** | Centre |
| Median | **7,000 steps** | Centre |
| Mode | **8,000 steps** | Centre |
| Standard Deviation | **1,617.92 steps** | Spread |
| Variance | **2,617,651 steps²** | Spread |
| Range | **7,000 (3,000–10,000)** | Spread |
| IQR | **2,400 (Q1=5,600, Q3=8,000)** | Spread |
| Skewness | **+0.18 (near-symmetric)** | Shape |

### Heart Rate

| Measure | Value | Type |
|---------|-------|------|
| Mean | **70.17 bpm** | Centre |
| Median | **70.00 bpm** | Centre |
| Mode | **70 bpm** | Centre |
| Standard Deviation | **4.14 bpm** | Spread |
| Range | **21 bpm (65–86)** | Spread |
| IQR | **4 bpm (Q1=68, Q3=72)** | Spread |
| Skewness | **+1.22 (right-skewed)** | Shape |
| Outliers | **15 values (80–86 bpm)** | Anomaly |

---

## 📝 Report

A full professional analytical report (`sleep_health_report.docx`) is included in the repository. It contains:

- **Executive Summary** — High-level overview of all findings
- **Problem Statement** — Public health context and analytical gaps addressed
- **Dataset Description** — Variable types, ranges, and structure
- **Solution Statement** — Multi-measure statistical framework rationale
- **Architecture** — Four-stage pipeline description with summary table
- **Key Statistical Findings** — Detailed results tables for all three variables
- **Conclusion** — Synthesis of distributional profiles and clinical implications
- **Value Statement** — Methodological, clinical, and strategic value articulated
- **References** — 10 academic and technical sources in APA format

---

## 📚 References

1. Centers for Disease Control and Prevention. (2022). *Sleep and sleep disorders: Data and statistics.* https://www.cdc.gov/sleep/data-statistics.html
2. Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.
3. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science and Engineering*, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55
4. Kaggle. (2023). *Sleep health and lifestyle dataset.* https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset
5. McKinney, W. (2022). *Python for data analysis* (3rd ed.). O'Reilly Media.
6. National Sleep Foundation. (2023). *Sleep health index.* https://www.sleepfoundation.org
7. NumPy Development Team. (2023). *NumPy documentation: Statistical functions.* https://numpy.org/doc/stable/reference/routines.statistics.html
8. pandas Development Team. (2023). *pandas documentation.* https://pandas.pydata.org/docs/
9. Triola, M. F. (2021). *Elementary statistics* (14th ed.). Pearson Education.
10. World Health Organisation. (2019). *Sleep and health: A public health perspective.* WHO Press.

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

**Built with Python · pandas · NumPy · Matplotlib · SciPy**

*Sleep Health & Lifestyle Statistical Analysis — February 2026*

</div>
