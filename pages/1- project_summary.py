import streamlit as st

st.title("📄 Project Summary")

# Welcome
st.markdown(
    "<div style='background-color:#f0fff0;padding:15px;border-radius:10px;"
    "margin-bottom:15px'>"
    "<h1>👋 Welcome to the Golf Predictive Analytics Dashboard</h1>"
    "<p>This dashboard presents a full analytical study designed to help a "
    "professional golf coaching company better understand elite-level "
    "performance and guide targeted player development strategies.</p>"
    "</div>",
    unsafe_allow_html=True
)

# README Link
st.info(
    "### 📘 Full Project Documentation\n"
    "To view the complete README for this project, click the link below:\n\n"
    "🔗 **[GitHub README]"
    "(https://github.com/andrewpmilne/project-five-golf-data-analytics/"
    "blob/main/README.md)**"
)

# Project Overview
st.markdown(
    "<div style='background-color:#fff0f5;padding:15px;border-radius:10px;"
    "margin-bottom:15px'>"
    "<h2>🎯 Project Overview</h2>"
    "<p>This study was developed to address <b>three core business "
    "requirements</b> defined by a professional golf coaching company.</p>"
    "<p>The primary goal is to provide <b>data-driven insights</b> into:</p>"
    "<ul>"
    "<li>which skills are most strongly associated with elite tournament "
    "performance,</li>"
    "<li>how players can be grouped based on their strokes gained skill "
    "profiles,</li>"
    "<li>and how a player's finishing position can be predicted using "
    "machine learning.</li>"
    "</ul>"
    "<p>These insights aim to help coaches:</p>"
    "<ul>"
    "<li>gain a deeper understanding of which skillsets matter most at "
    "elite level,</li>"
    "<li>identify typical player types and their strengths and weaknesses,"
    "</li>"
    "<li>target coaching interventions more accurately,</li>"
    "<li>and support players seeking to move into regular <b>top-ten "
    "finishing positions</b>.</li>"
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)

# Business Requirements
st.markdown(
    "<div style='background-color:#f5f5dc;padding:15px;border-radius:10px;"
    "margin-bottom:15px'>"
    "<h2>🏆 Business Requirements</h2>"
    "<p>A golf coaching Company has approached us to conduct a study to help "
    "them analyse the foci of their coaching techniques with prospective "
    "elite-level golfing clients. They wish to attract clients who are "
    "currently playing professionally but do not yet have the skill level or "
    "consistency to regularly finish in the top ten of tournaments.</p>"
    "<p>They have suggested three primary business requirements:</p>"
    "<h3>Business Requirement One</h3>"
    "<p>The client wishes us to conduct an analysis of current elite-level "
    "golf tournament data to determine which golfing skills (e.g., driving, "
    "approach play, chipping, and putting) are most likely to result in a "
    "player reaching the top ten of a tournament.</p>"
    "<h3>Business Requirement Two</h3>"
    "<p>They wish to group elite-level golfers based on their skills in order "
    "to further determine which style of golfer they could identify for "
    "improvement.</p>"
    "<h3>Business Requirement Three</h3>"
    "<p>Once they have worked with a player and gained an understanding of "
    "their 'strokes gained' performance, they would like us to deliver a "
    "machine learning (ML) model capable of reliably predicting the finishing "
    "position of a player based on their current level of skill in each "
    "strokes gained area.</p>"
    "</div>",
    unsafe_allow_html=True
)

# Project Terms & Jargon
st.markdown(
    "<div style='background-color:#fff8dc;padding:15px;border-radius:10px;"
    "margin-bottom:15px'>"
    "<h2>📚 Project Terms & Jargon</h2>"
    "<p><b>PGA Tour:</b> The PGA Tour is a professional golf circuit "
    "in the United States, featuring the world’s top male golfers. It "
    "organises most of the major golf tournaments played throughout the "
    "year.</p>"
    "<p><b>Golf Tournament:</b> A competitive event where golfers "
    "play multiple rounds (typically four, over four days) on a specific "
    "course. Each player's performance is measured by the number of strokes "
    "taken, with the goal of completing the course in as few strokes as "
    "possible. Usually, around 120 players take part in a tournament, so "
    "finishing in the top ten would be considered a good achievement for "
    "most.</p>"
    "<p><b>The Cut:</b> After the first two rounds (36 holes) of an event, "
    "a score threshold known as the cut is applied. Only players whose total "
    "strokes are at or below this threshold continue to play the final two "
    "rounds. The rest are eliminated. The cut ensures that only the top-"
    "performing players compete in the weekend rounds.</p>"
    "<p><b>Strokes Gained:</b> A performance metric developed to quantify how "
    "a golfer’s performance compares to the field average. It measures how "
    "many strokes a player gains or loses relative to the typical performance "
    "of other players on each shot or play category.</p>"
    "</div>",
    unsafe_allow_html=True
)

# Dataset Description
st.markdown(
    "<div style='background-color:#e0ffff;padding:15px;border-radius:10px;"
    "margin-bottom:15px'>"
    "<h2>📊 Dataset Description</h2>"
    "<p>The dataset used in this study contains PGA Tour performance data for "
    "years 2015–2022. It includes player-level statistics, strokes gained "
    "metrics (Driving, Approach, Around-the-Green, Putting), and finishing "
    "positions for tournaments.</p>"
    "<p>These data allow detailed analysis of elite professional golfers and "
    "their performance profiles over time.</p>"
    "<p>📂 <b>Source:</b> <a href='https://www.kaggle.com/datasets/robikscube/"
    "pga-tour-golf-data-20152022' target='_blank'>Kaggle – PGA Tour Golf Data "
    "(2015–2022)</a></p>"
    "</div>",
    unsafe_allow_html=True
)
