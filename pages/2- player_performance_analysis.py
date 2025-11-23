import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

# Load the cleaned golf data
@st.cache_data
def load_golf_data():
    df = pd.read_csv("outputs/data/final/cleaned_golfdata.csv")
    return df

def page_player_performance_study_body():
    st.title("⛳ Player Performance Study")

    # Load data
    df = load_golf_data()

    # Define strokes gained features
    sg_features = ['sg_ott', 'sg_app', 'sg_arg', 'sg_putt', 'sg_t2g', 'sg_total']

    # Data inspection
    st.subheader("🔍 Inspect Player Data")

    st.write(f"* The dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**.")

# Checkbox to show/hide dataframe
    if st.checkbox("Show first 5 rows of the dataset"):
        st.dataframe(df.head(5))

    st.markdown("---")

    st.markdown(
        f"<div style='background-color:#e6f2ff;padding:15px;border-radius:10px'>"
        f"<h2>⛳ Player Performance Study Overview</h2>"
        f"<p>This section addresses <b>Business Requirement One</b>: identifying which golfing "
        f"skills (driving, approach play, chipping, and putting) are most likely to result in a "
        f"top-ten tournament finish.</p>"

        f"<p>The analysis was conducted in two stages:</p>"
        f"<ul>"
        f"<li><b>Top-Ten vs. All Players</b> – Initially, we compared top-ten finishers with the "
        f"entire field to examine overall differences in strokes gained metrics and highlight general patterns.</li>"
        f"<li><b>Top-Ten vs. Mid-Range Players (11th–30th)</b> – Next, to comply with the wishes of the client, "
        f"we focused on players who regularly finish just outside the top ten on average, with players who " 
        f"consistently do finish inside the top ten, to identify differences in their skillsets "
        f"(e.g., chipping, driving) that could help someone of that particular standard "
        f"to break into the top ten.</li>"
        f"</ul>"

        f"<p>The study evaluates:</p>"
        f"<ul>"
        f"<li>Average strokes gained per category,</li>"
        f"<li>Differences between player groups to highlight key areas for improvement,</li>"
        f"<li>Distributions and correlations of strokes gained metrics to reveal patterns in elite performance.</li>"
        f"</ul>"

        f"<p>This analysis provides actionable insights for player development and informs subsequent "
        f"predictive modelling to support top-ten finishes.</p>"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("## 📊 Comparison of Top-Ten Players and the Field")

    st.markdown(
        """
    <div style="background-color:#f7f7f2; padding:20px; border-radius:10px; border:1px solid #e0e0d6;">
    <h3>Comparison Overview</h3>

    <p>To understand how top-ten performers differ from the rest of the field, several analyses were conducted:</p>

    <ul>
    <li><b>Average Strokes Gained Comparison</b><br>
    Comparison of mean strokes gained values (driving, approach, around the green, putting) between top-ten finishers and all other players.</li>

    <li><b>Difference Analysis</b><br>
    Bar charts showing how much higher (or lower) top-ten players score in each strokes gained category relative to the field.</li>

    <li><b>Pairwise Relationships (Pairplot)</b><br>
    Visualisation of interactions between strokes gained metrics using Seaborn pairplots.</li>

    <li><b>Correlation Analysis (Spearman)</b><br>
    Heatmap illustrating how strongly each strokes gained metric relates to top-ten finishes and to true finishing position.</li>
    </ul>

    <p>These comparisons provide a broad view of which skills most consistently separate elite performers from the rest of the field.</p>
    </div>
    """,
        unsafe_allow_html=True
    )

    st.write("")

    # Checkbox to show top-ten vs field analysis plots
    show_top10_plots = st.checkbox("Show Top-Ten vs Field Plots 📊")

    if show_top10_plots:
        st.subheader("Top-Ten vs Field: Visual Analysis")

        # Average strokes gained comparison (bar chart)
        avg_sg = df.groupby('top_ten')[sg_features].mean()
        avg_sg.T.plot(kind='bar', figsize=(10,6))
        plt.title('Average Strokes Gained by Category: Top-Ten vs Non-Top-Ten')
        plt.xlabel('Strokes Gained Category')
        plt.ylabel('Average Strokes Gained')
        plt.xticks(rotation=0)
        plt.legend(title='Top Ten', labels=['Not Top Ten', 'Top Ten'])
        st.pyplot(plt.gcf())
        plt.clf()

        # Difference analysis (bar chart)
        diff_sg = avg_sg.loc[1] - avg_sg.loc[0]
        plt.figure(figsize=(10,6))
        diff_sg.plot(kind='bar', color='skyblue')
        plt.title('Difference in Average Strokes Gained: Top-Ten vs Non-Top-Ten')
        plt.xlabel('Strokes Gained Category')
        plt.ylabel('Average Difference (Top Ten - Not Top Ten)')
        plt.xticks(rotation=0)
        st.pyplot(plt.gcf())
        plt.clf()

        # Pairplot
        st.write("Pairwise relationships between strokes gained metrics:")
        sns.pairplot(df[sg_features + ['top_ten']], hue='top_ten', palette=['grey','blue'])
        st.pyplot(plt.gcf())
        plt.clf()

        # Correlation heatmap (Spearman)
        st.write("Spearman correlation heatmap:")
        corr_spearman = df[sg_features + ['top_ten']].corr(method='spearman')
        plt.figure(figsize=(8,6))
        sns.heatmap(corr_spearman, annot=True, cmap='coolwarm', center=0)
        plt.title('Spearman Correlation Heatmap')
        st.pyplot(plt.gcf())
        plt.clf()
    
    # --- Analysis Subheading and Bullet Point with light background ---
    st.markdown(
        """
        <div style="background-color:#f0f8ff; padding:15px; border-radius:10px; border:1px solid #d0e0f0;">
            <h3>📌 Analysis</h3>
            <ul>
                <li><b>Strokes Gained T2G (Tee to Green) and Strokes Gained Total</b> are metrics that encompass a range of different strokes, so it is expected they will have the biggest correlation. However, this is not relevant for our study.</li>
                <li>The plots show that <b>putting and approach play</b> are the key factors in performing well enough to reach the top ten of a tournament. This is also reflected in the heatmap.</li>
                <li>The pairwise plot shows that although there can occasionally be examples where a particularly good performance in one area can counteract a slightly weaker performance in another area (such as approach and putting), in general <b>all features are fairly significant for a top-ten finish</b>.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # --- Load precomputed player comparison data ---
    @st.cache_data
    def load_player_comparisons():
        top_15_players = pd.read_csv("outputs/data/interim/comparison/top_15_players_comparison.csv")
        mid_15_players = pd.read_csv("outputs/data/interim/comparison/mid_range_players_comparison.csv")
        return top_15_players, mid_15_players

    top_15_players, top_15_mid_players_final = load_player_comparisons()


    # --- Mid-Range vs Top-Ten Players Section ---
    st.subheader("📊 Comparison of Players Finishing 30th–11th with Top-Ten Players")

    st.markdown(
        """
        <div style='background-color:#f7f7f2; padding:15px; border-radius:10px; border:1px solid #e0e0d6;'>
        <p>We used the precomputed data to identify players who regularly reach the top ten and players who regularly finish 11–30th, 
        and compared them using their average strokes gained statistics.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Checkbox to show Mid-Range vs Top-Ten analysis plots
    show_midrange_plots = st.checkbox("Show 11th–30th vs Top-Ten Plots 📊")

    if show_midrange_plots:
        st.subheader("Mid-Range vs Top-Ten Players: Visual Analysis")

        sg_features_avg = ['avg_sg_putt', 'avg_sg_arg', 'avg_sg_app', 'avg_sg_ott', 'avg_sg_t2g', 'avg_sg_total']

        # Prepare plot dataframe
        top_ten_avg = top_15_players[sg_features_avg].mean()
        mid_avg = top_15_mid_players_final[sg_features_avg].mean()

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

        plt.figure(figsize=(10,6))
        sns.barplot(
            x='Strokes Gained Metric',
            y='Average SG',
            hue='Player Group',
            data=plot_df_melted
        )
        plt.title('Average Strokes Gained: Top-Ten vs Mid-Range Players')
        plt.ylabel('Average Strokes Gained')
        plt.xlabel('Metric')
        plt.xticks(rotation=45)
        plt.legend(title='Player Group')
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()

        # Difference plot
        diff = top_ten_avg - mid_avg
        diff_df = pd.DataFrame({
            'Strokes Gained Metric': sg_features_avg,
            'Difference (Top-Ten - Mid-Range)': diff.values
        })

        plt.figure(figsize=(10,6))
        sns.barplot(
            x='Strokes Gained Metric',
            y='Difference (Top-Ten - Mid-Range)',
            data=diff_df,
            palette='viridis'
        )
        plt.title('Difference in Average Strokes Gained: Top-Ten vs Mid-Range Players')
        plt.ylabel('Difference in Average SG')
        plt.xlabel('Metric')
        plt.xticks(rotation=45)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()

        # KDE plots
        plt.figure(figsize=(16, 12))
        for i, metric in enumerate(sg_features_avg, 1):
            plt.subplot(2, 3, i)
            sns.kdeplot(top_15_players[metric], label='Top-Ten Players', fill=True)
            sns.kdeplot(top_15_mid_players_final[metric], label='Mid-Range Players', fill=True)
            plt.title(f'Distribution of {metric}')
            plt.xlabel('Strokes Gained')
            plt.ylabel('Density')
            plt.legend()

        plt.tight_layout()
        st.pyplot(plt.gcf())
        plt.clf()
    
    # --- Analysis Subheading and Bullet Points ---
    st.markdown(
        """
        <div style="background-color:#f0f8ff; padding:15px; border-radius:10px; border:1px solid #d0e0f0;">
            <h3>📌 Analysis</h3>
            <ul>
                <li><b>Chipping and Driving Skills:</b> Interestingly, these results are in stark contrast to the previous set analysing all golfers. 
                For those already at a level to perform to a standard to regularly finish 11–30th, it would appear the skills of chipping 
                (around the green) and driving (off the tee) are the most in need of development. This suggests that targeted development 
                in these specific skills could help mid-range players bridge the gap to top-ten performance.</li>
                <li><b>Around the Green Differences:</b> The KDE plot further emphasises the difference in the 'around the green' metric 
                for elite players in comparison to mid-range players. A number of mid-range players even slip into negative around the 
                green statistics, whereas elite players are all of a very similar standard of performance.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )



# Call the function to display the page
page_player_performance_study_body()
