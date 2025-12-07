# End-to-End Insurance Risk Analytics & Predictive Modeling

## Project Overview
This repository provides a complete workflow for insurance risk analytics, including exploratory data analysis (EDA), data processing, and reproducible data versioning using DVC. The project demonstrates best practices for data science, from raw data ingestion to advanced insights and pipeline automation.

---

## Directory Structure
```
├── data/
│   ├── raw/         # Original data files (.txt, .csv)
│   └── processed/   # Cleaned and processed data files
├── notebooks/
│   └── eda.ipynb    # Main EDA notebook
├── scripts/
│   └── initial_preprocess.py  # Script for initial data processing
├── dvc.yaml         # DVC pipeline definition
├── dvc.lock         # DVC pipeline lock file
├── .dvc/            # DVC configuration and cache
├── .dvcignore       # DVC ignore file
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## Data Versioning & Pipeline (DVC)

This project uses [DVC](https://dvc.org/) for data versioning and pipeline management:
- **Raw data** is tracked with DVC (`dvc add data/raw/MachineLearningRating_v3.csv`).
- **Local remote storage** is configured for data sharing and backup.
- **Pipeline stage** defined in `dvc.yaml` automates data processing:
  - Converts raw `.txt` data to processed `.csv` using `scripts/initial_preprocess.py`.
  - Output is stored in `data/processed/MachineLearningRating_v3.csv`.
- **Reproducibility:**
  - Run `dvc repro` to reproduce the pipeline.
  - Run `dvc push`/`dvc pull` to sync data with remote storage.
- **Version control:**
  - All `.dvc` files, `dvc.yaml`, and `dvc.lock` are tracked in Git.

---

## Exploratory Data Analysis (EDA)

The EDA notebook (`notebooks/eda.ipynb`) covers:

### 1. Data Summary
- Data loading and type inspection
- Conversion of date columns
- Descriptive statistics for key columns

### 2. Data Quality
- Missing value analysis
- Duplicate detection
- Outlier visualization (boxplots, log scale)

### 3. Univariate Analysis
- Histograms for `TotalPremium` and `TotalClaims`
- Bar charts for `Province`, `Make`, `Gender`, `VehicleType`

### 4. Bivariate & Multivariate Analysis
- Loss ratio calculation and visualization by category
- Correlation matrix for numeric columns
- Monthly trends by postal code and by total premiums and claims

### 5. Trend Analysis
- Monthly total claims, premiums, and loss ratio (line plots)
- Interpretation of trends

### 6. Geography & Car Insights
- Top 10 vehicle makes and models by claims
- Top 10 postal codes by premiums and claims
- Interpretation of risk drivers

### 7. Predictive Modeling (Template)
- Steps for feature engineering, model training, and evaluation
- Example targets: `TotalClaims`, `LossRatio`, claim occurrence

---

## How to Reproduce the Workflow

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    pip install dvc
    ```
2. **Initialize DVC (if not done)**
    ```bash
    dvc init
    ```
3. **Add raw data to DVC**
    ```bash
    dvc add data/raw/MachineLearningRating_v3.csv
    ```
4. **Configure local remote storage**
    ```bash
    dvc remote add -d localstorgae C:/Users/yeget/LocalStorage -- adjust-path to your desired location
    ```
5. **Run the pipeline**
    ```bash
    dvc repro
    ```
6. **Push/pull data to/from remote**
    ```bash
    dvc push
    dvc pull
    ```
7. **Run EDA notebook**
    - Open `notebooks/eda.ipynb` in Jupyter or VS Code
    - Execute cells to explore and visualize the data

---

## Notes & Best Practices
- Data files are tracked by DVC, not Git. Only `.dvc` files and pipeline definitions are committed.
- Use DVC for reproducible pipelines and data sharing.
- Activate your Conda environment before running DVC commands if using one.
- All code and analysis are modular and extensible for further modeling.

---

## Contact & Contributions
Feel free to open issues or pull requests for improvements, bug fixes, or new features.

---

**This project demonstrates a robust, reproducible workflow for insurance risk analytics and predictive modeling.**
