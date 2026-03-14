import streamlit as st

st.set_page_config(
    page_title="Blood Donation Management",
    page_icon="🩸",
    layout="wide"
)

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

def main():
    st.sidebar.title("Navigation")
    st.sidebar.info("Select a module from the list above.")
    
    st.title("🩸 Blood Donation Camp Management System")
    st.markdown("""
    Welcome to the centralized donor database. Use this application to:
    - **Analyze** donation trends on the Dashboard.
    - **Explore** and Export donor lists with custom filters.
    - **Manage** donor records (Add/Edit/Delete).
    """)
    
    st.image("https://img.freepik.com/free-vector/blood-donation-abstract-concept-vector-illustration-blood-bank-save-life-hospital-patient-transfusion-volunteer-help-medical-center-donated-plasma-equipment-laboratory-abstract-metaphor_335657-2936.jpg", width=400)

if __name__ == "__main__":
    main()
