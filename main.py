from docx import Document
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")



# this function extract the text from job description ms word file
def jd_text_extraction(path):
    doc = Document(path)
    text  =""
    for para in doc.paragraphs:
        if "Final note for the participants of the Redrob hackathon" in para.text:
            break

        if para.text.strip():
            text += para.text +"\n"
    
    return text


# this is function for getting te text of profile section
def getting_profile_text(candidate):
    profile = candidate['profile']
    # name = "Name : " + profile.get("anonymized_name"," ")
    headline = "headline : " + profile.get("headline"," ")
    summary = "summary : "+ profile.get("summary"," ")
    # location = "location : "+ profile.get("location"," ")
    # country = "country : "+ profile.get("country"," ")
    yr_experience= "years of experience : "+ str(profile.get("years_of_experience"," "))
    current_title= "current_title : "+ profile.get("current_title"," ")
    # current_company ="current_company : "+ profile.get("current_company"," ")
    # company_size = "company_size : " + str(profile.get("current_company_size"," "))
    # current_industry = "current_industry : "+ profile.get("current_industry"," ")

    return  headline + "\n" + summary + "\n"  + yr_experience + "\n" + current_title 


# this is function for get the text of career history section
def getting_career_history_text(candidate):
    # cr_history_text = candidate.get("career_history"," ")
    text =""
    for job in candidate.get("career_history",[]):
        company = job.get("company","")
        title = job.get("title", "")
        # start_date = job.get("start_date","")
        # end_date = job.get("end_date", "")
        # duration_months= str(job.get("duration_months", ""))
        # is_current = str(job.get("is_current",""))
        industry = job.get("industry","")
        # company_size = job.get("company_size","")
        description = job.get("description", "")
        text += (
            f"company : {company} \n"
            f"title : {title}\n"
            # f"start date : {start_date}\n"
            # f"end date : {end_date}\n"
            # f"duration_months : {duration_months}\n"
            # f"is current : {is_current}\n"
            f"industry : {industry}\n"
            # f"company size : {company_size}\n"
            f"description : {description}\n\n"
        )
    return "Career History : \n" + text


# this is function for get the text of education section
def for_education_text(candidate):
    text = ""
    for data in candidate.get("education",[]):
        # institute = data.get("institution","")
        degree = data.get("degree","")
        field_of_study = data.get("field_of_study","")
        # start_yr = str(data.get("start_year",""))
        # end_year = str(data.get("end_year",""))
        # grade = data.get("grade","")
        # tier = data.get("tier","")
        text += (
            f"degree : {degree}\n"
            f"field of study : {field_of_study}\n"
            
        )
    return "Education : \n" + text


# this function is for getting the text of skills section 
def get_skills_text(candidate):
    text = ""
    for data in candidate.get("skills",[]):
        name = data.get("name","")
        proficiency = data.get("proficiency","")
        # endo = str(data.get("endorsements",""))
        # duration = str(data.get("duration_months",""))
        text +=(
            f"Skill name : {name}\n"
            # f"Proficiency : {proficiency}\n"
            # f"skill duration in months : {duration}\n\n"
        )
    return "Skills : \n" + text


# this is function for getting the text of certification section
def get_certification_text(candidate):
    text =""
    for data in candidate.get("certifications",[]):
        name = data.get("name","")
        # issuer = data.get("issuer","")
        # year = str(data.get("year",""))
        text+=(
            f"certificate name : {name}\n"
            # f"issuer : {issuer}\n"
            # f"year : {year}\n
            
        )
    return "Certifications : \n "+ text


# This function is used to build the final candidate text after collecting small parts of text from different function 
def build_candidates_text(candidate):
    text = ""
    text += getting_profile_text(candidate) + getting_career_history_text(candidate) + for_education_text(candidate) + get_skills_text(candidate) + get_certification_text(candidate)  
    return text
    

jd_text = jd_text_extraction("job_description.docx")

jd_embedding = model.encode(jd_text)
    

df= pd.read_json('filtered_candidates.jsonl',lines=True)

candidate_embedding = np.load("candidate_embedding.npy")


# This function is returning sementic score of candidate after the finding similarity 
def temp_score(i):
    
    score = cosine_similarity(
        [jd_embedding],
        [candidate_embedding[i]]
    )[0][0]
    return score 


# This function returns the score by experience of candidate
def get_experience_score(candidate):
    exp = (candidate["profile"]['years_of_experience'])
    score = 0
    if(exp >= 5 and exp <= 9):
        score = 1.0
    elif((exp >=4 and exp <5) or (exp > 9 and exp<=11)):
        score = 0.8
    else:
        score = 0.5

    return score


# this function returns the score by redrob signal 
def get_redrob_signal_score(candidate):
    
    redrob = candidate.get("redrob_signals",{})
    score = 0
    
    if redrob.get("open_to_work_flag"):
        score += 0.15
    
    if redrob.get("willing_to_relocate"):
        score += 0.10
    
    if redrob.get("linkedin_connected"):
        score +=0.05

    score += min(redrob.get("recruiter_response_rate",0),1)*0.20

    score += min(redrob.get("interview_completion_rate",0),1)*0.20

    notice = redrob.get("notice_period_days",90)
    if notice <= 30:
        score+=0.15
    elif notice <=60:
        score+=0.10
    
    comp = redrob.get("profile_completeness_score",0)
    score += (comp/100)*0.15

    return min(score,1.0)


# This function returns the score by skill section of candidate
def get_skill_score(candidate):

    core_ai = {
        "machine learning",
        "deep learning",
        "llms",
        "large language models",
        "nlp",
        "recommendation systems",
        "generative ai",
        "rag",
        "hugging face transformers",
        "transformers"
    }

    retrieval = {
        "faiss",
        "qdrant",
        "pinecone",
        "weaviate",
        "chroma",
        "bm25",
        "elasticsearch",
        "haystack",
        "semantic search",
        "vector search",
        "learning to rank",
        "ranking",
        "search"
    }

    production = {
        "python",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "mlops",
        "kubeflow",
        "docker",
        "fastapi",
        "flask"
    }

    skills = {
        skill.get("name", "").lower().strip()
        for skill in candidate.get("skills", [])
    }

    core_matches = skills & core_ai
    retrieval_matches = skills & retrieval
    production_matches = skills & production

    core_score = len(core_matches) / len(core_ai)
    retrieval_score = len(retrieval_matches) / len(retrieval)
    production_score = len(production_matches) / len(production)

    score = (
        0.50 * core_score +
        0.35 * retrieval_score +
        0.15 * production_score
    )

    expert_core = []
    advanced_core = []

    expert_retrieval = []
    advanced_retrieval = []

    for skill in candidate.get("skills", []):

        name = skill.get("name", "").strip()
        skill_name = name.lower()
        proficiency = skill.get("proficiency", "").lower()

        if skill_name in core_ai:

            if proficiency == "expert":
                expert_core.append(name)

            elif proficiency == "advanced":
                advanced_core.append(name)

        elif skill_name in retrieval:

            if proficiency == "expert":
                expert_retrieval.append(name)

            elif proficiency == "advanced":
                advanced_retrieval.append(name)

    return {

        # Score (same as before)
        "score": min(score, 1.0),

        # Counts
        "core_count": len(core_matches),
        "retrieval_count": len(retrieval_matches),
        "production_count": len(production_matches),

        # Reasoning
        "expert_core": expert_core,
        "advanced_core": advanced_core,
        "expert_retrieval": expert_retrieval,
        "advanced_retrieval": advanced_retrieval
    }


# This function is for generating the reasoning for candidate ranking
def generate_reasoning(candidate, skill_data):

    title = candidate["profile"].get("current_title", "Unknown")
    exp = candidate["profile"].get("years_of_experience", 0)

    parts = [
        f"{title}",
        f"{exp:.1f} yrs"
    ]

    if skill_data["expert_core"]:
        parts.append(f"Expert Core AI with {len(skill_data['expert_core'])} skills")

    if skill_data["advanced_core"]:
        parts.append(f"Advanced Core AI with {len(skill_data['advanced_core'])} skills")

    if skill_data["expert_retrieval"]:
        parts.append(f"Expert in {len(skill_data['expert_retrieval'])} retrival skillls")

    if skill_data["advanced_retrieval"]:
        parts.append(
            f"Advanced in {len(skill_data['advanced_retrieval'])} retrival skills"
        )
    if (
    not skill_data["expert_core"]
    and not skill_data["advanced_core"]
    and not skill_data["expert_retrieval"]
    and not skill_data["advanced_retrieval"]):
        parts.append("Intermediate AI/ML skill exposure")

    return "| ".join(parts)


# Final process for scoring and reasoning
scoring = []

for i in range(len(df)):
    candidate = df.iloc[i]
    skill_data = get_skill_score(candidate)
    final_score =(
    0.55* temp_score(i) +
    0.15* get_experience_score(candidate) +
    0.20 *skill_data['score'] +
    0.10* get_redrob_signal_score(candidate)
    )
    reasoning = generate_reasoning(candidate,skill_data)
    scoring.append(
        {
            "candidate id" :  candidate["candidate_id"],
            "score" : float(final_score),
            "Reasoning" : reasoning
        }
    )


scoring.sort(key=lambda x : x['score'],reverse= True)

rank_df = pd.DataFrame(scoring)

rank_df = rank_df.head(100)

rank_df.insert(0,"Rank", range(1,len(rank_df)+1)) 

# Generating the final top candidates csv file
rank_df.to_csv("Final_ranked_candidate.csv",index= False)

