import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Page title
st.title("ML: Predict Tournament Finishes")

# 1. Considerations & Conclusions
st.header("Considerations & Conclusions")
st.markdown("""
- This Random Forest model predicts a player's finishing position based on strokes gained metrics:
  - `sg_putt`, `sg_arg`, `sg_app`, `sg_ott`
- Test data shows **MAE < 5 positions** when trained on finished players only (`adj_pos < 1`).
- Feature importance confirms **Putting** and **Approach** are the most critical factors influencing performance.
- The model is slightly underfitting for lower-ranked players but performs well for the client’s target range (top 30).
""")

# 2. Load pipeline and test data
pipeline = joblib.load("outputs/pipelines/tournament_prediction_pipeline.pkl")
test_data = pd.read_csv("outputs/data/final/test/test_data.csv")
val_data  = pd.read_csv("outputs/data/final/validation/val_data.csv")

# Filter out players who missed the cut
test_filtered = test_data[test_data['adj_pos'] < 1].copy()
val_filtered  = val_data[val_data['adj_pos'] < 1].copy()

sg_features = ['sg_putt', 'sg_arg', 'sg_app', 'sg_ott']

X_test_f = test_filtered[sg_features]
y_test_f = test_filtered['adj_pos']

# 3. Predict
y_test_pred = pipeline.predict(X_test_f)

# Convert scaled positions back to tournament positions
max_pos = test_filtered.groupby('tournament_id')['true_pos'].transform('max')
y_test_pred_pos = y_test_pred * (max_pos - 1) + 1
y_test_actual = test_filtered['true_pos']

# 4. Show Performance Metrics
st.header("Model Performance Metrics")
mae_positions = mean_absolute_error(y_test_actual, y_test_pred_pos)
rmse_positions = np.sqrt(mean_squared_error(y_test_actual, y_test_pred_pos))

st.markdown(f"**Test MAE:** {mae_positions:.2f} positions")
st.markdown(f"**Test RMSE:** {rmse_positions:.2f} positions")

# 5. Feature Importance
st.header("Feature Importance")
model = pipeline.named_steps['model']
importances = model.feature_importances_

fig, ax = plt.subplots()
sns.barplot(x=importances, y=sg_features, palette="viridis", ax=ax)
ax.set_xlabel("Importance")
ax.set_title("Feature Importance for Finishing Position Prediction")
st.pyplot(fig)

# 6. Predicted vs Actual Plot
st.header("Predicted vs Actual Positions (Test Set)")
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(y_test_actual, y_test_pred_pos, alpha=0.6, color='purple', edgecolor='k')
ax.plot([y_test_actual.min(), y_test_actual.max()],
        [y_test_actual.min(), y_test_actual.max()], 'r--', linewidth=2)
ax.set_xlabel("Actual Position")
ax.set_ylabel("Predicted Position")
ax.set_title("Predicted vs Actual Tournament Position")
ax.grid(True)
st.pyplot(fig)
