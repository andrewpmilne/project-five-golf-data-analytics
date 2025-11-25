import streamlit as st  
import pandas as pd  
import joblib  
import numpy as np  

# Load pipelines  
pipeline = joblib.load("outputs/pipelines/tournament_prediction_pipeline.pkl")  
cluster_pipeline = joblib.load("outputs/pipelines/clustering_pipeline.pkl")  

# Header  
st.markdown(  
    "<div style='background-color:#f0f8ff;padding:15px;"  
    "border-radius:10px;margin-bottom:15px'>"  
    "<h1>Predict Tournament Finish</h1>"  
    "<p>Input a player’s strokes‑gained stats to estimate their finish "  
    "in a 70‑player tournament.</p>"  
    "</div>",  
    unsafe_allow_html=True  
)  

# Input form  
with st.form("predict_form"):  
    sg_putt = st.number_input(  
        "SG Putting", min_value=-2.0, max_value=2.0, value=0.0,  
        step=0.01, format="%0.2f"  
    )  
    sg_arg = st.number_input(  
        "SG Around Green", min_value=-2.0, max_value=2.0, value=0.0,  
        step=0.01, format="%0.2f"  
    )  
    sg_app = st.number_input(  
        "SG Approach", min_value=-2.0, max_value=2.0, value=0.0,  
        step=0.01, format="%0.2f"  
    )  
    sg_ott = st.number_input(  
        "SG Off the Tee", min_value=-2.0, max_value=2.0, value=0.0,  
        step=0.01, format="%0.2f"  
    )  
    submit = st.form_submit_button("Run Prediction")  

if submit:  
    X = np.array([[sg_putt, sg_arg, sg_app, sg_ott]])  
    scaled_pred = pipeline.predict(X)[0]  
    unscaled = 1 + scaled_pred * (70 - 1)  
    predicted_position = int(np.round(unscaled))  
    predicted_position = max(1, min(predicted_position, 70))  
    st.success(f"Predicted finishing position: **{predicted_position}**")  

    # Predict cluster  
    cluster_label = cluster_pipeline.predict(X)[0]  

    # Descriptions
    cluster_descriptions = {
        0: "Strong chippers, weak driving; steady on the green.",
        1: "Weak approach a large issue; good putters.",
        2: "Consistent drivers, moderate to poor in other categories.",
        3: "Excellent ball‑strikers (tee to green); good all‑round but could work on putting.",
        4: "Approach a strength; putting an issue.",
        5: "Many areas need work!",
        6: "Approach play should be the first area to develop.",
        7: "Consistent performer with no major deficiencies; all metrics roughly equal."
    }
 

    description = cluster_descriptions.get(
        cluster_label, "No description available for this cluster."
    )

    st.write(f"**Cluster:** {cluster_label}")
    st.info(description)

    # Note about interpretation
    st.write(
        "⚠️ *Please be aware that the cluster description "
        " is a guide to the player, "
        "and may not exactly correspond with the current inputted statistics.*"
    )