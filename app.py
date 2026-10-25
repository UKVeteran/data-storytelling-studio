import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_and_clean_data

st.set_page_config(
    page_title="Dataset Storytelling Studio",
    page_icon="📊",
    layout="wide"
)

# Load data
df = load_and_clean_data()

# Sidebar Controls
st.sidebar.title("🔍 Investigation Controls")
regions = ["All"] + list(df['Region'].unique())
selected_region = st.sidebar.selectbox("Filter by Geographic Region", regions)

min_gdp, max_gdp = int(df['GDP_per_Capita'].min()), int(df['GDP_per_Capita'].max())
gdp_range = st.sidebar.slider("GDP per Capita Range ($)", min_gdp, max_gdp, (min_gdp, max_gdp))

# Filter dataframe
filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]

filtered_df = filtered_df[
    (filtered_df['GDP_per_Capita'] >= gdp_range[0]) & 
    (filtered_df['GDP_per_Capita'] <= gdp_range[1])
]

# Header & Introduction
st.title("📊 Dataset Storytelling Studio")
st.markdown("""
### Investigation: Global Public Health & Economic Prosperity
*How strongly does healthcare expenditure and overall economic output predict life expectancy across global regions?*
""")

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Countries Analyzed", len(filtered_df))
col2.metric("Avg Life Expectancy", f"{filtered_df['LifeExpectancy'].mean():.1f} yrs")
col3.metric("Avg GDP per Capita", f"${filtered_df['GDP_per_Capita'].mean():,.0f}")
col4.metric("Avg Healthcare Spend", f"{filtered_df['Healthcare_Spend_Pct'].mean():.1f}%")

st.divider()

# Visualization Section
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("1. Wealth vs. Longevity Correlation")
    fig_scatter = px.scatter(
        filtered_df,
        x="GDP_per_Capita",
        y="LifeExpectancy",
        size="Population",
        color="Region",
        hover_name="Country",
        log_x=True,
        title="Life Expectancy vs. Log GDP per Capita",
        labels={"GDP_per_Capita": "GDP per Capita (USD, Log Scale)", "LifeExpectancy": "Life Expectancy (Years)"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_right:
    st.subheader("2. Regional Healthcare Investment")
    fig_bar = px.bar(
        filtered_df.groupby("Region")["Healthcare_Spend_Pct"].mean().reset_index(),
        x="Region",
        y="Healthcare_Spend_Pct",
        color="Region",
        title="Average Healthcare Spend (% of GDP)",
        labels={"Healthcare_Spend_Pct": "% of GDP"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# Synthesis & Conclusion
st.subheader("📌 Investigative Synthesis & Findings")
st.markdown("""
> **Key Insight:** There exists a non-linear log relationship between GDP per Capita and Life Expectancy. 
> Initial investments in healthcare and economic growth yield sharp returns in overall lifespan, 
> tapering off into a plateau past $40,000 GDP per capita.
""")

with st.expander("📄 View Data Table"):
    st.dataframe(filtered_df, use_container_width=True)
