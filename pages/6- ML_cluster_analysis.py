import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib


def page_cluster_analysis_body():

    # Load clustering pipeline and outputs
    cluster_pipe = joblib.load(
        "outputs/pipelines/clustering_pipeline.pkl"
    )
    cluster_summary = pd.read_csv(
        "outputs/cluster/cluster.csv"
    )
    silhouette_plot = plt.imread(
        "outputs/cluster/silhouette_plot.png"
    )

    # Page header
    st.write("## ML – Cluster Analysis")
    st.info(
        "* This analysis groups players based on similarities in their "
        "strokes-gained skill profiles.\n"
        "* Clustering enables identification of player archetypes for "
        "targeted coaching.\n"
        "* Eight clusters were selected using the elbow and silhouette "
        "evaluation methods."
    )
    st.write("---")

    # Pipeline explanation
    st.write("### Clustering Pipeline")
    st.write(
        "* **Aggregation:** Player means over ≥10 tournaments.\n"
        "* **Scaling:** Not required due to similar feature scales.\n"
        "* **Algorithm:** KMeans (k=8), chosen via silhouette + elbow."
    )

    st.write("#### Pipeline Details")
    st.write(cluster_pipe)
    st.write("---")

    # Silhouette plot
    st.write("### Silhouette Score Plot")
    st.image(silhouette_plot, caption="Silhouette Scores by K")
    st.write("*k = 8 shows the strongest separation between clusters.*")
    st.write("---")

    # Cluster summary table
    st.write("### Cluster Profiles (Mean Strokes Gained)")
    st.dataframe(cluster_summary)
    st.write("---")

    # Coaching summaries block
    html_block = (
        "<div style='background-color:#e8f4f8;padding:15px;"
        "border-radius:10px;margin-top:20px;margin-bottom:10px'>"
        "<h2>Summarising Each Cluster</h2>"
        "<ul>"
        "<li><strong>Cluster 0:</strong> Strong chippers, weak driving; "
        "steady on the green.</li>"
        "<li><strong>Cluster 1:</strong> Weak approach a large issue; "
        "good putters.</li>"
        "<li><strong>Cluster 2:</strong> Consistent drivers; moderate to "
        "poor across other areas.</li>"
        "<li><strong>Cluster 3:</strong> Excellent ball-strikers "
        "(tee-to-green); putting needs work.</li>"
        "<li><strong>Cluster 4:</strong> Strong approach players; "
        "putting is the key weakness.</li>"
        "<li><strong>Cluster 5:</strong> Many areas require improvement.</li>"
        "<li><strong>Cluster 6:</strong> Approach play should be the "
        "primary development focus.</li>"
        "<li><strong>Cluster 7:</strong> Balanced performers with no "
        "clear weaknesses.</li>"
        "</ul>"
        "</div>"
    )

    st.markdown(html_block, unsafe_allow_html=True)


page_cluster_analysis_body()
