import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.plotter import plot_chart

def main():
    st.title("BI Dashboard")

    # Load data
    data = load_data("data/processed/sample_data.csv")

    # Display some data
    st.write("Data Preview:", data.head())

    # Add interactive elements
    st.sidebar.title("Filters")
    category_filter = st.sidebar.selectbox("Select Category", data["Category"].unique())

    # Filter data based on the selection
    filtered_data = data[data["Category"] == category_filter]

    # Display the filtered data
    st.write(f"Filtered Data for {category_filter}:")
    st.write(filtered_data)

    # Plot a chart
    st.write("Sales Trend:")
    plot_chart(filtered_data)

if __name__ == "__main__":
    main()
