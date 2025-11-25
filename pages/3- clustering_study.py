import streamlit as st
import pandas as pd
import joblib

# heading container
st.markdown(
    "<div style='background-color:#f0f8ff;padding:15px;"
    "border-radius:10px;margin-bottom:15px'>"
    "<h1>Clustering</h1>"
    "<p>This section addresses <strong>Business Requirement 2</strong>: "
    "the client wishes to group elite‑level golfers by skills for insight.</p>"
    "</div>",
    unsafe_allow_html=True
)

# Load data
cluster_summary = pd.read_csv("outputs/cluster/cluster.csv")
cluster_pipeline = joblib.load(
    "outputs/pipelines/clustering_pipeline.pkl"
)

# Toggle summary table
if st.checkbox("Show cluster summary table"):
    st.dataframe(cluster_summary.style.format("{:.3f}"))

# Summaries of each cluster
st.markdown(
    "<div style='background-color:#e8f4f8;padding:15px;"
    "border-radius:10px;margin-top:20px;margin-bottom:10px'>"
    "<h2>Summarising Each Cluster</h2>"
    "<ul>"
    "<li><strong>Cluster 0:</strong> Strong chippers, weak driving; "
    "steady on the green.</li>"
    "<li><strong>Cluster 1:</strong> Weak approach a large issue; "
    "good putters.</li>"
    "<li><strong>Cluster 2:</strong> Consistent drivers, "
    "moderate to poor in other categories.</li>"
    "<li><strong>Cluster 3:</strong> Excelent ball-strikers (tee to green); "
    "good all-round but could work on putting.</li>"
    "<li><strong>Cluster 4:</strong> Approach a strength; "
    "putting an issue.</li>"
    "<li><strong>Cluster 5:</strong> Many areas need work!</li>"
    "<li><strong>Cluster 6:</strong> Approach play should be the "
    "first area to develop.</li>"
    "<li><strong>Cluster 7:</strong> Consistent performer with no major "
    "deficiencies; all metrics roughly equal.</li>"
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)
