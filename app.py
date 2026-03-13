import streamlit as st

st.set_page_config(
    page_title="Blood Donation Management",
    page_icon="🩸",
    layout="wide"
)

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