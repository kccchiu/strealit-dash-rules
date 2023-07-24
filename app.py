import os
import streamlit as st
import pandas as pd
from components.sidebar import select_category_and_rule
from components.plot import create_roc_plot, create_pr_plot
from components.data_loader import load_data

# Main Streamlit app
def main():
    # Sidebar for category and rule selection
    category, rule = select_category_and_rule()

    # Set the title with the selected category and rule
    st.markdown(f"<h1 style='text-align: center;'>Model Performance Dashboard for <br>{category} {rule}</h1>", unsafe_allow_html=True)
    
    # Load data based on category and rule
    data = load_data(category, rule)

    # Toggle button for showing/hiding the Moving Average line
    show_trace_line = st.checkbox("Show Moving Average Line", value=True)
    # Show data frame checkbox
    show_data_frame = st.checkbox("Show Data Frame")

    # Create and display the ROC AUC plot with the Moving Average line (if enabled)
    st.subheader("ROC AUC Over Time")
    fig_roc = create_roc_plot(data, show_trace_line)
    st.plotly_chart(fig_roc)

    # Create and display the PR AUC plot with the Moving Average line (if enabled)
    st.subheader("PR AUC Over Time")
    fig_pr = create_pr_plot(data, show_trace_line)
    st.plotly_chart(fig_pr)


    # If checkbox is checked, display the data frame
    if show_data_frame:
        st.subheader(f"Data for Category {category}, Rule {rule}")
        st.dataframe(data)


if __name__ == "__main__":
    main()
