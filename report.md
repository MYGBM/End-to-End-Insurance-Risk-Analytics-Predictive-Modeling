# Insurance Portfolio Analysis Report

**Prepared for:** Omega Consultancy  
**Date:** November 30, 2025  
**Subject:** Analysis of Insurance Portfolio Data for Risk, Profitability & Pricing Insights  

---

## 1. Executive Summary

This report summarizes an exploratory data analysis (EDA) of an insurance portfolio containing policy, vehicle, geographic, premium, and claim information. The goals were to:

- Understand the distribution and quality of key variables (`TotalPremium`, `TotalClaims`, `CustomValueEstimate`, `SumInsured`).
- Quantify risk and profitability via **Loss Ratio** (`TotalClaims / TotalPremium`).
- Identify high‑risk segments by province, vehicle type, make, gender, and postal code.
- Establish a reproducible data pipeline using **DVC (Data Version Control)**.

Key insights:

- Monetary variables are **highly skewed and zero‑inflated**, with many low/zero values and a few very large ones.
- **Gauteng**, heavy commercial vehicles, and certain makes (e.g., Mitsubishi, Suzuki) show **elevated loss ratios** compared with other segments.
- Postal code **2000** exhibits especially high premium and claim volumes, with several other postal codes (e.g., 122, 8000) also material.
- Over time, **premiums grow faster than claims**, leading to a gradually improving and more stable loss ratio.

A DVC‑based pipeline ensures the raw text data is consistently processed into a clean CSV, supporting reproducible EDA and future predictive modeling.

---

## 2. EDA Methodology (Condensed)

The EDA was structured into clear steps, aligned with your notebook markdowns.

### 2.1 Step 1 — Data Summary

**Objectives**
- Inspect structure (`head`, `info`, `dtypes`) and convert object date fields (e.g., `TransactionMonth`) to `datetime`.
- Compute descriptive statistics for `TotalPremium`, `TotalClaims`, `CustomValueEstimate`, `SumInsured`.

**Findings**
- Numeric columns are generally typed correctly; dates required conversion.
- All four key monetary variables show **high variance, strong right skew, and extreme outliers**.

**[Plot Placeholder 1] Descriptive Statistics Table**  
*Title:* Descriptive Statistics for Key Numeric Columns  
*X‑axis:* Key variables  
*Y‑axis:* Statistical values (table: mean, std, quartiles, max)  
*Below‑plot text:* Emphasize skew, long right tails, and concentration of volume in a small subset of policies.

---

### 2.2 Step 2 — Data Quality

**Objectives**
- Measure missingness and duplicates.
- Visualize outliers for `TotalPremium`, `TotalClaims`, `CustomValueEstimate`.

**Findings**
- `CustomValueEstimate` has ~77% missing values; several other features (e.g., `WrittenOff`, `Rebuilt`, `Converted`, `CrossBorder`, `NumberOfSupplements`) are also sparse.
- `NumberOfVehiclesInFleet` is effectively unusable (near 100% missing) and can be dropped.
- Raw boxplots are dominated by zeros; a **log scale** helps reveal distribution and outliers.

**[Plot Placeholder 2] Missing Values**  
*Title:* Percentage of Missing Values per Column  
*X‑axis:* Columns with missing data  
*Y‑axis:* % Missing  
*Below‑plot text:* Highlight which columns may be dropped, imputed, or engineered.

**[Plot Placeholder 3] Boxplots (Log Scale)**  
*Title:* Boxplots of `TotalPremium`, `TotalClaims`, `CustomValueEstimate` (Log Scale)  
*X‑axis:* Variable  
*Y‑axis:* Log(Value)  
*Below‑plot text:* Show that most observations are low‑value, with clear high‑value outliers.

---

### 2.3 Step 3 — Univariate Analysis

**Objectives**
- Profile distributions of `TotalPremium` and `TotalClaims`.
- Understand portfolio composition by `Province`, `make`, `Gender`, `VehicleType`.

**Findings**
- Premiums and claims are **heavily right‑skewed** with many zeros.
- Gauteng dominates policy counts, followed by KwaZulu‑Natal and Western Cape.
- Toyota is the most common make; passenger vehicles are the dominant vehicle type.
- Gender is often unspecified; among specified records, male policies are more common.

**[Plot Placeholder 4] Histograms**  
*Title:* Distribution of `TotalPremium` and `TotalClaims`  
*X‑axis:* Amount  
*Y‑axis:* Policy count  
*Below‑plot text:* Note zero‑inflation and implications for modeling (e.g., two‑part or zero‑inflated models).

**[Plot Placeholder 5] Categorical Bar Charts**  
*Title:* Policy Counts by Province, Make, Gender, Vehicle Type  
*X‑axis:* Category  
*Y‑axis:* Count  
*Below‑plot text:* Comment on concentration of business in certain regions and brands.

---

### 2.4 Step 4 — Bivariate & Multivariate Analysis

**Loss Ratio by Segment**
- Defined `LossRatio = TotalClaims / TotalPremium` (with zero‑premium cases handled as missing).
- Computed mean loss ratio by **Province**, **VehicleType**, **make**, and **Gender**.

**Key Patterns**
- Provinces: Gauteng, Mpumalanga, and Limpopo have **higher average loss ratios**; Free State shows lower ratios.
- Vehicle types: **Heavy commercial** and **light commercial** vehicles have higher loss ratios than passenger vehicles.
- Makes: Mitsubishi, Suzuki, and similar brands stand out with higher loss ratios; some makes like B.A.W are lower.
- Gender: Among specified records, females show a slightly higher mean loss ratio than males.

**[Plot Placeholder 6] Loss Ratio by Segment**  
*Title:* Mean Loss Ratio by Province, Vehicle Type, Make, Gender  
*X‑axis:* Segment  
*Y‑axis:* Mean Loss Ratio  
*Below‑plot text:* Highlight high‑risk segments and potential pricing opportunities.

**Correlation Analysis**
- Examined correlations among `TotalPremium`, `TotalClaims`, `CustomValueEstimate`, `SumInsured`, and `LossRatio`.
- Premiums and claims are positively correlated, with expected links between loss ratio and both components.

**[Plot Placeholder 7] Correlation Heatmap**  
*Title:* Correlation Matrix of Key Numeric Variables  
*X-/Y‑axis:* Variables  
*Below‑plot text:* Note modest linear correlations, suggesting complex, non‑linear risk structure.

**Multivariate: Monthly × Postal Code**
- Aggregated monthly `TotalPremium` and `TotalClaims` by `PostalCode`.
- Focused on top 10 postal codes by premiums and claims (e.g., 2000, 122, 8000).

**[Plot Placeholder 8] Monthly Premiums & Claims by Postal Code**  
*Title:* Monthly `TotalPremium` and `TotalClaims` by Top Postal Codes  
*X‑axis:* Month  
*Y‑axis:* Monthly total (premium or claims)  
*Color:* Postal code  
*Below‑plot text:* Emphasize postal code 2000 as a high‑volume, high‑exposure region.

---

### 2.5 Step 5 — Trend Analysis

**Objectives**
- Track monthly `TotalPremium`, `TotalClaims`, and `LossRatio`.

**Findings**
- Claims rise over time, peaking around mid‑2015 before easing.
- Premiums grow steadily and strongly, indicating portfolio expansion.
- Loss ratio is volatile early (low volume + large claims) but stabilizes and **gradually improves** as the book grows.

**[Plot Placeholder 9] Monthly Trends**  
*Title:* Monthly `TotalClaims`, `TotalPremium`, and `LossRatio`  
*X‑axis:* Month  
*Y‑axis:* Aggregate value  
*Below‑plot text:* Link improving loss ratio to potential gains in profitability and scale.

---

### 2.6 Step 6 — Geography & Car Insights

**Objectives**
- Identify high‑claim makes/models and high‑premium/high‑claim postal codes.

**Findings**
- Toyota and particularly **Toyota Quantum** models feature prominently in total claims.
- Postal codes 2000, 122, 8000 and others are major contributors to premiums and claims.

**[Plot Placeholder 10] Vehicle & Postal Code Insights**  
*Title:* Top 10 Vehicle Makes/Models and Postal Codes by Claims/Premiums  
*X‑axis:* Category (make, model, postal code)  
*Y‑axis:* TotalClaims or TotalPremium  
*Below‑plot text:* Note how specific combinations of geography and vehicle characteristics drive loss experience.

---

## 3. DVC Setup Methodology (High Level)

To keep analysis reproducible:

- A DVC stage `initial_process_csv` is defined in `dvc.yaml`:
  - **cmd:** `python scripts/initial_preprocess.py`
  - **deps:** `data/raw/MachineLearningRating_v3.txt`, `scripts/initial_preprocess.py`
  - **outs:** `data/processed/MachineLearningRating_v3.csv`
- Raw and processed data are tracked with DVC; only small `.dvc` files and pipeline metadata live in Git.
- A local DVC remote (e.g., `C:/Users/yeget/LocalStorage`) is configured for storing versioned data.
- Any collaborator can:
  1. Clone the repo and run `dvc pull` to fetch data.
  2. Run `dvc repro` to regenerate the processed CSV from raw inputs.

This ensures that all EDA and modeling work can be rerun consistently, with clear auditability of data and code versions.

---

## 4. Business Impact

The analysis supports several business decisions:

- **Risk‑Based Pricing:**  
  Elevated loss ratios in specific provinces, vehicle types, makes, and postal codes provide a basis for refined rating factors and surcharges/discounts.

- **Portfolio Management:**  
  High‑loss segments (e.g., heavy commercial vehicles, certain makes or postal codes) can be targeted with stricter underwriting rules, reinsurance strategies, or risk‑management programs.

- **Profitable Growth:**  
  Improving loss ratios as the portfolio grows suggest that expansion within well‑understood segments may be profitable, provided risk appetite is controlled.

- **Governance & Compliance:**  
  DVC‑backed data lineage improves transparency, enabling regulators and stakeholders to trace how datasets used for pricing and capital modeling were produced.

---

## 5. Challenges & Next Steps

### 5.1 Key Challenges

- **Understanding a Large, Complex Dataset:**  
  Many columns and records required a disciplined focus on the most business‑relevant variables.

- **Identifying Key EDA Columns:**  
  Prioritizing `TotalPremium`, `TotalClaims`, `CustomValueEstimate`, `SumInsured`, geography, and core categorical fields was essential to keep EDA focused and meaningful.

- **Missingness & Sparse Features:**  
  High missingness in `CustomValueEstimate` and some status flags complicates their use in models.

- **Skewness, Zeros, and Outliers:**  
  Zero‑inflated, heavy‑tailed distributions demand appropriate transformations, robust methods, or two‑stage modeling approaches.

### 5.2 Next Steps

1. **Hypothesis Testing**  
   - Formally test segment differences, e.g.:  
     - Heavy vs. passenger vehicles by loss ratio.  
     - High‑risk vs. low‑risk postal codes.  
     - Vehicle make/model–specific loss experience.

2. **Predictive Modeling**  
   - Build models for:  
     - Claim frequency (classification/Poisson‑like models).  
     - Claim severity among claimants.  
     - Policy‑level loss cost or loss ratio.
   - Incorporate time, geography, and vehicle features, and experiment with tree‑based and GLM‑type models.

3. **Productionization & Monitoring**  
   - Integrate models into the DVC pipeline.  
   - Define KPIs and monitoring dashboards to track drift, calibration, and portfolio performance.

This shorter report consolidates the core EDA, DVC methodology, business implications, challenges, and immediate next steps into a format suitable for a ~5‑page client‑facing deliverable.