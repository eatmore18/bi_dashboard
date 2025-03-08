import plotly.express as px
import pandas as pd
import streamlit as st

def plot_chart(data: pd.DataFrame):
    """
    Function to plot a sales trend chart.
    """
    fig = px.line(data, x="Date", y="Sales", title="Sales Trend Over Time")
    st.plotly_chart(fig)
