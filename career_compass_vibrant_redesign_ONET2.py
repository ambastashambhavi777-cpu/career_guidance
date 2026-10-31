
import streamlit as st
import pandas as pd
import re
from pathlib import Path

# --------------------------------------------------
# O*NET DATASET CONNECTION
# --------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent / "data"

@st.cache_data(show_spinner=False)
def load_onet_csv(filename):
    """Load an O*NET CSV safely; return an empty frame if it is unavailable."""
    file_path = DATA_DIR / filename
    if not file_path.exists():
        return pd.DataFrame()
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return pd.read_csv(file_path, encoding=encoding, low_memory=False)
        except UnicodeDecodeError:
            continue
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()

ONET_OCCUPATIONS = load_onet_csv("occupation_data.csv")
ONET_ESSENTIAL_SKILLS = load_onet_csv("essential_skills.csv")
ONET_SOFTWARE_SKILLS = load_onet_csv("software_skills.csv")

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Career Compass | AI Guidance",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #eff8ff, #f0fdfa, #fff7f5);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #dff3ff, #d5f5f0);
    border-right: 2px solid #bde5f5;
}

[data-testid="stSidebar"] * {
    color: #164e63 !important;
}

.hero {
    background: linear-gradient(120deg, #0284c7, #0d9488, #38bdf8);
    padding: 42px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(2,132,199,0.18);
}

.hero h1 {
    color: white;
    font-size: 38px;
    font-weight: 800;
}

.hero p {
    color: #f0fdfa;
    font-size: 16px;
}

.section-title {
    color: #075985;
    font-size: 27px;
    font-weight: 800;
    margin-top: 20px;
}

.info-card {
    background: white;
    padding: 23px;
    border-radius: 18px;
    border: 1px solid #bae6fd;
    box-shadow: 0 5px 18px rgba(2,132,199,0.09);
    margin-bottom: 14px;
    min-height: 130px;
}

.info-card h3 {
    color: #0284c7;
    font-size: 19px;
}

.info-card p {
    color: #475569;
    font-size: 14px;
}

.career-card {
    background: white;
    padding: 22px;
    border-radius: 17px;
    border-left: 6px solid #14b8a6;
    box-shadow: 0 5px 18px rgba(2,132,199,0.08);
    margin-bottom: 15px;
}

.career-card h3 {
    color: #075985;
}

.small-note {
    color: #64748b;
    font-size: 13px;
}

.stButton > button {
    background: linear-gradient(90deg, #0284c7, #0d9488);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 22px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0369a1, #0f766e);
    color: white;
    border: none;
}

h1, h2, h3 {
    color: #075985;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #bae6fd;
    padding: 15px;
    border-radius: 15px;
}


/* Student assessment visual design */
.assessment-hero {
    display:flex; align-items:center; justify-content:space-between;
    gap:20px; padding:30px 34px; border-radius:26px; margin:4px 0 24px;
    background:linear-gradient(115deg,#dff3ff 0%,#e4fbf7 58%,#fff0e8 100%);
    border:1px solid #c6e8f5; overflow:hidden; min-height:205px;
}
.assessment-hero-copy { flex:1; min-width:0; }
.assessment-hero .eyebrow { color:#0e7490; font-size:11px; font-weight:800; letter-spacing:2px; }
.assessment-hero h1 { color:#073b68 !important; font-size:clamp(28px,3vw,42px); margin:8px 0; font-weight:800; }
.assessment-hero p { color:#36566f; font-size:15px; max-width:620px; }
.hero-pills { display:flex; flex-wrap:wrap; gap:8px; margin-top:16px; }
.hero-pills span { background:rgba(255,255,255,.75); color:#075985; border:1px solid #c5e8f5; border-radius:30px; padding:7px 12px; font-size:11px; font-weight:600; }
.assessment-art { width:290px; height:150px; flex:0 0 290px; position:relative; border-radius:22px; background:radial-gradient(circle at 50% 50%,rgba(255,255,255,.9),rgba(255,255,255,.12) 68%); }
.assessment-art div { position:absolute; filter:drop-shadow(0 5px 5px rgba(30,90,120,.12)); }
.art-sun { width:65px;height:65px;border-radius:50%;background:#ffe29a;right:95px;top:12px; }
.art-globe { font-size:55px; left:18px; bottom:14px; }
.art-books { font-size:48px; left:90px; bottom:8px; }
.art-cap { font-size:66px; right:38px; top:20px; transform:rotate(-8deg); }
.art-target { font-size:43px; right:2px; bottom:12px; }
.art-rocket { font-size:37px; left:125px; top:3px; transform:rotate(15deg); }
.art-note { right:0; top:0; color:#0e7490; font-size:10px; font-weight:800; letter-spacing:1px; text-align:center; transform:rotate(8deg); }
.assessment-progress-title { display:flex; justify-content:space-between; gap:12px; color:#075985; font-weight:800; font-size:13px; margin:10px 0 12px; }
.progress-subtitle { color:#64748b; font-size:12px; font-weight:500; }
.step-card { text-align:center; padding:12px 5px; border-radius:15px; margin-bottom:8px; border:1px solid #d5eaf5; background:#fff; }
.step-active { background:linear-gradient(135deg,#d7f5f5,#dceeff); border:1px solid #72d5d2; box-shadow:0 4px 12px rgba(14,165,166,.10); }
.step-upcoming { background:#f8fbfe; }
.step-number { font-size:23px; }
.step-label { color:#245574; font-size:11px; font-weight:700; }
.assessment-panel { background:rgba(255,255,255,.92); border:1px solid #d6edf7; border-radius:23px; padding:24px; box-shadow:0 8px 24px rgba(14,116,144,.07); }
.student-type-hint { display:flex; align-items:center; gap:13px; border-radius:15px; padding:13px 16px; margin:12px 0 20px; }
.school-hint { background:#e6f4ff; border:1px solid #b9e2fb; }
.college-hint { background:#e3faf4; border:1px solid #b6eee0; }
.hint-icon { font-size:30px; }
.student-type-hint b { color:#075985; }
.student-type-hint small { color:#45647b; }
.form-section-heading { color:#075985; font-size:18px; font-weight:800; margin-top:20px; padding-top:8px; }
.assessment-tip { display:flex; gap:12px; background:#fff7e9; border:1px solid #ffe0a8; border-left:5px solid #f59e0b; padding:14px; border-radius:14px; color:#854d0e; font-size:13px; margin:18px 0; }
.assessment-tip span { font-size:25px; }
.why-card,.quote-card,.privacy-card { background:white; border:1px solid #dceef6; border-radius:20px; padding:20px; margin-bottom:16px; box-shadow:0 5px 18px rgba(14,116,144,.06); }
.why-card { background:linear-gradient(150deg,#fffaf0,#fff4e5); border-color:#f9e5c6; }
.why-title { color:#075985; font-size:19px; font-weight:800; margin-bottom:18px; }
.why-item { display:flex; align-items:flex-start; gap:11px; margin:14px 0; }
.why-item span { font-size:25px; }
.why-item p { color:#31546d; margin:0; font-size:13px; }
.why-item small { color:#64748b; }
.quote-card { background:linear-gradient(145deg,#e7f5ff,#e3faf7); text-align:center; }
.quote-mark { color:#38bdf8; font-size:48px; line-height:1; font-weight:800; }
.quote-card p { color:#075985; font-size:18px; font-weight:700; font-style:italic; }
.quote-decor { font-size:25px; margin-top:8px; }
.privacy-card { background:#f8fcff; color:#075985; font-size:13px; }
.privacy-card p { color:#64748b; margin:7px 0 0; }
[data-testid="stForm"] { border:0; padding:0; }
[data-testid="stFormSubmitButton"] button { background:linear-gradient(90deg,#14b8a6,#2585e8) !important; color:white !important; border:0 !important; border-radius:13px !important; min-height:48px; font-weight:700; }
[data-testid="stMultiSelect"] [data-baseweb="tag"] { background:#d9f3f2 !important; color:#075985 !important; }
@media (max-width: 800px) {
  .assessment-art { display:none; }
  .assessment-hero { padding:22px; }
  .assessment-progress-title { display:block; }
}

/* Polished controls and page-wide visual consistency */
.stApp { color: #183b56; }
[data-testid="stHeader"] { background: rgba(239,248,255,.82); }
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 12px; padding: 7px 10px; margin: 3px 0;
}
[data-testid="stTextInput"] input,
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    border: 1px solid #b9ddec !important;
    border-radius: 12px !important;
    color: #164e63 !important;
    min-height: 44px;
}
[data-testid="stTextInput"] input:focus {
    border-color: #0d9488 !important;
    box-shadow: 0 0 0 2px rgba(13,148,136,.13) !important;
}
[data-testid="stRadio"] [role="radiogroup"] { gap: 12px; }
[data-testid="stRadio"] [role="radiogroup"] label {
    background: #f3faff; border: 1px solid #c8e5f2;
    border-radius: 14px; padding: 12px 16px;
}
[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    border-radius: 20px !important; padding: 4px 8px !important;
}
[data-testid="stForm"] {
    background: linear-gradient(145deg, #ffffff, #f6fcff);
    border: 1px solid #d5eaf5; border-radius: 22px;
    padding: 22px 24px 18px;
    box-shadow: 0 8px 24px rgba(14,116,144,.07);
}
[data-testid="stFormSubmitButton"] button {
    min-height: 52px; font-size: 15px; letter-spacing: .2px;
    box-shadow: 0 6px 16px rgba(2,132,199,.18);
}
[data-testid="stMetric"] label { color: #47718a !important; }
[data-testid="stMetric"] [data-testid="stMetricValue"] { color: #075985; }
hr { border-color: #d8eaf2; }
.stAlert { border-radius: 14px; }
@media (max-width: 800px) {
  [data-testid="stForm"] { padding: 16px; }
  .assessment-hero h1 { font-size: 28px; }
}


/* DARK MODE TEXT VISIBILITY FIX */

[data-theme="dark"] .stApp,
[data-theme="dark"] [data-testid="stAppViewContainer"] {
    background-color: #101827 !important;
    color: #f1f5f9 !important;
}

[data-theme="dark"] [data-testid="stMarkdownContainer"] p,
[data-theme="dark"] [data-testid="stMarkdownContainer"] li,
[data-theme="dark"] [data-testid="stMarkdownContainer"] label,
[data-theme="dark"] h1,
[data-theme="dark"] h2,
[data-theme="dark"] h3,
[data-theme="dark"] h4 {
    color: #f1f5f9 !important;
}

[data-theme="dark"] [data-testid="stForm"] {
    background: #1e293b !important;
    border-color: #475569 !important;
}

[data-theme="dark"] input,
[data-theme="dark"] [data-baseweb="select"] > div {
    background: #263449 !important;
    color: #ffffff !important;
    border-color: #64748b !important;
}

[data-theme="dark"] [data-testid="stSidebar"] {
    background: #172337 !important;
}

[data-theme="dark"] [data-testid="stSidebar"] * {
    color: #f1f5f9 !important;
}

/* Career Compass - Dark theme override */

:root[data-theme="dark"] .stApp,
html[data-theme="dark"] .stApp {
    background: #101827 !important;
    color: #f1f5f9 !important;
}

:root[data-theme="dark"] [data-testid="stAppViewContainer"],
html[data-theme="dark"] [data-testid="stAppViewContainer"] {
    background: #101827 !important;
}

:root[data-theme="dark"] [data-testid="stSidebar"],
html[data-theme="dark"] [data-testid="stSidebar"] {
    background: #172337 !important;
}

:root[data-theme="dark"] [data-testid="stMarkdownContainer"] p,
:root[data-theme="dark"] [data-testid="stMarkdownContainer"] h1,
:root[data-theme="dark"] [data-testid="stMarkdownContainer"] h2,
:root[data-theme="dark"] [data-testid="stMarkdownContainer"] h3,
:root[data-theme="dark"] label {
    color: #f1f5f9 !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA: INTERESTS, SUBJECTS AND SKILLS
# --------------------------------------------------

interests_list = [
    "Technology", "Business", "Design", "Science",
    "Mathematics", "Healthcare", "Sports", "Writing",
    "Art", "Music", "Research", "Teaching",
    "Environment", "Finance", "Law", "Psychology",
    "Entrepreneurship", "Social Work", "Communication",
    "Travel", "Agriculture", "Engineering"
]

school_subjects = [
    "Mathematics", "Physics", "Chemistry", "Biology",
    "English", "Hindi", "Computer Science", "Social Science",
    "History", "Geography", "Economics", "Political Science",
    "Accountancy", "Business Studies", "Physical Education",
    "Psychology", "Environmental Science", "Fine Arts"
]

college_subjects = [
    "Computer Science", "Data Structures", "DBMS",
    "Artificial Intelligence", "Machine Learning",
    "Statistics", "Mathematics", "Physics", "Chemistry",
    "Biotechnology", "Microbiology", "Psychology",
    "Economics", "Finance", "Marketing", "Management",
    "Accounting", "Law", "English Literature",
    "Graphic Design", "Mass Communication",
    "Electrical Engineering", "Mechanical Engineering",
    "Civil Engineering", "Electronics",
    "Nursing", "Pharmacy", "Political Science"
]

skills_list = [
    "Python", "Java", "C++", "C Programming",
    "HTML", "CSS", "JavaScript", "SQL",
    "Data Analysis", "Machine Learning",
    "Problem Solving", "Critical Thinking",
    "Communication", "Leadership", "Teamwork",
    "Creativity", "Time Management", "Research",
    "Public Speaking", "Writing", "Teaching",
    "Graphic Design", "Video Editing", "Photography",
    "Digital Marketing", "Microsoft Excel",
    "Accounting", "Financial Analysis",
    "Decision Making", "Project Management",
    "Networking", "Cybersecurity", "Cloud Computing",
    "Presentation Skills", "Empathy",
    "Adaptability", "Organization"
]

# --------------------------------------------------
# CAREER DATABASE
# --------------------------------------------------

career_profiles = {
    "Data Scientist": {
        "interests": ["Technology", "Mathematics", "Research"],
        "subjects": ["Computer Science", "Mathematics", "Statistics"],
        "skills": ["Python", "Data Analysis", "Problem Solving"],
        "qualification": "B.Tech, B.Sc or M.Sc in Computer Science, Statistics or Data Science",
        "description": "Analyze information and discover useful patterns to help organizations make decisions.",
        "roadmap": ["Learn Python", "Study Statistics", "Learn SQL", "Practice Data Analysis", "Build Projects"]
    },

    "AI / ML Engineer": {
        "interests": ["Technology", "Science", "Mathematics"],
        "subjects": ["Computer Science", "Mathematics", "Artificial Intelligence"],
        "skills": ["Python", "Machine Learning", "Problem Solving"],
        "qualification": "B.Tech or degree in Computer Science, AI or related field",
        "description": "Build intelligent applications and machine learning systems.",
        "roadmap": ["Learn Python", "Study Mathematics", "Learn Machine Learning", "Practice AI Projects"]
    },

    "Software Developer": {
        "interests": ["Technology", "Engineering"],
        "subjects": ["Computer Science", "Mathematics", "Data Structures"],
        "skills": ["Java", "Python", "Problem Solving", "C++"],
        "qualification": "B.Tech, BCA, MCA or related qualification",
        "description": "Design, develop, test and maintain software applications.",
        "roadmap": ["Learn Programming", "Study Data Structures", "Learn Git", "Build Applications"]
    },

    "Web Developer": {
        "interests": ["Technology", "Design", "Creativity"],
        "subjects": ["Computer Science", "English"],
        "skills": ["HTML", "CSS", "JavaScript", "Creativity"],
        "qualification": "BCA, B.Tech, B.Sc IT or relevant web development training",
        "description": "Create websites and interactive web applications.",
        "roadmap": ["Learn HTML", "Learn CSS", "Learn JavaScript", "Build Websites", "Learn Backend"]
    },

    "Cybersecurity Analyst": {
        "interests": ["Technology", "Research"],
        "subjects": ["Computer Science", "Mathematics"],
        "skills": ["Networking", "Cybersecurity", "Problem Solving"],
        "qualification": "B.Tech, BCA or related cybersecurity qualification",
        "description": "Protect computer systems, networks and information from cyber threats.",
        "roadmap": ["Learn Networking", "Study Operating Systems", "Learn Security Basics", "Practice Labs"]
    },

    "Doctor / Healthcare Professional": {
        "interests": ["Healthcare", "Science", "Social Work"],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "skills": ["Communication", "Research", "Empathy"],
        "qualification": "MBBS or another relevant healthcare qualification",
        "description": "Help people maintain their health and diagnose or treat illnesses.",
        "roadmap": ["Study Biology", "Prepare for Entrance Exams", "Complete Medical Education", "Gain Clinical Experience"]
    },

    "Business Analyst": {
        "interests": ["Business", "Mathematics", "Finance"],
        "subjects": ["Economics", "Mathematics", "Business Studies"],
        "skills": ["Data Analysis", "Communication", "Microsoft Excel"],
        "qualification": "BBA, B.Com, MBA or related qualification",
        "description": "Study business problems and recommend improvements using data.",
        "roadmap": ["Learn Excel", "Study Business", "Learn Data Analysis", "Practice Reporting"]
    },

    "Chartered Accountant": {
        "interests": ["Business", "Finance", "Mathematics"],
        "subjects": ["Accountancy", "Economics", "Mathematics"],
        "skills": ["Accounting", "Financial Analysis", "Time Management"],
        "qualification": "CA qualification through the ICAI course",
        "description": "Work with accounting, taxation, auditing and financial management.",
        "roadmap": ["Study Accountancy", "Understand Taxation", "Prepare for CA Exams", "Gain Practical Training"]
    },

    "Graphic Designer": {
        "interests": ["Design", "Art", "Creativity"],
        "subjects": ["Fine Arts", "Computer Science", "English"],
        "skills": ["Graphic Design", "Creativity", "Photography"],
        "qualification": "Degree or diploma in Graphic Design or related field",
        "description": "Create visual designs for brands, websites, products and media.",
        "roadmap": ["Study Design Basics", "Learn Design Software", "Create a Portfolio", "Practice Projects"]
    },

    "Psychologist": {
        "interests": ["Psychology", "Healthcare", "Research"],
        "subjects": ["Psychology", "Biology", "English"],
        "skills": ["Communication", "Research", "Empathy"],
        "qualification": "Relevant psychology degree and further qualifications for professional practice",
        "description": "Study human behaviour, emotions and mental processes.",
        "roadmap": ["Study Psychology", "Learn Research Methods", "Complete Higher Education", "Pursue Relevant Training"]
    },

    "Mechanical Engineer": {
        "interests": ["Engineering", "Technology", "Science"],
        "subjects": ["Physics", "Mathematics", "Chemistry", "Mechanical Engineering"],
        "skills": ["Problem Solving", "Research", "C++"],
        "qualification": "B.Tech or B.E. in Mechanical Engineering",
        "description": "Design and develop machines, mechanical systems and equipment.",
        "roadmap": ["Study Physics", "Learn Engineering Mathematics", "Study CAD", "Build Practical Projects"]
    },

    "Digital Marketing Specialist": {
        "interests": ["Business", "Communication", "Creativity"],
        "subjects": ["Marketing", "English", "Business Studies"],
        "skills": ["Digital Marketing", "Writing", "Communication", "Creativity"],
        "qualification": "BBA, Marketing degree or relevant digital marketing certification",
        "description": "Promote products and services through online platforms and digital campaigns.",
        "roadmap": ["Learn Marketing Basics", "Study SEO", "Learn Social Media Marketing", "Create Campaigns"]
    },

    "Teacher / Educator": {
        "interests": ["Teaching", "Social Work", "Communication"],
        "subjects": ["English", "Mathematics", "Biology"],
        "skills": ["Teaching", "Communication", "Public Speaking"],
        "qualification": "Relevant subject degree and required teaching qualification",
        "description": "Educate students and help them develop knowledge and skills.",
        "roadmap": ["Choose a Subject", "Complete Relevant Degree", "Pursue Teaching Qualification", "Gain Experience"]
    },

    "Environmental Scientist": {
        "interests": ["Science", "Environment", "Research"],
        "subjects": ["Biology", "Chemistry", "Environmental Science"],
        "skills": ["Research", "Data Analysis", "Critical Thinking"],
        "qualification": "B.Sc or M.Sc in Environmental Science or related field",
        "description": "Study environmental problems and help protect natural resources.",
        "roadmap": ["Study Environmental Science", "Learn Research Methods", "Conduct Field Studies", "Build Expertise"]
    }
}

# --------------------------------------------------
# O*NET CAREER MATCHING
# --------------------------------------------------
# These titles connect the app's existing career cards to occupations
# actually present in the supplied O*NET occupation_data.csv file.
ONET_CAREER_TITLES = {
    "Data Scientist": ["Data Scientists"],
    "AI / ML Engineer": ["Computer and Information Research Scientists", "Software Developers"],
    "Software Developer": ["Software Developers"],
    "Web Developer": ["Web Developers"],
    "Cybersecurity Analyst": ["Information Security Analysts"],
    "Doctor / Healthcare": ["Physicians, All Other", "Family Medicine Physicians"],
    "Business Analyst": ["Management Analysts", "Business Intelligence Analysts"],
    "Chartered Accountant": ["Accountants and Auditors"],
    "Graphic Designer": ["Graphic Designers"],
    "Psychologist": ["Clinical and Counseling Psychologists"],
    "Mechanical Engineer": ["Mechanical Engineers"],
    "Digital Marketing Specialist": ["Market Research Analysts and Marketing Specialists"],
    "Teacher / Educator": ["Secondary School Teachers, Except Special and Career/Technical Education"],
    "Environmental Scientist": ["Environmental Scientists and Specialists, Including Health"],
}


def _normalise_skill(value):
    """Normalize skill labels for forgiving, case-insensitive comparison."""
    return re.sub(r"[^a-z0-9]+", " ", str(value).casefold()).strip()


def _onet_career_insights(career, selected_skills):
    """Build display-ready O*NET skills and software insights for a career."""
    titles = ONET_CAREER_TITLES.get(career, [])
    if ONET_OCCUPATIONS.empty or not titles:
        return None
    matches = ONET_OCCUPATIONS[ONET_OCCUPATIONS["Title"].isin(titles)]
    if matches.empty:
        return None
    occupation = matches.iloc[0]
    code = str(occupation.get("O*NET-SOC Code", ""))
    result = {"title": occupation["Title"], "description": occupation.get("Description", ""),
              "skills": [], "software": [], "matched": []}

    if not ONET_ESSENTIAL_SKILLS.empty and "O*NET-SOC Code" in ONET_ESSENTIAL_SKILLS.columns:
        rows = ONET_ESSENTIAL_SKILLS[ONET_ESSENTIAL_SKILLS["O*NET-SOC Code"].astype(str) == code].copy()
        if "Scale Name" in rows.columns:
            rows = rows[rows["Scale Name"].astype(str).str.casefold() == "importance"]
        if not rows.empty and "Element Name" in rows.columns:
            if "Data Value" in rows.columns:
                rows["Data Value"] = pd.to_numeric(rows["Data Value"], errors="coerce")
                rows = rows.sort_values("Data Value", ascending=False)
            result["skills"] = rows["Element Name"].dropna().astype(str).drop_duplicates().head(8).tolist()
            normalized = {_normalise_skill(x): x for x in result["skills"]}
            for selected in selected_skills:
                key = _normalise_skill(selected)
                for label_key, label in normalized.items():
                    if key and (key == label_key or (len(key) >= 5 and (key in label_key or label_key in key))):
                        if label not in result["matched"]:
                            result["matched"].append(label)
                        break

    if not ONET_SOFTWARE_SKILLS.empty and "O*NET-SOC Code" in ONET_SOFTWARE_SKILLS.columns:
        software_rows = ONET_SOFTWARE_SKILLS[ONET_SOFTWARE_SKILLS["O*NET-SOC Code"].astype(str) == code]
        column = "Workplace Example" if "Workplace Example" in software_rows.columns else None
        if column:
            result["software"] = software_rows[column].dropna().astype(str).drop_duplicates().head(8).tolist()
    return result


def _onet_skill_data(career, selected_skills):
    """Return O*NET skill match details for a career, when available."""
    titles = ONET_CAREER_TITLES.get(career, [])
    if ONET_OCCUPATIONS.empty or not titles or "Title" not in ONET_OCCUPATIONS.columns:
        return None

    occupation = ONET_OCCUPATIONS[ONET_OCCUPATIONS["Title"].isin(titles)]
    if occupation.empty:
        return None
    occupation = occupation.iloc[0]
    code = str(occupation.get("O*NET-SOC Code", ""))

    if ONET_ESSENTIAL_SKILLS.empty or "O*NET-SOC Code" not in ONET_ESSENTIAL_SKILLS.columns:
        return {"title": occupation["Title"], "description": occupation.get("Description", ""), "matched": [], "skill_score": None}

    rows = ONET_ESSENTIAL_SKILLS[ONET_ESSENTIAL_SKILLS["O*NET-SOC Code"].astype(str) == code].copy()
    if "Scale Name" in rows.columns:
        importance = rows[rows["Scale Name"].astype(str).str.casefold() == "importance"]
        if not importance.empty:
            rows = importance
    if "Element Name" not in rows.columns or rows.empty:
        return {"title": occupation["Title"], "description": occupation.get("Description", ""), "matched": [], "skill_score": None}

    names = rows["Element Name"].dropna().astype(str).drop_duplicates().tolist()
    normalized_names = {_normalise_skill(name): name for name in names}
    selected = [_normalise_skill(skill) for skill in selected_skills if str(skill).strip()]
    matched = []
    for skill in selected:
        if not skill:
            continue
        # Exact or meaningful phrase containment avoids loose single-word matches.
        for normalized, original in normalized_names.items():
            if skill == normalized or (len(skill) >= 5 and (skill in normalized or normalized in skill)):
                if original not in matched:
                    matched.append(original)
                break

    score = len(matched) / max(min(len(names), 8), 1) if selected else 0.0
    return {
        "title": occupation["Title"],
        "description": occupation.get("Description", ""),
        "matched": matched,
        "skill_score": min(score, 1.0),
    }


# --------------------------------------------------
# RECOMMENDATION FUNCTION
# --------------------------------------------------

def get_recommendations(interests, subjects, skills):

    results = []

    for career, requirements in career_profiles.items():

        interest_match = len(
            set(interests) & set(requirements["interests"])
        )

        subject_match = len(
            set(subjects) & set(requirements["subjects"])
        )

        skill_match = len(
            set(skills) & set(requirements["skills"])
        )

        interest_score = interest_match / max(len(requirements["interests"]), 1)
        subject_score = subject_match / max(len(requirements["subjects"]), 1)
        profile_skill_score = skill_match / max(len(requirements["skills"]), 1)
        onet_data = _onet_skill_data(career, skills)
        # Keep the original profile match meaningful while incorporating
        # real O*NET essential-skill data when a mapped occupation is available.
        if onet_data and onet_data.get("skill_score") is not None:
            skill_score = (profile_skill_score * 0.60) + (onet_data["skill_score"] * 0.40)
        else:
            skill_score = profile_skill_score

        score = round(
            (interest_score * 30) +
            (subject_score * 35) +
            (skill_score * 35)
        )

        results.append({
            "career": career,
            "score": score,
            "interest_match": interest_match,
            "subject_match": subject_match,
            "skill_match": skill_match,
            "onet_title": onet_data.get("title") if onet_data else None,
            "onet_skill_matches": onet_data.get("matched", []) if onet_data else [],
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "results" not in st.session_state:
    st.session_state.results = []

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "student_type" not in st.session_state:
    st.session_state.student_type = ""

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.markdown("# 🎓 Career Compass")
st.sidebar.markdown("### Your future starts here!")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Home",
        "📝 Student Assessment",
        "🎯 Career Recommendations",
        "📚 Skills & Learning",
        "🌟 Explore Careers"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Helping school and college students "
    "discover career possibilities."
)

if not ONET_OCCUPATIONS.empty:
    st.sidebar.success(
        f"O*NET dataset connected · {len(ONET_OCCUPATIONS):,} occupations"
    )
else:
    st.sidebar.warning("O*NET data not found. Put the CSV files in the data folder.")

# ==================================================
# PAGE 1: HOME
# ==================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>Discover Your Future Career 🚀</h1>
        <p>
        Welcome to AI-Based Student Career Guidance Expert System.
        Explore your interests, identify your strengths and discover
        career possibilities that match your personality.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Explore Your Potential</div>',
                unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <h3>🎯 Personalized Guidance</h3>
            <p>Explore career options based on your interests,
            favourite subjects and skills.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <h3>📊 Skill Matching</h3>
            <p>Understand how your current skills match
            different career requirements.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">
            <h3>📚 Learning Roadmaps</h3>
            <p>Discover useful skills and learning steps
            for your future career.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Who Can Use This System?</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="info-card">
            <h3>🏫 School Students</h3>
            <p>Students from classes 6 to 12 can explore
            career possibilities based on their interests,
            favourite subjects and abilities.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <h3>🎓 College Students</h3>
            <p>Undergraduate and postgraduate students can
            explore professional career paths and identify
            skills they may need to develop.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">How It Works</div>',
                unsafe_allow_html=True)

    steps = st.columns(4)

    step_data = [
        ("01", "Enter Details", "Tell us about yourself."),
        ("02", "Select Interests", "Choose subjects and skills."),
        ("03", "Get Suggestions", "View career compatibility."),
        ("04", "Plan Learning", "Explore your skill roadmap.")
    ]

    for col, item in zip(steps, step_data):
        with col:
            st.markdown(f"""
            <div class="info-card">
                <h3>{item[0]} ✨</h3>
                <b>{item[1]}</b>
                <p>{item[2]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.caption(
        "Career Compass provides exploratory guidance. "
        "Its recommendations are not a guarantee of career success."
    )


# ==================================================
# PAGE 2: STUDENT ASSESSMENT
# ==================================================


elif page == "📝 Student Assessment":

    # Decorative assessment banner
    st.markdown("""
    <div class="assessment-hero">
        <div class="assessment-hero-copy">
            <div class="eyebrow">CAREER COMPASS  /  YOUR JOURNEY</div>
            <h1>Student Assessment</h1>
            <p>Tell us about yourself so we can suggest career paths that
            connect with your interests, favourite subjects and strengths.</p>
            <div class="hero-pills">
                <span>✦ Personalised guidance</span>
                <span>◎ Interest-based</span>
                <span>↗ Explore possibilities</span>
            </div>
        </div>
        <div class="assessment-art" aria-label="Books, globe and graduation cap">
            <div class="art-sun"></div>
            <div class="art-globe">🌍</div>
            <div class="art-books">📚</div>
            <div class="art-cap">🎓</div>
            <div class="art-target">🎯</div>
            <div class="art-rocket">🚀</div>
            <div class="art-note">DISCOVER<br>PLAN<br>GROW</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="assessment-progress-title">
        <span>YOUR CAREER DISCOVERY JOURNEY</span>
        <span class="progress-subtitle">A few details to get started</span>
    </div>
    """, unsafe_allow_html=True)

    progress_cols = st.columns(5)
    progress_steps = [
        ("01", "Profile", "👤"),
        ("02", "Interests", "💡"),
        ("03", "Subjects", "📖"),
        ("04", "Skills", "⚡"),
        ("05", "Results", "🏁")
    ]

    for index, (col, item) in enumerate(zip(progress_cols, progress_steps)):
        number, label, symbol = item
        with col:
            active_class = "step-active" if index == 0 else "step-upcoming"
            st.markdown(f"""
            <div class="step-card {active_class}">
                <div class="step-number">{symbol}</div>
                <div class="step-label">{number} · {label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.progress(0.20)

    left, right = st.columns([2.5, 1], gap="large")

    with left:
        st.markdown("### 1. First, tell us where you are in your studies")
        st.caption("Choose the option that best describes you.")

        student_type = st.radio(
            "Student category",
            ["School Student", "College Student"],
            horizontal=True,
            label_visibility="collapsed"
        )

        if student_type == "School Student":
            st.markdown("""
            <div class="student-type-hint school-hint">
                <span class="hint-icon">🏫</span>
                <div><b>School student</b><br>
                <small>For classes 6–12 · Explore subjects, streams and future possibilities.</small></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="student-type-hint college-hint">
                <span class="hint-icon">🎓</span>
                <div><b>College student</b><br>
                <small>For diploma, undergraduate and postgraduate students · Connect your studies with careers.</small></div>
            </div>
            """, unsafe_allow_html=True)

        with st.form("student_assessment"):
            st.markdown("### 2. Basic information")
            name = st.text_input(
                "Full name",
                placeholder="e.g. Richa Poddar"
            )

            info_col1, info_col2 = st.columns(2)

            if student_type == "School Student":
                with info_col1:
                    education = st.selectbox(
                        "Current class",
                        ["Class 6", "Class 7", "Class 8", "Class 9",
                         "Class 10", "Class 11", "Class 12"]
                    )
                with info_col2:
                    stream = st.selectbox(
                        "Stream (if applicable)",
                        ["Not Selected", "Science", "Commerce",
                         "Arts / Humanities", "Other"]
                    )
                subjects_options = school_subjects
            else:
                with info_col1:
                    education = st.selectbox(
                        "Education level",
                        ["Diploma", "Undergraduate", "Postgraduate", "Other"]
                    )
                with info_col2:
                    stream = st.selectbox(
                        "Course / specialisation",
                        ["Computer Science", "Engineering", "BCA / MCA",
                         "BBA / MBA", "B.Com / M.Com", "B.Sc / M.Sc",
                         "Medical / Healthcare", "Arts / Humanities",
                         "Law", "Design", "Other"]
                    )
                subjects_options = college_subjects

            st.markdown('<div class="form-section-heading">3. What are you interested in?</div>',
                        unsafe_allow_html=True)
            st.caption("Select all the areas you enjoy or would like to explore.")
            interests = st.multiselect(
                "Your interests",
                interests_list,
                placeholder="Choose your interests...",
                help="You can select more than one."
            )

            st.markdown('<div class="form-section-heading">4. Which subjects do you enjoy?</div>',
                        unsafe_allow_html=True)
            st.caption("Choose subjects you study, enjoy or want to learn more about.")
            subjects = st.multiselect(
                "Your favourite subjects",
                subjects_options,
                placeholder="Choose your subjects..."
            )

            st.markdown('<div class="form-section-heading">5. What are your strengths?</div>',
                        unsafe_allow_html=True)
            st.caption("Select skills you already have or are currently developing.")
            skills = st.multiselect(
                "Your skills",
                skills_list,
                placeholder="Choose your skills...",
                help="You do not need to be an expert in a skill to select it."
            )

            st.markdown("""
            <div class="assessment-tip">
                <span>💡</span>
                <div><b>A helpful reminder</b><br>
                Be honest about what you enjoy and what you can do today.
                Your answers are a starting point for exploration, not a test.</div>
            </div>
            """, unsafe_allow_html=True)

            submitted = st.form_submit_button(
                "Generate My Career Recommendations  →",
                use_container_width=True
            )


    with right:
        st.markdown("""
        <div class="why-card">
            <div class="why-title">💡 Why this matters</div>
            <div class="why-item"><span>🎯</span><p><b>Understand your stage</b><br>
            <small>Your school class or college course helps shape relevant suggestions.</small></p></div>
            <div class="why-item"><span>🧭</span><p><b>Explore your interests</b><br>
            <small>Your preferences help identify career areas worth exploring.</small></p></div>
            <div class="why-item"><span>🌱</span><p><b>Find ways to grow</b><br>
            <small>Your skills can highlight strengths and possible learning goals.</small></p></div>
        </div>
        <div class="quote-card">
            <div class="quote-mark">“</div>
            <p>Small steps today can open up big opportunities tomorrow.</p>
            <div class="quote-decor">📚 ✨ 🚀</div>
        </div>
        <div class="privacy-card">
            <b>🔒 Your answers guide your results</b>
            <p>Recommendations are based on the information you choose to provide.</p>
        </div>
        """, unsafe_allow_html=True)

    if submitted:
        if not name.strip() or not interests or not subjects or not skills:
            st.error(
                "Please enter your name and select at least one interest, "
                "subject and skill."
            )
        else:
            st.session_state.student_name = name
            st.session_state.student_type = student_type
            st.session_state.education = education
            st.session_state.stream = stream
            st.session_state.results = get_recommendations(
                interests, subjects, skills
            )
            st.session_state.selected_interests = interests
            st.session_state.selected_subjects = subjects
            st.session_state.selected_skills = skills
            st.success(
                "Your assessment is complete! Open Career Recommendations "
                "from the sidebar to explore your matches."
            )
            st.balloons()


# ==================================================
# PAGE 3: CAREER RECOMMENDATIONS
# ==================================================

elif page == "🎯 Career Recommendations":

    st.markdown('<div class="section-title">🎯 Career Recommendations</div>',
                unsafe_allow_html=True)

    if not st.session_state.results:

        st.info(
            "Please complete the Student Assessment first "
            "to view your career recommendations."
        )

    else:

        st.success(
            f"Welcome, {st.session_state.student_name}! "
            "Here are your career suggestions."
        )

        st.write(
            f"Education level: {st.session_state.student_type}"
        )

        best = st.session_state.results[0]

        a, b, c = st.columns(3)

        with a:
            st.metric("Career Options", len(st.session_state.results))

        with b:
            st.metric("Top Career Match", best["career"])

        with c:
            st.metric("Top Compatibility", f'{best["score"]}%')

        st.divider()

        st.subheader("Your Career Match Results")

        for item in st.session_state.results:

            career = item["career"]
            score = item["score"]
            details = career_profiles[career]

            st.markdown(f"""
            <div class="career-card">
                <h3>🌟 {career}</h3>
                <p>{details["description"]}</p>
                <b>Compatibility: {score}%</b>
            </div>
            """, unsafe_allow_html=True)

            st.progress(score / 100)

            with st.expander(f"Explore {career}"):

                st.write("**Required qualification:**")
                st.write(details["qualification"])

                st.write("**Important skills:**")
                st.write(", ".join(details["skills"]))

                onet_insights = _onet_career_insights(career, st.session_state.selected_skills)
                if onet_insights:
                    st.divider()
                    st.markdown("**🌐 O*NET Career Insights**")
                    st.caption(f"Occupation matched in O*NET: {onet_insights['title']}")
                    if onet_insights["description"]:
                        st.write(onet_insights["description"])
                    if onet_insights["skills"]:
                        st.write("**Important skills from O*NET:**")
                        st.write(", ".join(onet_insights["skills"]))
                    if onet_insights["matched"]:
                        st.success("Your selected skills that match O*NET: " + ", ".join(onet_insights["matched"]))
                    else:
                        st.info("No direct match found between your selected skills and the O*NET skill labels for this occupation.")
                    if onet_insights["software"]:
                        st.write("**Related workplace software examples:**")
                        st.write(", ".join(onet_insights["software"]))
                    st.caption("Source: the O*NET CSV datasets included with Career Compass.")

                st.write("**Suggested learning roadmap:**")

                for step in details["roadmap"]:
                    st.write("✓ " + step)

        st.caption(
            "Compatibility is a rule-based matching score calculated "
            "from the selected interests, subjects and skills. "
            "It is not a validated prediction or exam score."
        )


# ==================================================
# PAGE 4: SKILLS AND LEARNING
# ==================================================

elif page == "📚 Skills & Learning":

    st.markdown('<div class="section-title">📚 Skills & Learning</div>',
                unsafe_allow_html=True)

    st.write(
        "Discover which skills you already have and what you "
        "could learn next."
    )

    if not st.session_state.results:

        st.info("Complete your assessment to view your personal skill analysis.")

    else:

        top_career = st.session_state.results[0]["career"]
        requirements = career_profiles[top_career]

        current_skills = st.session_state.selected_skills
        required_skills = requirements["skills"]

        matched_skills = [
            skill for skill in required_skills
            if skill in current_skills
        ]

        missing_skills = [
            skill for skill in required_skills
            if skill not in current_skills
        ]

        st.markdown(f"### Your leading career match: {top_career}")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("#### ✅ Skills You Already Have")

            if matched_skills:
                for skill in matched_skills:
                    st.success(skill)
            else:
                st.write("No directly matching skills selected yet.")

        with c2:
            st.markdown("#### 🌱 Skills You Could Develop")

            if missing_skills:
                for skill in missing_skills:
                    st.warning(skill)
            else:
                st.success("You selected all the listed skills!")

        st.divider()

        st.subheader("Your Suggested Learning Roadmap")

        for i, step in enumerate(requirements["roadmap"], 1):

            st.markdown(f"""
            <div class="info-card">
                <h3>Step {i}</h3>
                <p>{step}</p>
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "These learning steps are suggestions, not mandatory "
            "qualification requirements."
        )


# ==================================================
# PAGE 5: EXPLORE CAREERS
# ==================================================

elif page == "🌟 Explore Careers":

    st.markdown('<div class="section-title">🌟 Explore Career Options</div>',
                unsafe_allow_html=True)

    st.write(
        "Explore different professional fields and learn "
        "about their work and qualifications."
    )

    career_choice = st.selectbox(
        "Choose a career to explore",
        list(career_profiles.keys())
    )

    details = career_profiles[career_choice]

    st.markdown(f"""
    <div class="hero">
        <h1>🚀 {career_choice}</h1>
        <p>{details["description"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎓 Educational Qualifications")

    st.info(details["qualification"])

    st.subheader("⚡ Important Skills")

    cols = st.columns(3)

    for i, skill in enumerate(details["skills"]):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="info-card">
                <h3>✨ {skill}</h3>
                <p>Useful skill for this career path.</p>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("📚 Suggested Learning Roadmap")

    for i, step in enumerate(details["roadmap"], 1):
        st.write(f"**{i}.** {step}")

    st.divider()

    st.subheader("💡 Career Exploration Tip")

    st.write(
        "Research the education requirements, daily responsibilities, "
        "work environment and future opportunities before choosing "
        "a career. Discuss your plans with teachers, parents "
        "or career professionals."
    )

    # O*NET-backed occupation explorer
    st.divider()
    st.subheader("🌐 Explore real occupations from the O*NET dataset")
    if ONET_OCCUPATIONS.empty:
        st.warning(
            "O*NET occupation data could not be loaded. Check that "
            "data/occupation_data.csv exists beside this Python file."
        )
    else:
        search_text = st.text_input(
            "Search O*NET occupations",
            placeholder="Try: software developer, teacher, accountant..."
        )
        occupation_view = ONET_OCCUPATIONS.copy()
        required_cols = {"Title", "O*NET-SOC Code", "Description"}
        if required_cols.issubset(occupation_view.columns):
            if search_text.strip():
                mask = (
                    occupation_view["Title"].fillna("").str.contains(search_text, case=False, regex=False)
                    | occupation_view["Description"].fillna("").str.contains(search_text, case=False, regex=False)
                )
                occupation_view = occupation_view[mask]
            st.caption(f"Showing {min(len(occupation_view), 100):,} of {len(occupation_view):,} matching occupations")
            if occupation_view.empty:
                st.info("No matching occupation found. Try a broader search term.")
            else:
                options = occupation_view.head(100)
                chosen_code = st.selectbox(
                    "Choose an occupation",
                    options["O*NET-SOC Code"].astype(str).tolist(),
                    format_func=lambda code: options.loc[options["O*NET-SOC Code"].astype(str) == code, "Title"].iloc[0]
                )
                chosen_row = options[options["O*NET-SOC Code"].astype(str) == chosen_code].iloc[0]
                st.markdown(f"### {chosen_row['Title']}")
                st.write(chosen_row["Description"])

                if not ONET_ESSENTIAL_SKILLS.empty and "O*NET-SOC Code" in ONET_ESSENTIAL_SKILLS.columns:
                    skill_rows = ONET_ESSENTIAL_SKILLS[
                        ONET_ESSENTIAL_SKILLS["O*NET-SOC Code"].astype(str) == chosen_code
                    ].copy()
                    if not skill_rows.empty and {"Element Name", "Scale Name", "Data Value"}.issubset(skill_rows.columns):
                        importance = skill_rows[skill_rows["Scale Name"].astype(str).str.casefold() == "importance"]
                        importance = importance.sort_values("Data Value", ascending=False)
                        st.markdown("**Important skills listed by O*NET**")
                        for _, skill_row in importance.head(8).iterrows():
                            st.write(f"• {skill_row['Element Name']} — importance {skill_row['Data Value']}")

                if not ONET_SOFTWARE_SKILLS.empty and "O*NET-SOC Code" in ONET_SOFTWARE_SKILLS.columns:
                    software_rows = ONET_SOFTWARE_SKILLS[
                        ONET_SOFTWARE_SKILLS["O*NET-SOC Code"].astype(str) == chosen_code
                    ]
                    if not software_rows.empty and "Example" in software_rows.columns:
                        software_col = "Example"
                    elif not software_rows.empty and "Workplace Example" in software_rows.columns:
                        software_col = "Workplace Example"
                    else:
                        software_col = None
                    if software_col:
                        st.markdown("**Workplace software examples**")
                        st.write(", ".join(software_rows[software_col].dropna().astype(str).drop_duplicates().head(10)))
        else:
            st.error("The occupation CSV headers do not match the expected O*NET format.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown("""
<div style="text-align:center; padding:20px;">
    <h3 style="color:#075985;">🎓 Career Compass</h3>
    <p style="color:#64748b;">
        AI-Based Student Career Guidance Expert System
    </p>
    <p style="color:#64748b; font-size:12px;">
        Explore your interests. Discover your strengths.
        Plan your future.
    </p>
</div>
""", unsafe_allow_html=True)
