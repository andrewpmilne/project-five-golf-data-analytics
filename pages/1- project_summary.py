import streamlit as st

st.title("📄 Project Summary")

# Welcome
st.markdown(
    f"<div style='background-color:#f0fff0;padding:15px;border-radius:10px;margin-bottom:15px'>"
    f"<h1>👋 Welcome to the Golf Predictive Analytics Dashboard</h1>"
    f"<p>This dashboard presents a full analytical study designed to help a professional "
    f"golf coaching company better understand elite-level performance and guide targeted "
    f"player development strategies.</p>"
    f"</div>",
    unsafe_allow_html=True
)


# README Link
st.info(
    f"### 📘 Full Project Documentation\n"
    f"To view the complete README for this project, click the link below:\n\n"
    f"🔗 **[GitHub README]"
    f"(https://github.com/andrewpmilne/project-five-golf-data-analytics/blob/main/README.md)**"
)

# Project Overview
st.markdown(
    f"<div style='background-color:#fff0f5;padding:15px;border-radius:10px;margin-bottom:15px'>"
    f"<h2>🎯 Project Overview</h2>"
    f"<p>This study was developed to address <b>three core business requirements</b> defined "
    f"by a professional golf coaching company.</p>"
    f"<p>The overarching goal is to provide <b>data-driven insights</b> into:</p>"
    f"<ul>"
    f"<li>which skills are most strongly associated with elite tournament performance,</li>"
    f"<li>how players can be grouped based on their strokes gained skill profiles,</li>"
    f"<li>and how a player's finishing position can be predicted using machine learning.</li>"
    f"</ul>"
    f"<p>These insights aim to help coaches:</p>"
    f"<ul>"
    f"<li>gain a deeper understanding of which skillsets matter most at elite level,</li>"
    f"<li>identify typical player types and their strengths and weaknesses,</li>"
    f"<li>target coaching interventions more accurately,</li>"
    f"<li>and support players seeking to move into regular <b>top-ten finishing positions</b>.</li>"
    f"</ul>"
    f"</div>",
    unsafe_allow_html=True
)

# Business Requirements
st.markdown(
    f"<div style='background-color:#f5f5dc;padding:15px;border-radius:10px;margin-bottom:15px'>"
    f"<h2>🏆 Business Requirements</h2>"
    f"<p>A golf coaching Company has approached us to conduct a study to help them analyse the "
    f"foci of their coaching techniques with prospective elite-level golfing clients. They "
    f"wish to attract clients who are currently playing professionally but do not yet have "
    f"the skill level or consistency to regularly finish in the top ten of tournaments.</p>"
    f"<p>They have suggested three primary business requirements:</p>"
    f"<h3>Business Requirement One</h3>"
    f"<p>The client wishes us to conduct an analysis of current elite-level golf tournament data "
    f"to determine which golfing skills (e.g., driving, approach play, chipping, and putting) "
    f"are most likely to result in a player reaching the top ten of a tournament.</p>"
    f"<h3>Business Requirement Two</h3>"
    f"<p>They wish to group elite-level golfers based on their skills in order to further "
    f"determine which style of golfer they could identify for improvement.</p>"
    f"<h3>Business Requirement Three</h3>"
    f"<p>Once they have worked with a player and gained an understanding of their 'strokes gained' "
    f"performance, they would like us to deliver a machine learning (ML) model capable of "
    f"reliably predicting the finishing position of a player based on their current level of "
    f"skill in each strokes gained area.</p>"
    f"</div>",
    unsafe_allow_html=True
)


# Project Terms & Jargon
st.markdown(
    f"<div style='background-color:#fff8dc;padding:15px;border-radius:10px;margin-bottom:15px'>"
    f"<h2>📚 Project Terms & Jargon</h2>"
    f"<p><b>PGA Tour:</b> The PGA Tour is the primary professional golf circuit in the United States, "
    f"featuring the world’s top male golfers. It organises most of the major golf tournaments played "
    f"throughout the year.</p>"
    f"<p><b>Golf Tournament:</b> A competitive event where professional golfers play multiple rounds "
    f"(typically four, over four days) on a specific course. Each player's performance is measured by "
    f"the number of strokes taken, with the goal of completing the course in as few strokes as possible. "
    f"Usually, around 120 players take part in a tournament, so finishing in the top ten would be considered "
    f"a good achievement for most.</p>"
    f"<p><b>The Cut:</b> After the first two rounds (36 holes) of a tournament, a score threshold known as "
    f"the cut is applied. Only players whose total strokes are at or below this threshold continue to play "
    f"the final two rounds. The rest are eliminated. The cut ensures that only the top-performing players "
    f"compete in the weekend rounds.</p>"
    f"<p><b>Strokes Gained:</b> A performance metric developed to quantify how a golfer’s performance compares "
    f"to the field average. It measures how many strokes a player gains or loses relative to the typical "
    f"performance of other players on each shot or play category.</p>"
    f"</div>",
    unsafe_allow_html=True
)



# Dataset Description
st.markdown(
    f"<div style='background-color:#e0ffff;padding:15px;border-radius:10px;margin-bottom:15px'>"
    f"<h2>📊 Dataset Description</h2>"
    f"<p>The dataset used in this study contains PGA Tour performance data for years 2015–2022. "
    f"It includes player-level statistics, strokes gained metrics (Driving, Approach, Around-the-Green, "
    f"Putting), and finishing positions for tournaments.</p>"
    f"<p>These data allow detailed analysis of elite professional golfers and their performance "
    f"profiles over time.</p>"
    f"<p>📂 <b>Source:</b> <a href='https://www.kaggle.com/datasets/robikscube/pga-tour-golf-data-20152022' target='_blank'>"
    f"Kaggle – PGA Tour Golf Data (2015–2022)</a></p>"
    f"</div>",
    unsafe_allow_html=True
)