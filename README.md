<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/DVC-Data%20Versioning-blueviolet?logo=dvc" alt="DVC"/>
  <img src="https://img.shields.io/badge/MLflow-Tracking-blue?logo=mlflow" alt="MLflow"/>
  <img src="https://img.shields.io/badge/SHAP-Explainability-green" alt="SHAP"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>
</p>

# 🚗 End-to-End Insurance Risk Analytics & Predictive Modeling

A comprehensive data science project that analyzes an insurance portfolio to uncover **risk patterns**, **profitability insights**, and **pricing opportunities** using advanced statistical methods, hypothesis testing, and machine learning with full reproducibility through DVC.

> **Prepared for:** Omega Consultancy  
> **Objective:** Analyze insurance portfolio data for risk, profitability, and pricing insights

---

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [Key Insights](#-key-insights)
- [Project Architecture](#-project-architecture)
- [Technical Components](#-technical-components)
- [Methodology](#-methodology)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Business Impact](#-business-impact)
- [Results & Findings](#-results--findings)

---

## 🎯 Executive Summary

This project provides an **end-to-end analytics solution** for insurance risk assessment, covering:

| Phase                    | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| **Data Pipeline**        | Reproducible ETL using DVC for data versioning         |
| **Exploratory Analysis** | Comprehensive EDA of premiums, claims, and loss ratios |
| **Hypothesis Testing**   | Statistical validation using A/B tests and ANOVA       |
| **Predictive Modeling**  | ML models tracked with MLflow, explained with SHAP     |

The analysis examines policy, vehicle, geographic, premium, and claim data to quantify risk via **Loss Ratio** (`TotalClaims / TotalPremium`) and identify high-risk segments.

---

## 🔑 Key Insights

<table>
<tr>
<td width="50%">

**📊 Data Characteristics**

- Monetary variables are **highly skewed** and **zero-inflated**
- Many low/zero values with few extreme outliers
- `CustomValueEstimate` has ~77% missing values

</td>
<td width="50%">

**🎯 High-Risk Segments**

- **Provinces:** Gauteng, Mpumalanga, Limpopo
- **Vehicles:** Heavy commercial vehicles
- **Makes:** Mitsubishi, Suzuki show elevated loss ratios

</td>
</tr>
<tr>
<td>

**📈 Portfolio Trends**

- Loss ratio gradually **improves** as portfolio grows
- Premiums grow faster than claims
- Postal code **2000** is highest volume region

</td>
<td>

**🚙 Vehicle Insights**

- Toyota dominates policy counts
- **Toyota Quantum** leads in total claims
- Passenger vehicles are most common type

</td>
</tr>
</table>

---

## 🏗️ Project Architecture

```
📦 End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
├── 📂 data/
│   ├── raw/                    # Original data files (.txt, .csv)
│   └── processed/              # Cleaned and processed data files
│
├── 📂 notebooks/
│   ├── eda.ipynb               # Comprehensive exploratory data analysis
│   ├── hypothesis_testing.ipynb # A/B tests and ANOVA analysis
│   └── statistical_modeling.ipynb # ML model training and evaluation
│
├── 📂 scripts/
│   ├── initial_preprocess.py   # Raw data preprocessing
│   ├── training.py             # MLflow training and SHAP explainability
│   └── utils.py                # Utility functions
│
├── 📂 src/
│   └── ab_testing.py           # Statistical testing functions
│
├── 📂 tests/                   # Unit tests
├── 📂 .github/workflows/       # CI/CD automation
│
├── dvc.yaml                    # DVC pipeline definition
├── dvc.lock                    # DVC pipeline lock file
├── requirements.txt            # Python dependencies
└── report.md                   # Detailed analysis report
```

---

## 🛠️ Technical Components

### 1. Statistical Testing Module (`src/ab_testing.py`)

Custom functions for hypothesis testing:

| Function            | Purpose                                            |
| ------------------- | -------------------------------------------------- |
| `ab_test()`         | Two-sample t-test for A/B comparisons              |
| `annova_test()`     | One-way ANOVA for multi-group comparisons          |
| `test_hypothesis()` | Automated hypothesis acceptance/rejection (α=0.05) |

### 2. ML Training Pipeline (`scripts/training.py`)

Integrated MLflow experiment tracking with SHAP explainability:

| Function                    | Purpose                                    |
| --------------------------- | ------------------------------------------ |
| `initialize_mlflow()`       | Set up tracking URI and experiments        |
| `train_and_log_model()`     | Train models, log metrics (MSE, R²)        |
| `explain_model_with_shap()` | Generate SHAP explanations for predictions |

**Supported Models:**

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

### 3. DVC Pipeline (`dvc.yaml`)

```yaml
stages:
  initial_process_csv:
    cmd: python scripts/initial_preprocess.py
    deps:
      - data/raw/MachineLearningRating_v3.txt
      - scripts/initial_preprocess.py
    outs:
      - data/processed/MachineLearningRating_v3.csv
```

---

## 📊 Methodology

### EDA Workflow

1. **Data Summary** — Structure inspection, date conversion, descriptive statistics
2. **Data Quality** — Missing value analysis, duplicate detection, outlier visualization
3. **Univariate Analysis** — Distribution profiling for premiums, claims, and categorical features
4. **Bivariate Analysis** — Loss ratio by segment, correlation analysis
5. **Trend Analysis** — Monthly tracking of claims, premiums, and loss ratio
6. **Geographic Insights** — High-risk postal codes and vehicle make/model analysis

### Hypothesis Tests Conducted

| Test                | Null Hypothesis                                 | Result                 |
| ------------------- | ----------------------------------------------- | ---------------------- |
| **Provincial Risk** | No risk differences across provinces            | Analyzed via ANOVA     |
| **Zip Code Risk**   | No risk differences between zip codes           | Accepted (p=0.998)     |
| **Zip Code Profit** | No margin differences between zip codes         | Accepted (p=0.998)     |
| **Gender Risk**     | No significant risk differences between genders | Tested via A/B & ANOVA |

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12+
- Git
- Conda (recommended) or pip

### Step-by-Step Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/End-to-End-Insurance-Risk-Analytics-Predictive-Modeling.git
cd End-to-End-Insurance-Risk-Analytics-Predictive-Modeling

# 2. Create and activate virtual environment
conda create -n insurance-analytics python=3.12
conda activate insurance-analytics

# 3. Install dependencies
pip install -r requirements.txt
pip install dvc scipy scikit-learn mlflow shap jupyter

# 4. Initialize DVC (if cloning fresh)
dvc init

# 5. Configure DVC remote storage
dvc remote add -d localstorage /path/to/your/storage

# 6. Pull data from remote
dvc pull

# 7. Reproduce the pipeline
dvc repro
```

---

## 📖 Usage Guide

### Run the Data Pipeline

```bash
# Reproduce all pipeline stages
dvc repro

# Check pipeline status
dvc status
```

### Execute Notebooks

```bash
# Launch Jupyter
jupyter notebook

# Navigate to:
# - notebooks/eda.ipynb              → Exploratory analysis
# - notebooks/hypothesis_testing.ipynb → Statistical tests
# - notebooks/statistical_modeling.ipynb → ML training
```

### MLflow Experiment Tracking

```bash
# Start MLflow UI
mlflow ui

# View experiments at http://localhost:5000
```

### Run Statistical Tests

```python
from src.ab_testing import ab_test, annova_test, test_hypothesis

# Example: A/B test on gender and risk
t_stat, p_value = ab_test('TotalClaims', 'Gender', data)
test_hypothesis("No risk difference between genders", p_value)

# Example: ANOVA on provinces
f_stat, p_value = annova_test('TotalClaims', 'Province', data)
test_hypothesis("No risk differences across provinces", p_value)
```

---

## 💼 Business Impact

### Risk-Based Pricing

> Elevated loss ratios in specific provinces, vehicle types, and postal codes provide a basis for **refined rating factors** and targeted surcharges/discounts.

### Portfolio Management

> High-loss segments (heavy commercial vehicles, certain makes, specific postal codes) can be targeted with **stricter underwriting rules** and reinsurance strategies.

### Profitable Growth

> Improving loss ratios as the portfolio grows suggest that **expansion within well-understood segments** may be profitable with controlled risk appetite.

### Governance & Compliance

> DVC-backed data lineage improves transparency, enabling regulators and stakeholders to **trace how datasets** used for pricing and capital modeling were produced.

---

## 📈 Results & Findings

### Loss Ratio by Segment

| Category         | High Risk                    | Lower Risk |
| ---------------- | ---------------------------- | ---------- |
| **Province**     | Gauteng, Mpumalanga, Limpopo | Free State |
| **Vehicle Type** | Heavy Commercial             | Passenger  |
| **Makes**        | Mitsubishi, Suzuki           | B.A.W.     |
| **Gender**       | Female (slightly higher)     | Male       |

### Portfolio Trends

- **Claims:** Rise over time, peak mid-2015, then ease
- **Premiums:** Steady, strong growth (portfolio expansion)
- **Loss Ratio:** Volatile early due to low volume, stabilizes and **improves over time**

### Top Risk Drivers

1. **Postal Code 2000** — Highest premium and claim volumes
2. **Toyota Quantum** — Prominent in total claims
3. **Heavy Commercial Vehicles** — Higher loss ratios than passenger vehicles

---

## 🛣️ Next Steps

1. **Formal Hypothesis Testing**
   - Heavy vs. passenger vehicles by loss ratio
   - High-risk vs. low-risk postal codes
   - Vehicle make/model-specific loss experience

2. **Predictive Modeling**
   - Claim frequency (classification/Poisson models)
   - Claim severity among claimants
   - Policy-level loss cost or loss ratio prediction

3. **Productionization**
   - Integrate models into DVC pipeline
   - Define KPIs and monitoring dashboards
   - Track drift, calibration, and portfolio performance

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

<p align="center">
  <b>Built with ❤️ for Insurance Risk Analytics</b>
</p>
