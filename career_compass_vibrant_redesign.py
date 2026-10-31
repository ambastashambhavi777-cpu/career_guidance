
import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Career Compass | AI Guidance",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# O*NET DATASET CONNECTION

DATA_DIR = Path(__file__).parent / "data"

@st.cache_data
def load_onet_data():
    occupations = pd.read_csv(DATA_DIR / "occupation_data.csv")
    skills = pd.read_csv(DATA_DIR / "essential_skills.csv")
    software = pd.read_csv(DATA_DIR / "software_skills.csv")
    return occupations, skills, software

occupations, onet_skills, software_skills = load_onet_data()
st.success("O*NET dataset loaded successfully!")

st.write("Total occupations:", len(occupations))
st.write("Total skill records:", len(onet_skills))
st.write("Total software skill records:", len(software_skills))

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

/* --------------------------------------------------
   CAREER COMPASS — VIBRANT VISUAL REFRESH
   -------------------------------------------------- */
.stApp {
    background:
      radial-gradient(circle at 8% 4%, rgba(56,189,248,.17), transparent 26%),
      radial-gradient(circle at 94% 12%, rgba(251,146,60,.14), transparent 24%),
      linear-gradient(145deg, #f5fbff 0%, #f0fdfa 52%, #fff9f2 100%) !important;
}
.block-container { padding-top: 2rem; padding-bottom: 2.5rem; max-width: 1440px; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #dff4ff 0%, #d9f7ef 55%, #fff0e5 100%) !important;
    border-right: 1px solid #c5e7ee;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 1.5rem; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    color: #075985 !important; font-size: 1.55rem; letter-spacing: -.6px;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: rgba(255,255,255,.62); border: 1px solid rgba(14,116,144,.10);
    border-radius: 14px; padding: 10px 12px; margin: 5px 0;
    transition: .2s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: white; border-color: #38bdf8;
}
.hero {
    position: relative; overflow: hidden;
    background: linear-gradient(112deg, #0879b9 0%, #079b9a 55%, #f28b61 125%) !important;
    border: 1px solid rgba(255,255,255,.35);
    border-radius: 28px !important; padding: 42px 44px !important;
    box-shadow: 0 18px 42px rgba(8,121,185,.17) !important;
}
.hero:after {
    content: "✦"; position: absolute; right: 7%; top: 5%;
    font-size: 115px; line-height: 1; color: rgba(255,255,255,.17);
    transform: rotate(12deg); pointer-events: none;
}
.hero h1 { font-size: clamp(32px, 4vw, 48px) !important; letter-spacing: -1.3px; }
.hero p { max-width: 720px; line-height: 1.7; }
.section-title {
    font-size: 27px !important; letter-spacing: -.6px;
    margin: 28px 0 16px !important; color: #075985 !important;
}
.info-card, .career-card {
    border: 1px solid #d7edf4 !important; border-radius: 21px !important;
    box-shadow: 0 9px 24px rgba(20,94,130,.08) !important;
    transition: transform .18s ease, box-shadow .18s ease;
}
.info-card:hover, .career-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(20,94,130,.13) !important;
}
.info-card { min-height: 155px; padding: 24px !important; }
.info-card h3 { color: #087eaa !important; }
.career-card {
    background: linear-gradient(110deg, #ffffff, #f4fcff) !important;
    border-left: 6px solid #13b8a6 !important;
}
.stButton > button, [data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #087fbd, #0ca99a, #f18b63) !important;
    color: #fff !important; border: 0 !important; border-radius: 14px !important;
    min-height: 46px; font-weight: 700 !important;
    box-shadow: 0 7px 18px rgba(8,127,189,.18);
}
.stButton > button:hover, [data-testid="stFormSubmitButton"] button:hover {
    filter: brightness(1.05); transform: translateY(-1px);
}
[data-testid="stMetric"] {
    background: linear-gradient(145deg,#fff,#f0fbff) !important;
    border: 1px solid #d6edf5 !important; border-radius: 18px !important;
    box-shadow: 0 7px 18px rgba(20,94,130,.06);
}
[data-testid="stExpander"] {
    background: rgba(255,255,255,.78); border: 1px solid #d7edf4;
    border-radius: 16px; overflow: hidden;
}
[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg,#0ea5a4,#38bdf8,#fb9866); }
[data-testid="stAlert"] { border-radius: 15px; }
.assessment-hero {
    background: linear-gradient(115deg,#dff5ff 0%,#dffaf2 55%,#fff0e5 100%) !important;
    border: 1px solid #c8e9ee !important;
    box-shadow: 0 12px 30px rgba(14,116,144,.08);
}
.step-card { box-shadow: 0 4px 12px rgba(14,116,144,.05); }
.step-active { background: linear-gradient(135deg,#d5f6ed,#dcefff) !important; }
.why-card, .quote-card, .privacy-card { box-shadow: 0 9px 22px rgba(14,116,144,.07); }
@media (max-width: 800px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { padding: 28px 24px !important; }
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
        skill_score = skill_match / max(len(requirements["skills"]), 1)

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
            "skill_match": skill_match
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

# ==================================================
# PAGE 1: HOME
# ==================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <div style="font-size:12px;font-weight:800;letter-spacing:2px;color:#dffaff;">
            YOUR IDEAS. YOUR STRENGTHS. YOUR NEXT CHAPTER.
        </div>
        <h1>Make your future<br>feel possible. ✨</h1>
        <p>
            Welcome to Career Compass — a space to explore what you enjoy,
            recognise the skills you are building, and discover career paths
            worth learning more about.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:9px;margin-top:20px;">
            <span style="background:rgba(255,255,255,.19);border:1px solid rgba(255,255,255,.35);padding:8px 13px;border-radius:30px;font-size:12px;">🎯 Interest-led discovery</span>
            <span style="background:rgba(255,255,255,.19);border:1px solid rgba(255,255,255,.35);padding:8px 13px;border-radius:30px;font-size:12px;">📚 School + college</span>
            <span style="background:rgba(255,255,255,.19);border:1px solid rgba(255,255,255,.35);padding:8px 13px;border-radius:30px;font-size:12px;">🌱 Skills and learning</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">A clearer way to explore what comes next</div>',
                unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown("""
        <div class="info-card" style="background:linear-gradient(145deg,#fff,#e9f7ff);border-top:5px solid #38bdf8;">
            <div style="font-size:30px;">🧭</div>
            <h3>Find your direction</h3>
            <p>Start with the subjects, interests and activities that make you curious.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="info-card" style="background:linear-gradient(145deg,#fff,#e8fbf5);border-top:5px solid #2dd4bf;">
            <div style="font-size:30px;">⚡</div>
            <h3>Spot your strengths</h3>
            <p>Connect the skills you have today with the skills different careers use.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="info-card" style="background:linear-gradient(145deg,#fff,#fff1e8);border-top:5px solid #fb9866;">
            <div style="font-size:30px;">🚀</div>
            <h3>Build your next step</h3>
            <p>Explore practical learning ideas and possible routes towards your goals.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Made for different stages of learning</div>',
                unsafe_allow_html=True)
    school_col, college_col = st.columns(2, gap="large")
    with school_col:
        st.markdown("""
        <div class="info-card" style="background:linear-gradient(135deg,#e7f5ff,#fff);border-left:6px solid #38bdf8;">
            <div style="font-size:32px;">🏫</div>
            <h3>School students · Classes 6–12</h3>
            <p>Explore subjects, interests and possible streams without feeling pressured to make every decision today.</p>
            <p><b>Explore:</b> subjects · interests · future pathways</p>
        </div>
        """, unsafe_allow_html=True)
    with college_col:
        st.markdown("""
        <div class="info-card" style="background:linear-gradient(135deg,#e5fbf3,#fff);border-left:6px solid #2dd4bf;">
            <div style="font-size:32px;">🎓</div>
            <h3>College students</h3>
            <p>Connect your course and developing skills with professional fields and possible career directions.</p>
            <p><b>Explore:</b> specialisations · skills · learning roadmaps</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Your discovery journey</div>',
                unsafe_allow_html=True)
    journey = st.columns(4, gap="small")
    journey_items = [
        ("01", "Tell us about you", "Choose your student stage.", "#e5f4ff", "#087eaa"),
        ("02", "Share your interests", "Pick areas you enjoy.", "#e4faf3", "#0f927e"),
        ("03", "Explore your matches", "Review suggested careers.", "#fff0e6", "#d97745"),
        ("04", "Plan a next step", "See skills and learning ideas.", "#fff7dc", "#b7791f")
    ]
    for col, (number, heading, description, bg, accent) in zip(journey, journey_items):
        with col:
            st.markdown(f"""
            <div style="background:{bg};border:1px solid #deebef;border-radius:18px;padding:18px;min-height:145px;">
                <div style="font-size:12px;font-weight:800;color:{accent};letter-spacing:1px;">STEP {number}</div>
                <h3 style="font-size:17px;color:#164e63;margin:10px 0 6px;">{heading}</h3>
                <p style="font-size:13px;color:#526b7a;margin:0;">{description}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:22px;padding:17px 20px;border-radius:17px;background:linear-gradient(100deg,#e9f7ff,#e7faf4);border:1px solid #cfe9ed;">
        <b style="color:#075985;">A little reminder 🌱</b>
        <span style="color:#45647b;"> You do not need to have your whole future figured out. Use these suggestions as a starting point for exploration.</span>
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
