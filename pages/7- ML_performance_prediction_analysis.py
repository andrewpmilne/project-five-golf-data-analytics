import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import json
import os
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score


def page_predict_tournament_body():

    save_dir = "outputs/pipelines"

    pipe_path = os.path.join(
        save_dir, "tournament_prediction_pipeline.pkl"
    )
    best_pipe = joblib.load(pipe_path)

    meta_path = os.path.join(save_dir, "metadata.json")
    with open(meta_path, "r") as f:
        metadata = json.load(f)

    X_train = pd.read_csv(os.path.join(save_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(save_dir, "y_train.csv"))
    X_test = pd.read_csv(os.path.join(save_dir, "X_test.csv"))
    y_test = pd.read_csv(os.path.join(save_dir, "y_test.csv"))

    feat_img_path = os.path.join(save_dir, "feature_importance.png")
    feat_img = plt.imread(feat_img_path)

    st.write("### ML Pipeline: Predict Tournament Finish")
    st.info(
        "* Predicts player finishing position using strokes gained data.\n"
        "* Final model: tuned XGBoost Regressor.\n"
        "* Features: putting, approach, around-the-green, off-the-tee.\n"
        "* Results include feature importance and performance metrics."
    )

    st.write("---")
    st.write("### Tuned Hyperparameters")

    tuned_params = {
        "n_estimators": best_pipe.get_params()["n_estimators"],
        "learning_rate": best_pipe.get_params()["learning_rate"],
        "max_depth": best_pipe.get_params()["max_depth"],
        "subsample": best_pipe.get_params()["subsample"],
        "colsample_bytree": best_pipe.get_params()["colsample_bytree"]
    }

    st.json(tuned_params)

    st.write("---")
    st.write("### Features Used")
    st.write(metadata["features"])
    st.image(feat_img, caption="Feature Importance")

    st.write("---")
    st.write("## Model Performance")

    def eval_plot(X, y, name):
        preds = best_pipe.predict(X)
        size = 70
        y_true = y.values.flatten() * size
        y_pred = preds * size

        y_true = np.clip(np.round(y_true), 1, size)
        y_pred = np.clip(np.round(y_pred), 1, size)

        mae = mean_absolute_error(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_true, y_pred)

        st.write(f"### {name} Set Metrics")
        st.write(f"* MAE: {mae:.2f}")
        st.write(f"* RMSE: {rmse:.2f}")
        st.write(f"* R²: {r2:.4f}")

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.scatter(y_true, y_pred, alpha=0.6)
        ax.plot([1, size], [1, size], 'r--')
        ax.set_xlabel("Actual Position")
        ax.set_ylabel("Predicted Position")
        ax.set_title(f"Predicted vs Actual ({name})")
        ax.grid(True)
        st.pyplot(fig)

    eval_plot(X_train, y_train, "Train")
    eval_plot(X_test, y_test, "Test")

page_predict_tournament_body()
