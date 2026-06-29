import streamlit as st


st.set_page_config(page_title="Resume Ranker AI", page_icon="🤖",layout="wide")

# STYLING WITH SOME CSS
st.markdown("""
<style>

/* =========================================
   GLOBAL THEME
========================================= */

.stApp{
    background-color:#0F172A;
    color:#F8FAFC;
    font-family:"Segoe UI",sans-serif;
}

/* =========================================
   HIDE STREAMLIT DEFAULT UI
========================================= */

#MainMenu,
footer,
header{
    visibility:hidden;
}

/* =========================================
   HEADINGS
========================================= */

h1,h2,h3,h4,h5,h6{
    color:#F8FAFC;
    font-weight:700;
    letter-spacing:0.3px;
}

p,label{
    color:#CBD5E1;
}

/* =========================================
   BUTTONS
========================================= */

.stButton>button{

    width:100%;
    background:#3B82F6;
    color:white;

    border:none;
    border-radius:12px;

    padding:12px;

    font-size:16px;
    font-weight:600;

    transition:0.25s;
}

.stButton>button:hover{

    background:#2563EB;

    transform:translateY(-2px);

    box-shadow:0 6px 18px rgba(59,130,246,.30);

}

.stButton>button:active{

    transform:scale(.98);

}

/* =========================================
   METRIC CARDS
========================================= */

[data-testid="stMetric"]{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:14px;

    padding:18px;

    transition:.25s;

}

[data-testid="stMetric"]:hover{

    border-color:#3B82F6;

    transform:translateY(-2px);

}

/* =========================================
   INFO / SUCCESS / WARNING
========================================= */

.stInfo,
.stSuccess,
.stWarning,
.stError{

    border-radius:12px;

}

/* =========================================
   INPUT BOX
========================================= */

.stTextInput input{

    background:#1E293B;

    color:white;

    border:1px solid #334155;

    border-radius:12px;

}

.stTextInput input:focus{

    border:1px solid #3B82F6;

}

/* =========================================
   SELECTBOX
========================================= */

.stSelectbox div[data-baseweb="select"]{

    background:#1E293B;

    border-radius:12px;

}

/* =========================================
   TEXT AREA
========================================= */

.stTextArea textarea{

    background:#1E293B;

    color:white;

    border-radius:12px;

    border:1px solid #334155;

}

/* =========================================
   FILE UPLOADER
========================================= */

[data-testid="stFileUploader"]{

    background:#1E293B;

    border:2px dashed #334155;

    border-radius:14px;

    padding:15px;

}

/* =========================================
   DATAFRAME
========================================= */

[data-testid="stDataFrame"]{

    border-radius:14px;

    overflow:hidden;

    border:1px solid #334155;

}

/* =========================================
   PROGRESS BAR
========================================= */

.stProgress > div > div > div{

    background:#3B82F6;

}

/* =========================================
   HORIZONTAL LINE
========================================= */

hr{

    border:none;

    border-top:1px solid #334155;

}

/* =========================================
   SCROLLBAR
========================================= */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-track{

    background:#0F172A;

}

::-webkit-scrollbar-thumb{

    background:#475569;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#64748B;

}

/* =========================================
   SIDEBAR (IF USED)
========================================= */

section[data-testid="stSidebar"]{

    background:#111827;

    border-right:1px solid #334155;

}

/* =========================================
   LINKS
========================================= */

a{

    color:#60A5FA;

    text-decoration:none;

}

a:hover{

    color:#93C5FD;

}

</style>
""", unsafe_allow_html=True)

# HEADER
st.title("🤖 AI RESUME RANKER SYSTEM")
st.subheader("AI Powered Resume Intelligence Platform")

st.write(
    """
Welcome to **_Resume Ranker AI System_**, an intelligent resume screening system that uses Artificial Intelligence to identify the most suitable candidates.This project combines **Semantic Search**, **Skill Intelligence**,
**Experience Evaluation**, and **Explainable AI** to rank candidates
efficiently.
"""
)

st.divider()

# FEATURES
st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.info("🧠 Semantic Resume Matching")
    st.info("⚡ Fast Precomputed Embedding Search")

with col2:
    st.info("💡 Explainable AI Reasoning")
    st.info("📊 Intelligent Candidate Ranking")

st.divider()


# PROJECT STATISTICS

st.header("📈 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label="Candidates",value="100,000")

with c2:
    st.metric(label="Top Results",value="100")

with c3:
    st.metric(label="Embedding Model",value="all-MiniLM-L6-v2")

with c4:
    st.metric(label="Similarity",value="Cosine")

st.divider()

# AI PIPELINE
st.header("⚙ AI Pipeline")

st.write("1️⃣ Load Candidate Dataset")

st.write("2️⃣ Load Candidate Embeddings")

st.write("3️⃣ Read Job Description")

st.write("4️⃣ Generate Job Description Embedding")

st.write("5️⃣ Calculate Semantic Similarity")

st.write("6️⃣ Apply Skill, Experience & Recruiter Scoring")

st.write("7️⃣ Generate Explainable Ranking")

st.write("8️⃣ Display Top 100 Candidates")

st.divider()

# TECHNOLOGIES used
st.header("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("Python")
    st.success("Sentence Transformers")

with tech2:
    st.success("python-docx")
    st.success("Scikit-Learn")

with tech3:
    st.success("NumPy")
    st.success("Pandas")

with tech4:
    st.success("Streamlit")
st.divider()

# START BUTTON
st.write("")
st.write("")

left, center, right = st.columns([1,2,1])

with center:

    start = st.button("🚀 Start Analysis",use_container_width=True)

if start:
    st.switch_page("pages/processing.py")

st.write("")
st.write("")

# FOOTER
st.caption(
    "Resume Ranker AI • Intelligent Resume Ranking using Semantic AI • Created By - Keshav Awasthi"
)
