# Golf Predictive Analytics using Machine Learning

## Introduction

Welcome to the readme file for the Golf Predictive Analytics study. Here you will find all information related to the project, including the business case, testing details, and instructions for deployment.

## Business Requirements

A golf coaching company has approached us to conduct a study to help them analyse the foci of their coaching techniques with prospective elite-level golfing clients. They wish to attract clients who are currently playing professionally but do not yet have the skill level or consistency to regularly finish in the top ten of tournaments. They have suggested two primary business requirements:

- **Business Requirement One**
  - The client wishes us to conduct an analysis of current elite-level golf tournament data to determine which golfing skills (e.g., driving, approach play, chipping, and putting) are most likely to result in a player reaching the top ten of a tournament. 
  - They are specifically interested in learning which skill to focus on to help a player improve from a 30th–11th place finish to a top-ten finish.
  - They wish to group elite level golfers based on their skills in order to further determine which style of play is most likely to result in success.

- **Business Requirement Two**
  - Once they have worked with a player and gained an understanding of their 'strokes gained' performance, they would like us to deliver a machine learning (ML) model capable of reliably predicting the chances of a player finishing in the top ten of a tournament based on their current level of performance.
  - They could also be interested in an ML system that can predict the exact finishing position of a player based on their current level of performance.

## Project Terms and Jargon

- **PGA Tour**  
  The PGA Tour is the primary professional golf circuit in the United States, featuring the world’s top male golfers. It organises most of the major golf tournaments played throughout the year.

- **Golf Tournament**  
  A competitive event where professional golfers play multiple rounds (typically four, over four days) on a specific course. Each player's performance is measured by the number of strokes taken, with the goal of completing the course in as few strokes as possible. Usually, around 120 players will take part in a tournament, so finishing in the top ten would be considered a good achievement for most.

- **The Cut**  
  After the first two rounds (36 holes) of a tournament, a score threshold known as *the cut* is applied. Only players whose total strokes are at or below this threshold continue to play the final two rounds. The rest are eliminated from the tournament. The cut ensures that only the top-performing players compete in the weekend rounds.

- **Strokes Gained**  
  A performance metric developed to quantify how a golfer’s performance compares to the field average. It measures how many strokes a player gains or loses relative to the typical performance of other players on each shot or play category.

### Categories of Strokes Gained Data

- **Driving (Strokes Gained: Off the Tee)**  
  Measures a player’s performance with the driver or tee shots. It reflects how effectively a player starts each hole compared to the field average.

- **Approach Play (Strokes Gained: Approach the Green)**  
  Evaluates a player’s shots from the fairway or rough. It measures accuracy and distance control when hitting toward the green.

- **Around the Green (Strokes Gained: Around the Green)**  
  Captures short-game performance on shots taken within 30 yards of the green (excluding putting). It reflects skill in chipping, pitching, and bunker shots.

- **Putting (Strokes Gained: Putting)**  
  Measures performance on the green, comparing how efficiently a player completes holes with the putter versus the field average.
  
## Business Case Assessment

**Is there any business requirement that can be answered with conventional data analysis?**  
Yes. Conventional data analysis can be used to:
- Investigate correlations between strokes gained metrics and top-ten finishes.
- Compare the performance profiles of players regularly finishing 11th–30th with those finishing in the top ten. 

**Does the client need a dashboard or an API endpoint?**  
The client requires a **dashboard**, allowing coaches to explore player performance, view correlations, clusters, and run predictions for individual players.  

**What does the client consider a successful project outcome?**  
- Identification of the most relevant skill areas that correlate with top-ten finishes.  
- Ability to predict the likelihood of a player achieving a top-ten finish.  
- Insights into player clusters and performance profiles to guide coaching strategies.  

**Can you break down the project into Epics and User Stories?**  
- **Information gathering and data collection:** Obtain historical PGA Tour performance data (2015–2022).  
- **Data visualisation, cleaning, and preparation:** Prepare strokes gained metrics, handle missing values, and visualise correlations.  
- **Model training, optimisation, and validation:** Train classification models for top-ten prediction and clustering models for player profiles.  
- **Dashboard planning, designing, and development:** Design interactive visualisations and prediction interfaces.  
- **Dashboard deployment and release:** Launch the Streamlit app for client access and testing.  

**Ethical or Privacy concerns?**  
No. The dataset consists of publicly available PGA Tour performance statistics.  Although names are included, they are of professional golfers whose perforance data is already in the public eye. No personal or senstitive data is included.

**Does the data suggest a particular model?**  
Yes. The data supports:  
- A **binary classifier** for predicting top-ten finishes.  
- **Unsupervised clustering** to group players by performance profiles.  

**What are the model's inputs and intended outputs?**  
- **Inputs:** Strokes gained metrics (Driving, Approach Play, Around the Green, Putting) and tournament finishing positions.  
- **Outputs:**  
  - Binary flag for top-ten likelihood with associated probability.  
  - Cluster assignment indicating the player’s performance group.  

**What are the criteria for the performance goal of the predictions?**  
- At least **80% recall** for top-ten players.  
- At least **80% precision** for non-top-ten predictions.  
- Clusters must show **clear separation** and meaningful differences in average strokes gained metrics.  

**How will the client benefit?**  
- Coaches can focus training on the skill areas most predictive of top-ten performance.  
- Data-driven predictions help identify players with the highest potential for success.  
- Player clustering provides actionable insights for targeted coaching strategies.  

  
## Hypotheses and How to Validate

- **Hypothesis 1: Strokes gained in driving will show the strongest correlation as to whether a player finishes in the top ten or not.**  
  *Validation:*  
  A correlation study will be conducted to determine the relationship between strokes gained in driving and a player’s likelihood of finishing in the top ten.

- **Hypothesis 2: For players regularly finishing between 30th and 11th, improved putting statistics will be the most likely factor in achieving top-ten finishes.**  
  *Validation:*  
  In a comparison study between players regularly finishing 30th–11th and those regularly finishing in the top ten, examine feature importance or model coefficients to determine which skill category most strongly influences the prediction.

  - **Hypothesis 3: In reality, although they may be some small statistical differences, all strokes gained categories (driving, approach play, around the green, and putting) will play an important role in achieving top-ten finishes.**  
  *Validation:*  
  Train a classification model using all strokes gained metrics as features to predict whether a player finishes in the top ten. Examine feature importance or model coefficients to assess the contribution of each skill category.

## Rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement One: Data Visualisation, Correlation, and Clustering

- We will inspect the tournament and player performance data.  
- We will conduct a correlation study (e.g., Pearson and Spearman) to understand how different strokes gained metrics relate to top-ten finishes.  
- We will compare players regularly finishing 11th–30th with those regularly finishing in the top ten, and use data visualisation to highlight differences in key skills.  
- We will visualise key variables against finishing position or top-ten status to gain insights into which skills are most impactful.  
- We will cluster players with similar performance profiles to identify patterns in skills and results, helping coaches understand typical player types and areas for improvement.

### Business Requirement Two: Predictive Modelling

- We want to predict whether a player will finish in the top ten or not. We will build a **binary classification model** using strokes gained metrics as features.  
- We may also predict a player’s **exact finishing position**. Depending on performance, we can approach this as a regression problem or convert it to classification into finishing bands (e.g., top 10, 11–30, 31+).  
- Model outputs will provide actionable insights for coaches about which players are likely to reach the top ten.


## ML Business Case

### Predict Top-Ten Finishes
**Classification Model**

We aim to develop a machine learning (ML) model that predicts whether a professional golfer will finish in the top ten of a tournament based on their performance statistics (strokes gained metrics).  
The target variable is categorical with two classes:
- **0:** Player finishes outside the top ten  
- **1:** Player finishes in the top ten  

This is a **supervised, two-class, single-label classification problem**.

Our ideal outcome is to provide reliable insights into which skill areas most strongly influence a player’s likelihood of achieving a top-ten finish. This will support coaches in prioritising the right technical areas for player development.

**Model success metrics:**
- At least **80% recall** for predicting top-ten finishes on both training and test datasets (to ensure the model captures most true top-ten players).  
- At least **80% precision** for predicting non-top-ten finishes (to avoid incorrectly classifying too many players as top-ten prospects).

**The ML model is considered a failure if:**
- After evaluation, more than **30% of actual top-ten players** are missed by the model (indicating low recall).  
- **Precision for non-top-ten predictions** falls below 80% on the train and test sets (indicating excessive false positives).  

**Model output:**
The model output will include a **binary flag** indicating whether a player is likely to finish in the top ten, along with an **associated probability score**.
These predictions will be made on demand, allowing coaches or analysts to input a player’s strokes gained statistics and instantly view their top-ten probability.

**Heuristics:**
Currently, there is **no formal analytical approach** that we are aware of used to predict top-ten likelihood among professional golfers. This model aims to fill that gap by quantifying the skill combinations most predictive of elite performance.

**Training Data:**
The training data will consist of historical player performance records from official tournaments on the PGA tour between 2015 and 2022. 
- **Target:** Top-ten finish (yes/no)  
- **Features:** Strokes gained metrics (Driving, Approach Play, Around the Green, Putting).

### Cluster Player Performance Profiles
**Clustering Model**

We aim to develop an unsupervised learning model that groups players with similar performance characteristics based on their strokes gained metrics. The objective is to identify patterns in skill profiles and understand which combinations of strengths and weaknesses are most associated with success at the elite level.

This will allow coaches to:
- Identify player types (e.g., strong drivers vs precision putters).
- Understand how current performance profiles compare to those of regular top-ten finishers.
- Target development strategies specific to each cluster to help players improve their overall ranking potential.

**Model success metrics:**
- The clusters must show **clear separation** between groups (e.g., measured by silhouette score).  
- Each cluster should demonstrate **meaningful differences** in average performance statistics across strokes gained categories.  

**Model output:**
The model will output a **cluster assignment** for each player, indicating their performance group, along with **summary statistics** (average strokes gained per category) for each cluster.  
These clusters will be visualised using 2D or 3D plots to make interpretation straightforward for coaches.

**Heuristics:**
Currently, performance analysis is often conducted on an individual basis or using simple averages. Clustering will allow for **data-driven analysis**, helping coaches to identify which players are most similar to elite performers and which specific areas need targeted improvement.

**Training Data:**
The training data will use the same strokes gained and tournament performance dataset as the classification model.  
- **Target:** None (unsupervised learning).  
- **Features:** Strokes gained metrics (Driving, Approach Play, Around the Green, Putting).

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
- **Quick project summary**  
  Provide a high-level overview of the Golf Predictive Analytics study, its objectives, and expected outcomes.  

- **Project Terms & Jargon**  
  Include definitions for PGA Tour, Golf Tournament, Strokes Gained, The Cut, and the categories of strokes gained data (Driving, Approach Play, Around the Green, Putting).  

- **Describe Project Dataset**  
  Summarise the historical tournament data, the number of players, number of tournaments, and which features (strokes gained metrics, finishing positions) are available.  

- **State Business Requirements**  
  Present Business Requirement One (exploratory analysis, correlation study and clustering) and Business Requirement Two (ML predictive modelling).  

---

### Page 2: Player Performance Analysis
- **State Business Requirement One**  
  Explore patterns in the historical player data and provide context for the analysis. This page addresses Business Requirement One, focusing on understanding which strokes gained metrics are most associated with top-ten finishes.  

- **Display the most correlated variables with top-ten finishes and conclusions**  
  Highlight which strokes gained metrics have the strongest correlation with achieving top-ten finishes. Include insights and interpretations from the correlation study (Pearson or Spearman as appropriate).  

- **Parallel plot using finishing position and correlated variables**  
  Provide a parallel coordinates plot to allow coaches and analysts to compare multiple correlated metrics across finishing positions in one visualisation.

- **Highlight differences in performance between 11–30th place finishers and top-ten finishers**  
  Visualise and compare the distributions of key strokes gained metrics for players finishing 11th–30th versus those in the top ten. Highlight which skill categories show the largest differences.  

- **Clustering Insights**  
  Display clusters of players with similar performance profiles based on aggregated strokes gained metrics. Show average values for each cluster, highlight patterns, and provide actionable insights for coaching strategies.

---

### Page 3: Player Top-Ten Predictor
- **State Business Requirement Two**  
  Predict whether a player is likely to finish in the top ten in upcoming tournaments.  

- **Set of widget inputs for player profile**  
  Include strokes gained metrics

- **"Run predictive analysis" button**  
  Feeds the player profile to the ML pipelines:  
  - Predicts **top-ten likelihood** with associated probability.  
  - Determines the **cluster assignment** for the player and displays the cluster profile.  

---

### Page 4: Project Hypotheses and Validation
- Before analysis: describe each hypothesis.  
- After analysis: report conclusions and validation results. Example hypotheses:  
  1. **Driving strokes gained will have the strongest correlation with top-ten finishes**  
     - Confirmed through correlation studies and classification model insights.  
  2. **For players regularly finishing 11th–30th, improved putting is the key factor for top-ten improvement**  
     - Validated through comparison studies and ML feature importance.  
  3. **All strokes gained categories are important for top-ten success**  
     - Confirmed via classification model and cluster analysis showing multiple skills influencing outcomes.  

---

### Page 5: ML - Predict Top-Ten Finishes
- Considerations and conclusions after training the pipeline.  
- Present ML pipeline steps (data preprocessing, feature selection, model training).  
- Show **feature importance** (which strokes gained metrics matter most).  
- Present **pipeline performance** metrics (accuracy, recall, precision).  

---

### Page 6: ML - Cluster Analysis
- Considerations and conclusions after clustering players.  
- Present clustering pipeline steps (aggregation, scaling, algorithm choice).  
- Display **silhouette plot** to evaluate cluster separation.  
- Show **distribution of clusters across top-ten vs 11–30 finishes**.  
- Show **relative percentage of top-ten players in each cluster**.  
- Display **most important features defining each cluster**.  
- Present **cluster profile** with average strokes gained metrics and coaching insights.










