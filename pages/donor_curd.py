import streamlit as st
from database import run_query, load_data

st.title("⚙️ Donor Records Management")

tab1, tab2, tab3 = st.tabs(["Add New Donor", "Edit Record", "Delete Record"])

# --- Add New ---
with tab1:
    with st.form("add_form"):
        col1, col2 = st.columns(2)
        fname = col1.text_input("First Name")
        lname = col1.text_input("Last Name")
        mobile = col2.text_input("Mobile No")
        area = col2.text_input("Area")
        source = st.selectbox("Data Source", ["REGISTRATION_2025", "BD_2024", "ANKUR_2023", "Other"])
        date = st.text_input("Camp Date (MM-DD-YY)")
        
        if st.form_submit_button("Add Donor"):
            query = """INSERT INTO donors (first_name, last_name, mobile_no, area, data_source, camp_date) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
            if run_query(query, (fname, lname, mobile, area, source, date)):
                st.success(f"Donor {fname} {lname} added!")

# --- Edit Record ---
with tab2:
    search_name = st.text_input("Search Full Name to Edit").upper()
    if search_name:
        df = load_data()
        # Search match logic
        match = df[(df['first_name'] + " " + df['last_name']).str.contains(search_name, na=False)]
        if not match.empty:
            st.write(f"Found {len(match)} matches:")
            selected_idx = st.selectbox("Select precise record", match.index, format_func=lambda x: f"{match.loc[x, 'first_name']} {match.loc[x, 'last_name']} - {match.loc[x, 'mobile_no']}")
            
            # Edit form
            with st.form("edit_form"):
                new_area = st.text_input("Update Area", value=match.loc[selected_idx, 'area'])
                new_mobile = st.text_input("Update Mobile", value=str(match.loc[selected_idx, 'mobile_no']))
                if st.form_submit_button("Update"):
                    q = "UPDATE donors SET area=%s, mobile_no=%s WHERE first_name=%s AND last_name=%s"
                    run_query(q, (new_area, new_mobile, match.loc[selected_idx, 'first_name'], match.loc[selected_idx, 'last_name']))
                    st.success("Record updated!")
        else:
            st.warning("No donor found with that name.")

# --- Delete Record ---
with tab3:
    st.error("Warning: Deletion is permanent.")
    search_del = st.text_input("Search Name for Deletion").upper()
    if search_del:
        df = load_data()
        match_del = df[(df['first_name'] + " " + df['last_name']).str.contains(search_del, na=False)]
        if not match_del.empty:
            st.table(match_del[['first_name', 'last_name', 'area', 'camp_date', 'data_source']])
            target_idx = st.selectbox("Select exact row to delete", match_del.index)
            
            if st.button("Confirm Delete"):
                q = "DELETE FROM donors WHERE first_name=%s AND last_name=%s AND camp_date=%s"
                params = (match_del.loc[target_idx, 'first_name'], match_del.loc[target_idx, 'last_name'], match_del.loc[target_idx, 'camp_date'])
                if run_query(q, params):
                    st.success("Donor deleted successfully.")