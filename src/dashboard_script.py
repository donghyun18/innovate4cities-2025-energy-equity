import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuration ---
st.set_page_config(layout="wide", page_title="NYC Energy Efficiency Dashboard")

# --- Load Data ---
excel_file = 'energy_efficiency_report_data.xlsx'

try:
    df_all_vulnerable = pd.read_excel(excel_file, sheet_name='All_Vulnerable_Devs')
    df_funded_developments = pd.read_excel(excel_file, sheet_name='Funded_Developments')
    df_roi_analysis = pd.read_excel(excel_file, sheet_name='ROI_Analysis')
except FileNotFoundError:
    st.error(f"Error: {excel_file} not found. Please ensure the Excel file is in the same directory as the script.")
    st.stop()

# --- Data Preprocessing ---

# Clean and convert funded_developments columns
df_funded_developments['KWH_Saved'] = (
    df_funded_developments['KWH_Saved'].astype(str)
    .str.replace(',', '', regex=False)
    .str.replace('$', '', regex=False)
)
df_funded_developments['KWH_Saved'] = pd.to_numeric(df_funded_developments['KWH_Saved'], errors='coerce')

df_funded_developments['Support_Cost_USD'] = (
    df_funded_developments['Support_Cost_USD'].astype(str)
    .str.replace(',', '', regex=False)
    .str.replace('$', '', regex=False)
)
df_funded_developments['Support_Cost_USD'] = pd.to_numeric(df_funded_developments['Support_Cost_USD'], errors='coerce')

# Clean and convert ROI analysis columns
df_roi_analysis['Annual_Savings_USD'] = pd.to_numeric(df_roi_analysis['Annual_Savings_USD'], errors='coerce')
df_roi_analysis['Payback_Period_Years'] = pd.to_numeric(df_roi_analysis['Payback_Period_Years'], errors='coerce')
df_roi_analysis['ROI_Percentage'] = pd.to_numeric(df_roi_analysis['ROI_Percentage'], errors='coerce')

# --- Dashboard Layout ---
st.title("NYC Energy Equity Initiative: Impact Dashboard")
st.markdown("---")

# --- Key Performance Indicators (KPIs) ---
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

total_funded_sites = len(df_funded_developments)
avg_payback_period = df_roi_analysis['Payback_Period_Years'].replace([float('inf'), -float('inf')], pd.NA).dropna().mean()
avg_roi_percentage = df_roi_analysis['ROI_Percentage'].replace([float('inf'), -float('inf')], pd.NA).dropna().mean()

total_fund_generated = 3_154_527_254.49
support_fund_allocated = 1_577_263_627.24

with col1:
    st.metric("Total Fund Generated", f"${total_fund_generated:,.2f}")
with col2:
    st.metric("Fund Allocated for Support", f"${support_fund_allocated:,.2f}")
with col3:
    st.metric("Sites Supported (Solar+Battery)", f"{total_funded_sites} developments")
with col4:
    st.metric("Avg. Project ROI (Annual)", f"{avg_roi_percentage:,.2f}%" if pd.notna(avg_roi_percentage) else "N/A")

st.markdown("---")

# --- Section for Funded Developments List (Table) ---
st.header("Details of Funded Developments")
st.write("Below are the details of the developments selected for solar + battery installations, along with their projected savings and ROI.")

# Copy funded developments and merge only ROI info
df_funded_display = df_funded_developments.copy()
df_funded_display = df_funded_display.merge(
    df_roi_analysis[['Development Name', 'Annual_Savings_USD', 'Payback_Period_Years', 'ROI_Percentage']],
    on='Development Name',
    how='left'
)

st.dataframe(df_funded_display[
    ['Development Name', 'Borough', 'KWH_Saved', 'Support_Cost_USD',
     'Annual_Savings_USD', 'Payback_Period_Years', 'ROI_Percentage']
].round(2))

st.markdown("---")

# --- Top 10 ROI Projects ---
st.header("Top 10 Projects by ROI (Overall)")
df_top_roi = df_roi_analysis.sort_values(by='ROI_Percentage', ascending=False).head(10)
st.dataframe(df_top_roi[
    ['Development Name', 'Borough', 'KWH_Saved', 'Annual_Savings_USD',
     'Payback_Period_Years', 'ROI_Percentage']
].round(2))

st.markdown("---")

# --- Distribution of KWH Saved ---
st.header("Distribution of Potential Annual KWH Savings")
fig_kwh_saved = px.histogram(
    df_all_vulnerable.dropna(subset=['KWH_Saved']),
    x='KWH_Saved',
    nbins=50,
    title='Distribution of Annual KWH Saved Across Vulnerable Developments',
    labels={'KWH_Saved': 'Annual KWH Saved (KWH)'}
)
st.plotly_chart(fig_kwh_saved, use_container_width=True)

st.markdown("---")

# --- Top 10 Overall Savers ---
xls = pd.ExcelFile(excel_file)
if 'Top_10_Overall_Savers' in xls.sheet_names:
    df_top_overall_savers = pd.read_excel(xls, sheet_name='Top_10_Overall_Savers')
    st.header("Top 10 Overall Energy Saving Developments (All Boroughs)")
    st.dataframe(df_top_overall_savers[
        ['Development Name', 'Borough', 'Consumption (KWH)', 'Expected_KWH', 'KWH_Saved']
    ].round(2))
    st.markdown("---")
