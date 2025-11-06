🏙️ NYC Energy Equity Initiative
Data-Driven Strategy for Sustainable Investment in Vulnerable NYC Communities

This project analyzes municipal electricity consumption, demographic vulnerability, and future forecasting to build a data-driven investment framework for energy equity in New York City.
Using a structured methodology, the analysis identifies overconsuming developments, simulates potential savings, forecasts long-term trends, and evaluates cost-effectiveness through ROI analysis.

The final output includes:
✅ An interactive Streamlit dashboard
✅ A master Excel report
✅ Forecasting results
✅ ROI evaluation
✅ Processed datasets used in investment planning

🚀 Live Dashboard Demo (Optional)

👉 Live App:
https://your-streamlit-app-url.streamlit.app
(Replace with your deployed Streamlit Cloud URL)

## 📊 Data Sources
The `data.zip` file contains the original datasets used in this project:

- **Electric_Consumption_data.csv** — NYC electricity usage dataset
- **New_York_City_Population.csv** — Population & demographic dataset

These datasets were used for:
- Energy burden analysis
- Demographic correlation studies
- Prophet-based future electricity consumption forecasting
- Streamlit dashboard visualizations

🔧 Technology Stack
Category	Tools	Purpose
Language	Python	Core data processing and analysis
Libraries	Pandas, NumPy	Data manipulation and numerical operations
Modeling	Prophet	Time-series forecasting for future consumption scenarios
Visualization	Streamlit, Plotly	Building the interactive project dashboard
📌 Project Overview

NYC experiences significant disparities in electricity consumption across boroughs—especially within low-income, vulnerable communities.
This project builds a transparent and data-driven methodology to:

✅ Identify developments that exceed borough consumption norms
✅ Simulate expected usage and calculate potential savings
✅ Forecast long-term usage under multiple scenarios
✅ Prioritize funding for high-impact interventions
✅ Evaluate ROI for solar + battery installations

The final goal is to support sustainable, equitable energy solutions through measurable insights.

🔬 Methodology

A clearly structured, multi-step methodology was used:

1️⃣ Flagging Developments Exceeding Borough Norms
✅ Vulnerability Assessment

Boroughs with Median Household Income < $55,000 (e.g., BRONX) were classified as economically vulnerable.

✅ Overconsumption Detection

Within each borough, developments were flagged as overconsuming if total KWH usage exceeded the borough’s average per-capita electricity consumption.

2️⃣ Simulating Expected Consumption & Potential Savings
✅ Expected Consumption (Expected_KWH)
Expected_KWH = Estimated Population × Borough Per Capita KWH

✅ KWH Savings Calculation
KWH_Saved = Actual Consumption – Expected_KWH


This represents the annual savings potential if usage aligns with borough norms.

3️⃣ Forecasting with Prophet (36-Month Projection)

The Prophet model forecasts electricity demand under two scenarios:

Business-as-Usual (current trend continues)

Reduced Usage (after interventions & savings)

These projections illustrate the long-term economic and environmental impact of targeted investment.

💰 Key Results & Systemwide Impact
✅ A. Potential Fund Generation

Total savings opportunity based on excess KWH and rate assumption ($0.25 / KWH):

💰 $3,154,527,254.49

Support Fund Allocation

50% allocated to vulnerable communities:

➡️ $1,577,263,627.24 for renewable energy installations.

✅ B. Prioritized Renewable Energy Projects

A total of 34 developments were selected based on:

Vulnerability level

Overconsumption severity

KWH savings potential

Each development receives:
✅ Solar panels
✅ Battery backup system
(Estimated cost per site: $30,000)

✅ C. ROI Analysis
⚡ Ultra-Fast Payback

Average payback period:
➡️ 0.2 years (~2.4 months)

📈 Outstanding Annual ROI

Average annual ROI:
➡️ 2,374%+

This demonstrates exceptionally strong financial and social returns from targeted investment.

✅ 📦 Output Files (Analysis Results)

This project generates several key output files used for forecasting, ROI modeling, dashboard visualization, and final reporting.

### 1. energy_efficiency_report_data.xlsx — Master Consolidated Report

The primary data source for the dashboard and final report.
It integrates vulnerability scoring, overconsumption tagging, savings simulation, and ROI metrics.

Contains sheets:

All_Vulnerable_Devs
Developments in economically vulnerable boroughs with potential savings.

Funded_Developments
Final prioritized list for solar + battery installations.

ROI_Analysis
Estimated KWH Saved, Support Cost (USD), Payback Period (Years), ROI (%).

### 2. overconsuming_developments.csv — Flagged High-Consumption Sites

Generated after Methodology 1.

Key Columns:

Development Name

Borough

Consumption (KWH)

Exceeds_Avg (True)

This forms the baseline dataset for calculating potential savings.

### 3. simulated_savings_per_development.csv — Estimated KWH Savings

Generated after Methodology 2.

Key Columns:

Development Name

Expected_KWH

KWH_Saved

Population

This dataset feeds directly into fund allocation and ROI modeling.

📓 Notebooks
✅ notebooks/Electric_Consumption_Analysis.ipynb

Contains the complete workflow:

Data loading & preprocessing

Vulnerability analysis

Overconsumption tagging

Savings simulation

Prophet forecasting

Visualizations & summary exports

🗂 Repository Structure
project/
├─ data/
│  ├─ raw/
│  └─ processed/
├─ output/
├─ notebooks/
│  └─ Electric_Consumption_Analysis.ipynb
├─ src/
│  └─ dashboard_script.py
├─ assets/
├─ README.md
├─ LICENSE
└─ .gitignore

🪪 License

MIT License


