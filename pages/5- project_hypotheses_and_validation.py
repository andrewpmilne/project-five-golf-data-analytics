import streamlit as st

st.title("Project Hypotheses and Validations")

# Hypothesis One
st.subheader("Hypothesis One")
st.markdown(
    "<div style='background-color:#FFF3E0; padding:15px; border-radius:5px;'>"
    "<strong>Hypothesis 1:</strong> Strokes gained in driving will show the "
    "strongest correlation with finishing in the top "
    "ten or not.<br><br>"
    "- <strong>This was proved false.</strong> The average strokes gained "
    "comparison and the Spearman correlation analysis showed that approach "
    "play and putting are the most important "
    "factors. This will be reported to the "
    "client."
    "</div>",
    unsafe_allow_html=True
)

# Hypothesis Two
st.subheader("Hypothesis Two")
st.markdown(
    "<div style='background-color:#E3F2FD; padding:15px; border-radius:5px;'>"
    "<strong>Hypothesis 2:</strong> For players finishing between 30th and "
    "11th, improved putting was expected to be the most important factor for "
    "top-ten finishes.<br><br>"
    "- <strong>This was also proved false.</strong> Average strokes gained "
    "analysis between these two player groups showed driving and "
    "around-the-green shots were the largest differences. These  "
    "results will also be reported to the client."
    "</div>",
    unsafe_allow_html=True
)

# Hypothesis Three
st.subheader("Hypothesis Three")
st.markdown(
    "<div style='background-color:#E8F5E9; padding:15px; border-radius:5px;'>"
    "<strong>Hypothesis 3:</strong> All strokes gained categories (driving, "
    "approach play, around the green, and putting) were expected to "
    "play a role in top-ten finishes.<br><br>"
    "- <strong>This was confirmed.</strong> Classification and clustering "
    "showed that multiple strokes gained metrics contribute to top-ten "
    "performance. A balanced skill set is important for elite "
    "golfers."
    "</div>",
    unsafe_allow_html=True
)
