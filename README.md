# Golf Predictive Analytics using Machine Learning

## Introduction

Welcome to the readme file for the Golf Predictive Analytics study. Here you will find all information related to the project, including the business case, testing details, and instructions for deployment.

## 

## Business Requirements

A golf coaching company has approached us to conduct a study to help them analyse the foci of their coaching techniques with prospective elite-level golfing clients. They wish to attract clients who are currently playing professionally but do not yet have the skill level or consistency to regularly finish in the top ten of tournaments. They have suggested two primary business requirements:

- **Business Requirement One**
  - The client wishes us to conduct an analysis of current elite-level golf tournament data to determine which golfing skills (e.g., driving, approach play, chipping, and putting) are most likely to result in a player reaching the top ten of a tournament. 
  - They are specifically interested in learning which skill to focus on to help a player improve from a 30th–11th place finish to a top-ten finish.

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
  Measures a player’s performance with the driver or tee shots on par 4s and par 5s. It reflects how effectively a player starts each hole compared to the field average.

- **Approach Play (Strokes Gained: Approach the Green)**  
  Evaluates a player’s shots from the fairway or rough (excluding tee shots on par 4s and 5s). It measures accuracy and distance control when hitting toward the green.

- **Around the Green (Strokes Gained: Around the Green)**  
  Captures short-game performance on shots taken within 30 yards of the green (excluding putting). It reflects skill in chipping, pitching, and bunker shots.

- **Putting (Strokes Gained: Putting)**  
  Measures performance on the green, comparing how efficiently a player completes holes with the putter versus the field average.

  
## Hypotheses and How to Validate

- **Hypothesis 1: Strokes gained in driving will show the strongest correlation with whether a player finishes in the top ten or not.**  
  *Validation:*  
  A correlation study will be conducted to determine the relationship between strokes gained in driving and a player’s likelihood of finishing in the top ten.

- **Hypothesis 2: For players regularly finishing between 30th and 11th, improved putting statistics will be the most likely factor in achieving top-ten finishes.**  
  *Validation:*  
  In a comparison study between players regularly finishing 30th–11th and those regularly finishing in the top ten, examine feature importance or model coefficients to determine which skill category most strongly influences the prediction.

  - **Hypothesis 3: In reality, although they may be some small statistical differences, all strokes gained categories (driving, approach play, around the green, and putting) will play an important role in achieving top-ten finishes.**  
  *Validation:*  
  Train a classification model using all strokes gained metrics as features to predict whether a player finishes in the top ten. Examine feature importance or model coefficients to assess the contribution of each skill category.

  ## Mapping Business Requirements to Data Analysis and ML Tasks

### Business Requirement One: Data Visualisation and Correlation Study

- We will inspect the tournament and player performance data.  
- We will conduct a correlation study (e.g., Pearson and Spearman) to understand how different strokes gained metrics relate to top-ten finishes.  
- We will compare players regularly finishing 11th–30th with those regularly finishing in the top ten, and use data visualisation to highlight differences in key skills.  
- We will visualise key variables against finishing position or top-ten status to gain insights into which skills are most impactful.

### Business Requirement Two: Classification, Regression, Cluster and Data Analysis

- We want to predict whether a player will finish in the top ten or not. We will build a **binary classification model** using strokes gained metrics as features.  
- We may also predict a player’s **exact finishing position**. Depending on performance, we can approach this as a regression problem or convert it to classification into finishing bands (e.g., top 10, 11–30, 31+).  
- We want to cluster players with similar performance profiles to understand patterns in skills and results.  
- We want to profile each cluster to provide actionable insights for coaching, such as which skill improvements are most likely to most likely to move a player into a top-ten group.

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









