import streamlit as st
import joblib
import numpy as np

# Load the saved XGBoost model directly
pipeline = joblib.load("outputs/pipelines/tournament_prediction_pipeline.pkl")
cluster_pipeline = joblib.load("outputs/pipelines/clustering_pipeline.pkl")

st.markdown(
    "<div style='background-color:#f0f8ff;padding:15px;"
    "border-radius:10px;margin-bottom:15px'>"
    "<h1>Predict Tournament Finish</h1>"
    "<p>Input a player’s strokes‑gained stats to estimate their "
    "finish in a 70‑player tournament.</p></div>",
    unsafe_allow_html=True
)

# Input form
with st.form("predict_form"):
    sg_putt = st.number_input("SG Putting", -2.0, 2.0, 0.0, 0.01)
    sg_arg = st.number_input("SG Around Green", -2.0, 2.0, 0.0, 0.01)
    sg_app = st.number_input("SG Approach", -2.0, 2.0, 0.0, 0.01)
    sg_ott = st.number_input("SG Off the Tee", -2.0, 2.0, 0.0, 0.01)
    submit = st.form_submit_button("Run Prediction")

if submit:
    X = np.array([[sg_putt, sg_arg, sg_app, sg_ott]])
    scaled_pred = pipeline.predict(X)[0]
    unscaled = 1 + scaled_pred * (70 - 1)
    predicted_position = int(np.clip(np.round(unscaled), 1, 70))
    st.success(f"Predicted finishing position: **{predicted_position}**")

    cluster_label = cluster_pipeline.predict(X)[0]
    cluster_desc = {
        0: "Strong chippers, weak driving; steady on the green.",
        1: "Weak approach a large issue; good putters.",
        2: "Consistent drivers, moderate to poor elsewhere.",
        3: "Excellent ball-strikers; good all-round, work on putting.",
        4: "Approach a strength; putting an issue.",
        5: "Many areas need work!",
        6: "Approach play should be first focus.",
        7: "Consistent performer; all metrics roughly equal."
    }
    st.write(f"**Cluster:** {cluster_label}")
    st.info(cluster_desc.get(cluster_label, "No description available."))
    st.write("⚠️ *Cluster description is a guide; may not match inputs.*")
