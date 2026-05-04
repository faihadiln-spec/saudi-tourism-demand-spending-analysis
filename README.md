# Data-Driven Analysis of Tourism Demand and Spending Patterns in Saudi Arabia

This repository contains the full data science project for analyzing tourism demand and spending patterns in Saudi Arabia using domestic and inbound tourism datasets from 2015 to 2025 H1.

## Project Overview

Tourism is a major part of Saudi Arabia's Vision 2030 economic diversification goals. This project studies how tourism demand and spending differ by visitor type, destination province, and purpose of visit. The main question is whether high visitor numbers always lead to high tourism spending.

The project includes exploratory data analysis, data cleaning, feature engineering, correlation analysis, machine learning model comparison, and an interactive Power BI dashboard.

## Objectives

- Analyze domestic and inbound tourism trends in Saudi Arabia.
- Compare visitor volume and spending by province and visit purpose.
- Calculate spending per tourist to understand economic contribution.
- Identify patterns that explain tourism demand and spending behavior.
- Build and compare machine learning models for tourism spending prediction.
- Present findings through reports, notebooks, and Power BI dashboards.

## Repository Structure

```text
saudi-tourism-demand-spending-analysis/
├── data/
│   └── raw/                         # Original CSV datasets
├── notebooks/                       # Jupyter notebooks for EDA and modeling
│   ├── 01_eda_data_preparation.ipynb
│   └── 02_modeling_evaluation.ipynb
├── dashboard/                       # Power BI dashboard files
├── reports/                         # Project reports and proposal PDFs
├── docs/                            # Submission notes and supporting files
├── src/                             # Reusable helper scripts
├── archive/                         # Original submitted ZIP files
├── requirements.txt
├── .gitignore
└── README.md
```

## Milestones

| Milestone | Description | Main Files |
|---|---|---|
| Stage 1 | Project proposal and initial project definition | `reports/Stage_1_Proposal.pdf` |
| Assignment 1 | Data acquisition, cleaning, feature engineering, EDA, and initial dashboard | `notebooks/01_eda_data_preparation.ipynb`, `reports/Assignment_1_Report.pdf`, `dashboard/assignment1_dashboard.pbix` |
| Assignment 2 | Machine learning modeling, Linear Regression, Random Forest, model evaluation, and discussion | `notebooks/02_modeling_evaluation.ipynb`, `reports/Assignment_2_Report.pdf` |
| Stage 2 | Updated Power BI dashboard and project report | `dashboard/Group4_Saudi_Tourism_Dashboard.pbix`, `reports/Stage_2_Report.pdf` |

## Datasets

The project uses four tourism CSV datasets:

1. Number of domestic tourists and spending by destination province.
2. Number of domestic tourists by main purpose.
3. Number of inbound tourists by main purpose.
4. Number of inbound tourists and spending by destination province.

These datasets include visitor counts, spending values, years, provinces, and visit purposes.

## Methodology

1. **Data Loading**: Load all tourism CSV files using pandas.
2. **Data Cleaning**: Standardize columns, convert numerical values, and convert `2025 H1` into numeric format.
3. **Missing Values Check**: Confirm whether the datasets contain missing values.
4. **Outlier Handling**: Identify high-value tourism regions and cap extreme values where needed.
5. **Feature Engineering**: Create `SPEND_PER_TOURIST` and log-transformed features.
6. **Exploratory Data Analysis**: Study tourism growth, visitor distribution, spending share, and regional/purpose trends.
7. **Correlation Analysis**: Analyze relationships between visitors, spending, year, and spending per tourist.
8. **Modeling**: Train and compare Linear Regression and Random Forest models.
9. **Dashboarding**: Build a Power BI dashboard to communicate insights interactively.

## Machine Learning Models

Two models were used:

- **Linear Regression**: Baseline interpretable model for understanding impact direction.
- **Random Forest**: Non-linear model for capturing complex patterns and feature interactions.

Model performance was evaluated using:

- R² Score
- MAE
- RMSE
- MSE

## Key Findings

- Domestic tourists represent a larger share of total visitors.
- Inbound tourists contribute a higher share of total spending.
- Visit purpose is a stronger predictor of spending than destination in several cases.
- Religious and business travel are important spending drivers for inbound tourism.
- Random Forest performs better when spending patterns are complex, while Linear Regression remains useful for interpretation.

## How to Run the Notebooks

1. Clone the repository:

```bash
git clone https://github.com/your-username/saudi-tourism-demand-spending-analysis.git
cd saudi-tourism-demand-spending-analysis
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open Jupyter Notebook:

```bash
jupyter notebook
```

5. Run the notebooks in this order:

```text
notebooks/01_eda_data_preparation.ipynb
notebooks/02_modeling_evaluation.ipynb
```

## Dashboard

Open the Power BI files in Microsoft Power BI Desktop:

```text
dashboard/assignment1_dashboard.pbix
dashboard/Group4_Saudi_Tourism_Dashboard.pbix
```