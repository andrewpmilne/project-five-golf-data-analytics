import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_golf_data, load_player_comparisons


sns.set_style("whitegrid")

# --- Main page ---
def page_player_performance_study_body():
    st.title("⛳ Player Performance Study")

    df = load_golf_data()
    top_15_players, mid_15_players = load_player_comparisons()

    sg_features = [
        'sg_ott', 'sg_app', 'sg_arg', 'sg_putt', 'sg_t2g', 'sg_total'
        ]
    sg_features_avg = ['avg_sg_putt', 'avg_sg_arg', 'avg_sg_app', 'avg_sg_ott',
                       'avg_sg_t2g', 'avg_sg_total']

    # --- Data inspection ---
    st.subheader("🔍 Inspect Player Data")
    st.write("* The dataset contains **{} rows** and **{} columns**.".format(
        df.shape[0], df.shape[1]
    ))

    if st.checkbox("Show first 5 rows of the dataset"):
        st.dataframe(df.head(5))

    st.markdown("---")

    # --- Player Performance Study Overview ---
    st.markdown(
        "<div style='background-color:#e6f2ff;"
        "padding:15px;"
        "border-radius:10px'>"
        "<h2>⛳ Player Performance Study Overview</h2>"
        "<p>This section addresses <b>Business Requirement One</b>: "
        "identifying which golfing skills (driving, approach play, "
        "chipping, and putting) are most likely to result in a top-ten "
        "tournament finish.</p>"
        "<p>The analysis was conducted in two stages:</p>"
        "<ul>"
        "<li><b>Top-Ten vs. All Players</b> – Compare top-ten finishers "
        "with all players to examine differences in strokes gained.</li>"
        "<li><b>Top-Ten vs. Mid-Range Players (11th–30th)</b> – Focus "
        "on players who finish just outside the top-ten to find skill "
        "differences.</li>"
        "</ul>"
        "<p>The study evaluates:</p>"
        "<ul>"
        "<li>Average strokes gained per category,</li>"
        "<li>Differences between groups to highlight improvement areas,</li>"
        "<li>Distributions and correlations of strokes gained metrics.</li>"
        "</ul>"
        "<p>This provides insights for player development and predictive "
        "modelling to support top-ten finishes.</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("## 📊 Comparison of Top-Ten Players and the Field")

    st.markdown(
        "<div style='background-color:#f7f7f2;padding:20px;border-radius:10px;"
        "border:1px solid #e0e0d6;'>"
        "<h3>Comparison Overview</h3>"
        "<p>Analyses conducted to compare top-ten players with the rest:</p>"
        "<ul>"
        "<li><b>Average Strokes Gained</b> – Compare mean values by category "
        "between top-ten and all players.</li>"
        "<li><b>Difference Analysis</b> – Bar charts showing differences "
        "between top-ten and field.</li>"
        "<li><b>Pairwise Relationships</b> – Visualise interactions using "
        "Seaborn pairplots.</li>"
        "<li><b>Correlation Analysis</b> – Spearman heatmap of strokes gained "
        "metrics vs finishing position.</li>"
        "</ul>"
        "<p>These provide a view of which skills separate elite performers "
        "from the rest.</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.write("")
    show_top10_plots = st.checkbox("Show Top-Ten vs Field Plots 📊")

    if show_top10_plots:
        st.subheader("Top-Ten vs Field: Visual Analysis")

        # Average SG bar chart
        avg_sg = df.groupby('top_ten')[sg_features].mean()
        avg_sg.T.plot(kind='bar', figsize=(10, 6))
        plt.title("Average Strokes Gained: Top-Ten vs Non-Top-Ten")
        plt.xlabel("Strokes Gained Category")
        plt.ylabel("Average SG")
        plt.xticks(rotation=0)
        plt.legend(title="Top Ten", labels=["Not Top Ten", "Top Ten"])
        st.pyplot(plt.gcf())
        plt.clf()

        # Difference bar chart
        diff_sg = avg_sg.loc[1] - avg_sg.loc[0]
        plt.figure(figsize=(10, 6))
        diff_sg.plot(kind='bar', color='skyblue')
        plt.title("Difference in Average Strokes Gained")
        plt.xlabel("Strokes Gained Category")
        plt.ylabel("Difference (Top Ten - Not Top Ten)")
        plt.xticks(rotation=0)
        st.pyplot(plt.gcf())
        plt.clf()

        # Pairplot
        st.write("Pairwise relationships of strokes gained metrics:")
        sns.pairplot(df[sg_features + ['top_ten']], hue='top_ten',
                     palette=['grey', 'blue'])
        st.pyplot(plt.gcf())
        plt.clf()

        # Spearman correlation heatmap
        st.write("Spearman correlation heatmap:")
        corr_spearman = df[sg_features + ['top_ten']].corr(method='spearman')
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_spearman, annot=True, cmap='coolwarm', center=0)
        plt.title("Spearman Correlation Heatmap")
        st.pyplot(plt.gcf())
        plt.clf()

    # --- Analysis Notes ---
    st.markdown(
        "<div style='background-color:#f0f8ff;padding:15px;border-radius:10px;"
        "border:1px solid #d0e0f0;'>"
        "<h3>📌 Analysis</h3>"
        "<ul>"
        "<li><b>T2G & Total SG</b> metrics cover multiple strokes. Not "
        "relevant to this study.</li>"
        "<li><b>Putting & Approach Play</b> are key factors for top-ten "
        "performance, confirmed by heatmap and plots.</li>"
        "<li>Pairwise plots show all features generally contribute to "
        "top-ten finishes.</li>"
        "<li>Heatmap also indicated that as no particular metric dominates, "
        "a balanced skill set is important.</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.subheader("📊 Comparison: Players 11th–30th vs Top-Ten")

    st.markdown(
        "<div style='background-color:#f7f7f2;padding:15px;border-radius:10px;"
        "border:1px solid #e0e0d6;'>"
        "<p>Precomputed data identifies players in 11th–30th and compares "
        "their average strokes gained to top-ten players.</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("")

    show_midrange_plots = st.checkbox("Show 11th–30th vs Top-Ten Plots 📊")

    if show_midrange_plots:
        st.subheader("Mid-Range vs Top-Ten: Visual Analysis")

        top_ten_avg = top_15_players[sg_features_avg].mean()
        mid_avg = mid_15_players[sg_features_avg].mean()

        plot_df = pd.DataFrame({
            'Strokes Gained Metric': sg_features_avg,
            'Top-Ten Players': top_ten_avg.values,
            'Mid-Range Players': mid_avg.values
        })

        plot_df_melted = plot_df.melt(
            id_vars='Strokes Gained Metric',
            var_name='Player Group',
            value_name='Average SG'
        )

        plt.figure(figsize=(10, 6))
        sns.barplot(
            x='Strokes Gained Metric',
            y='Average SG',
            hue='Player Group',
            data=plot_df_melted
        )
        plt.title("Average SG: Top-Ten vs Mid-Range")
        plt.ylabel("Average SG")
        plt.xlabel("Metric")
        plt.xticks(rotation=45)
        plt.legend(title="Player Group")
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()

        # Difference plot
        diff = top_ten_avg - mid_avg
        diff_df = pd.DataFrame({
            'Strokes Gained Metric': sg_features_avg,
            'Difference': diff.values
        })

        plt.figure(figsize=(10, 6))
        sns.barplot(
            x='Strokes Gained Metric',
            y='Difference',
            data=diff_df,
            palette='viridis'
        )
        plt.title("Difference in SG: Top-Ten vs Mid-Range")
        plt.ylabel("Difference")
        plt.xlabel("Metric")
        plt.xticks(rotation=45)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()

        # KDE plots
        plt.figure(figsize=(16, 12))
        for i, metric in enumerate(sg_features_avg, 1):
            plt.subplot(2, 3, i)
            sns.kdeplot(top_15_players[metric], label='Top-Ten', fill=True)
            sns.kdeplot(mid_15_players[metric], label='Mid-Range', fill=True)
            plt.title("Distribution of {}".format(metric))
            plt.xlabel("Strokes Gained")
            plt.ylabel("Density")
            plt.legend()
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()

    # --- Analysis notes for mid-range vs top-ten ---
    st.markdown(
        "<div style='background-color:#f0f8ff;padding:15px;border-radius:10px;"
        "border:1px solid #d0e0f0;'>"
        "<h3>📌 Analysis</h3>"
        "<ul>"
        "<li><b>Chipping & Driving Skills:</b> Mid-range players need "
        "improvement in these areas to bridge gap to top-ten. When "
        "driving, boths sets have similar max 'ceilings' but top-ten "
        "players are more consistently good.</li>"
        "<li><b>Around the Green Differences:</b> KDE plots show elite "
        "players have consistent performance and a higher 'ceiling'; "
        "mid-range players vary.</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )


# Run the page
page_player_performance_study_body()
