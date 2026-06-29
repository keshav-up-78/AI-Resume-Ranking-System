
# 🤖AI Resume Ranking System

An AI-powered resume ranking system developed for Redrob AI hackathon. This system ranks the Top-100 best fit candidate according to job description from the total resumes(100000) given in dataset. In this system sentence-transformers AI model is used for semantic search. I use semantic searching , embedding , similarity , different section score for better scoring. Technologies used - Python ,Pandas,Numpy, scikit-learn, Python-docx, Sentence Transformers and Streamlit for User Interface.


## ✨ Features

- AI-powered resume ranking using Sentence Transformers
- Semantic matching between Job Description and Candidate Profiles
- Pre-embedding calculation for time management
- Hybrid scoring system combining multiple ranking factors
- Experience-based candidate evaluation
- Intelligent job title relevance scoring
- Recruiter signal analysis (Open to Work, Response Rate, Notice Period, etc.)
- Automatic Top-N candidate ranking
- Interactive Streamlit web interface
- Real-time ranking dashboard
- CSV export for ranked candidates
- Modular and scalable Python codebase
- Optimized for CPU-only execution

## 🔄 Workflow

1. Import libraries.
2. Upload the Job Description.
3. Extract job Description text.
4. Load candidate profiles from the dataset.
5. Extract candidate information.
6. Generate semantic embeddings.
7. Calculate similarity scores.
8. Apply Experience, Title, and Redrob Signal scoring.
9. Compute the final weighted score.
10. Generate the Ranking Reasoning.
11. Rank candidates.
12. Generate the final Top-100 CSV.
13. Display results through the Streamlit dashboard.
## 📂 Project Structure

- app.py
- candidate_embedding.npy
- candidate.jsonl
- filtered_candidates.jsonl
- pages/
     - processing.py
     - dashboard.py
- main.py
- job_description.docx
- Final_ranked_candidate.csv
- submission_metadata.yaml
- requirement.txt
- README.md 
## Installation

Clone the repository:

```bash
git clone https://github.com/keshav-up-78/AI-Resume-Ranking-System.git
cd AI-Resume-Ranking-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

    
## Usage

Run the streamlit application:

```bash
streamlit run app.py
```

- Then click START ANALYSIS button to start ranking engine or process.
- Then click VIEW DASHBOARD button see final analysis or output by which you can download ranked_candidate.csv file.

Or if only for run main file:

```bash
python main.py
```

**Live Demo**

Follow this link to see app: https://ai-resume-ranking-system-project.streamlit.app/

## ## ⚙️ Tech Stack

**Programming Language**
- Python 3.14

**Machine Learning**
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn (Cosine Similarity)

**Data Processing**
- Pandas
- NumPy

**Frontend**
- Streamlit
- CSS

**Document Processing**
- python-docx

**Development Tools**
- VS Code
- Git
- GitHub
## 🧠 Scoring Methodology

The ranking engine follows a hybrid scoring approach that combines semantic understanding with rule-based evaluation.

1. Semantic Similarity

The Job Description and each candidate profile are converted into vector embeddings using the all-MiniLM-L6-v2 Sentence Transformer model. Cosine similarity is then calculated to measure how closely a candidate matches the job requirements.

2. Experience Score

Candidates are evaluated based on their total years of professional experience. Profiles with experience closest to the target requirement receive higher scores.

3. Job Title Score

Current and previous job titles are analyzed to determine how relevant they are to AI, Machine Learning, Data Engineering, and Software Engineering roles.

4. Redrob Signal Score

Recruitment-related signals are considered to improve ranking quality, including:

- Open to Work status
- Recruiter response rate
- Interview completion rate
- Notice period
- Profile completeness
- Relocation preference
- LinkedIn connection

Final Score

The final candidate score is calculated using a weighted combination of all scoring components:

Final Score =

- 55% Semantic Similarity
- 15% Experience Score
- 20% skill_score
- 10% Redrob Signal Score

Candidates are ranked in descending order based on the final score, and the Top-100 candidates are exported as the final submission.
## 📤 Output

The system generates a ranked list of candidates based on their overall relevance to the provided Job Description.

Output Format

The final submission is exported as a CSV file containing the following columns:

|    Column      |   Description|

|"candidate_id"| Unique candidate identifier|

|"rank"| Candidate rank (1–100)|

|"score"| Final ranking score|

|"reasoning"| Short explanation for the assigned rank|

**Sample Output**

candidate_id| rank| score

CAND_00xxxxx| 1| 0.962

CAND_00xxxxx| 2| 0.954

CAND_00xxxxx| 3| 0.947

The candidates are sorted in descending order of their final score, ensuring that the highest-ranked candidate appears first.
## 👨‍💻 Author

**Keshav Awasthi**

🎓 B.Tech CSE (AI & ML)

💻 Passionate about AI, Machine Learning & Software Development

🔗 GitHub: https://github.com/keshav-up-78

💼 LinkedIn: https://www.linkedin.com/in/keshav-awasthi-430b34347/
## 📄 License

This project was developed as part of the **Redrob Hackathon** for educational and demonstration purposes.
