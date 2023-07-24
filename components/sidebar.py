import streamlit as st
import os

def select_category_and_rule():
    st.sidebar.title("Model and Rule Selection")

    # Scan the 'data' directory to get available categories and rules
    data_dir = "data"
    categories = sorted(os.listdir(data_dir))
    category = st.sidebar.selectbox("Select Category", categories)

    category_dir = os.path.join(data_dir, category)
    rules = sorted([file_name.split("_")[1][4:-4] for file_name in os.listdir(category_dir) if file_name.endswith(".csv")])
    rule = st.sidebar.selectbox("Select Rule", rules)

    st.sidebar.markdown("### Selected Category and Rule:")
    st.sidebar.write(f"**Category:** {category}")
    st.sidebar.write(f"**Rule:** {rule}")

    return category, rule