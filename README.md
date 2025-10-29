# Golf Predictive Analytics using Machine Learning

## Introduction

Welcome to the readme file for the Golf Predictive Analytics study. Here you will find all information related to the project, including the business case, testing details, and instructions for deployment.

## 

## Business Case

A golf coaching company has approached us to conduct a study to help them analyse the foci of their coaching techniques with prospective elite-level golfing clients. They wish to attract clients who are currently playing professionally but do not yet have the skill level or consistency to regularly finish in the top ten of tournaments. They have suggested two primary business requirements:

- **Business Requirement One**
  - The client wishes us to conduct an analysis of current elite-level golf tournament data to determine which golfing skills (e.g., driving, approach play, chipping, and putting) are most likely to result in a player reaching the top ten of a tournament. 
  - They are specifically interested in learning which skill to focus on to help a player improve from a 30th–11th place finish to a top-ten finish.

- **Business Requirement Two**
  - Once they have worked with a player and gained an understanding of their 'strokes gained' performance, they would like us to deliver a machine learning (ML) system capable of reliably predicting the chances of a player finishing in the top ten of a tournament based on their current level of performance.
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

