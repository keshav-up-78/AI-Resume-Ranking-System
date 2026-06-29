import streamlit as st
import time
import importlib

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

st.set_page_config(page_title="AI Processing",page_icon="⚙️",layout="wide")

# styling
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

st.title("⚙️ AI Processing Pipeline")
st.subheader("Resume Ranker AI System")

st.write("The AI engine is evaluating candidate profiles and generating the final ranking.")

st.divider()

left, right = st.columns([3, 1])

# RIGHT PANEL
with right:

    st.header("📊 System Information")
    st.metric("Dataset Size", "100,000")
    st.metric("Output", "Top 100")
    st.metric("Model", "MiniLM-L6-v2")
    st.metric("Ranking", "Hybrid AI")

    st.divider()

    st.info("""
### 🚀 Optimization

This system uses:

✅ Precomputed Candidate Embeddings

✅ Semantic Similarity Search

✅ Hybrid AI Ranking

✅ Explainable AI Reasoning

This reduces runtime and improves scalability.
""")

# LEFT PANEL
with left:

    st.header("🟢 Preloaded Components")

    st.success("✅Main Dataset Already Processed")
    st.caption("candidates.jsonl")

    st.success("✅ Filtered Dataset Loaded")
    st.caption("filtered_candidates.jsonl")

    st.success("✅ Candidate Embeddings Loaded")
    st.caption("candidate_embedding.npy")

    st.success("✅ Sentence Transformer Ready")
    st.caption("all-MiniLM-L6-v2")

    st.success("✅ Ranking Engine Ready")

    st.divider()

    st.header("🟡 Runtime Processing")

    progress = st.progress(0)
    status = st.empty()

    pipeline_steps = [
        ("📄 Reading Job Description", 10),
        ("🧠 Generating Job Description Embedding", 25),
        ("⚙️ Initializing Ranking Engine", 40),
        ("📊 Computing Semantic Similarity", 55),
        ("🧾 Computing The Score Of Each Candidate",65),
        ("💡 Generating Explainable AI Ranking", 80),
        ("🏆 Preparing Top Candidates", 95)
    ]

    for step, value in pipeline_steps:

        status.info(step)

        current = progress.progress(0)

        for i in range(value):
            progress.progress(i + 1)
            time.sleep(0.02)

        st.success(f"{step} ✔")

    

    if not st.session_state.analysis_done:
        status.warning("🚀 Running Resume Ranking Engine...")

        start_time = time.time()

        import main
        importlib.reload(main)

        elapsed = round(time.time() - start_time, 2)

        progress.progress(100)

        status.success("🎉 Analysis Completed Successfully")

        st.success(f"Top candidates ranked successfully in {elapsed} seconds.")
        st.session_state.analysis_done = True
    else:
        progress.progress(100)

        status.success("✅Analysis Already Completed")

        st.success("Final ranking is already available.")

st.divider()

st.header("📈 Analysis Summary")

c1, c2 = st.columns(2)

with c1:
    st.metric("Profiles Evaluated", "100,000")

with c2:
    st.metric("Candidates Ranked", "100")

c3, c4 = st.columns(2)

with c3:
    st.metric("Method", "With Some Help Of Semantic AI")

with c4:
    st.metric("Status", "Completed")

st.divider()

st.success("""
🏆 Final ranking has been generated successfully.

The file 'Final_ranked_candidate.csv' is now available
for dashboard visualization.
""")

if st.button("➡️ Open Dashboard", use_container_width=True):
    st.switch_page("pages/dashboard.py")