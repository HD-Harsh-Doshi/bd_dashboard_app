import streamlit as st

st.set_page_config(
    page_title="Blood Donation Management",
    page_icon="🩸",
    layout="wide"
)

# --- CSS TO HIDE GITHUB, FORK, AND PENCIL BUTTONS ---
hide_toolbar_css = """
    <style>
    /* Hides the GitHub, Fork, and Edit buttons */
    div[data-testid="stStatusWidget"] {
        visibility: hidden;
    }
    /* Hides the 'Edit' pencil button specifically */
    .stAppDeployButton {
        display: none;
    }
    /* Hides the 'Made with Streamlit' footer */
    footer {
        visibility: hidden;
    }
    /* Optional: Hides the main menu (three dots) */
    #MainMenu {
        visibility: hidden;
    }
    </style>
"""
st.markdown(hide_toolbar_css, unsafe_allow_html=True)

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
