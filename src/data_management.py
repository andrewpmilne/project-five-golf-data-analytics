import streamlit as st
import pandas as pd


@st.cache_data
def load_golf_data(path="outputs/data/final/cleaned_golfdata.csv"):
    """Load the cleaned golf dataset."""
    return pd.read_csv(path)


@st.cache_data
def load_player_comparisons(
    top_path="outputs/data/interim/comparison/top_15_players_comparison.csv",
    mid_path="outputs/data/interim/comparison/mid_range_players_comparison.csv"
):
    """Load Top-15 and Mid-range precomputed comparison datasets."""
    top_15 = pd.read_csv(top_path)
    mid_15 = pd.read_csv(mid_path)
    return top_15, mid_15