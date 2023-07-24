import os
import streamlit as st
import pandas as pd
from components.sidebar import select_category_and_rule
from components.plot import create_roc_plot, create_pr_plot

# Function to load data from CSV files
def load_data(category, rule):
    file_path = f"data/{category}/cat{category}_rule{rule}.csv"
    data = pd.read_csv(file_path)
    return data

# Main Streamlit app
def main():
    # Sidebar for category and rule selection
    category, rule = select_category_and_rule()

    # Set the title with the selected category and rule
    st.markdown(f"<h1 style='text-align: center;'>Model Performance Dashboard for {category} {rule}</h1>", unsafe_allow_html=True)
    
    # Load data based on category and rule
    data = load_data(category, rule)

    # Toggle button for showing/hiding the smooth metric line
    show_smooth_metric_line = st.checkbox("Show Smooth Metric Line", value=True)
    # Show data frame checkbox
    show_data_frame = st.checkbox("Show Data Frame")

    # Create and display the ROC AUC plot with the smooth metric line (if enabled)
    st.subheader("ROC AUC Over Time")
    fig_roc = create_roc_plot(data, show_smooth_metric_line)
    st.plotly_chart(fig_roc)

    # Create and display the PR AUC plot with the smooth metric line (if enabled)
    st.subheader("PR AUC Over Time")
    fig_pr = create_pr_plot(data, show_smooth_metric_line)
    st.plotly_chart(fig_pr)


    # If checkbox is checked, display the data frame
    if show_data_frame:
        st.subheader(f"Data for Category {category}, Rule {rule}")
        st.dataframe(data)


if __name__ == "__main__":
    main()
