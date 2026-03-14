import streamlit as st
import plotly.express as px
from database import load_data
from utils import process_data

st.set_page_config(layout="wide")
st.title("📊 Donation Analytics Dashboard")

hide_all_viewer_elements = """
    <style>
    /* 1. Hides the Fork icon and the "Fork this app" text */
    button[data-testid="stBaseButton-header"] {
        display: none !important;
    }

    /* 2. Hides the GitHub icon and the status widget */
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }

    /* 3. Hides the Edit/Pencil button (Deploy button) */
    .stAppDeployButton {
        display: none !important;
    }

    /* 4. Hides the 'Made with Streamlit' footer at the bottom */
    footer {
        visibility: hidden !important;
    }
    
    /* 5. Extra safety: Hide any tooltips that might show "Fork" on hover */
    div[data-testid="stTooltipHoverTarget"] {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_all_viewer_elements, unsafe_allow_html=True)

df = load_data()
df = process_data(df)

if not df.empty:
    # --- Sidebar Filters ---
    st.sidebar.header("Global Filters")
    years = sorted(df['year'].unique().tolist())
    selected_year = st.sidebar.multiselect("Select Years", years, default=years)
    
    # Filter data
    filtered_df = df[df['year'].isin(selected_year)]

    # --- KPI Cards ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Donors", len(filtered_df))
    col2.metric("Total Units", filtered_df['unit_no'].nunique())
    col3.metric("Total Areas", filtered_df['area'].nunique())
    col4.metric("Data Sources", filtered_df['data_source'].nunique())

    # --- Charts ---
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Donations per Year")
        year_counts = filtered_df.groupby('year').size().reset_index(name='counts')
        fig_year = px.bar(year_counts, x='year', y='counts', color='year', text_auto=True)
        st.plotly_chart(fig_year, use_container_width=True)

    with c2:
        st.subheader("Top 10 Areas")
        area_counts = filtered_df['area'].value_counts().nlargest(10).reset_index()
        fig_area = px.pie(area_counts, values='count', names='area', hole=0.3)
        st.plotly_chart(fig_area, use_container_width=True)

    st.subheader("Data Source Distribution")
    source_counts = filtered_df['data_source'].value_counts().reset_index()
    fig_source = px.bar(source_counts, x='data_source', y='count', color='data_source', orientation='v')
    st.plotly_chart(fig_source, use_container_width=True)
else:
    st.warning("No data found in the database. Please initialize the database.")
