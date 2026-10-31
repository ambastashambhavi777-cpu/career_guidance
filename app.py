
import streamlit as st

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

    # Assessment header
    st.markdown("""
    <div style="
        background:linear-gradient(110deg,#dff3ff,#d9f7f0,#fff0e9);
        padding:30px;
        border-radius:22px;
        border:1px solid #c7e9f5;
    ">
        <h1 style="color:#075985;">Let's Discover Your Potential! 🚀</h1>
        <p style="color:#334155;font-size:16px;">
            Tell us about yourself, your interests and your abilities.
            Your journey towards a suitable career starts here!
        </p>
        <div style="font-size:42px;">📚 🌍 🎓 🚀 💡</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Your Career Discovery Journey")

    progress_cols = st.columns(5)

    progress_steps = [
        ("01", "Profile"),
        ("02", "Interests"),
        ("03", "Subjects"),
        ("04", "Skills"),
        ("05", "Results")
    ]

    for col, (number, label) in zip(progress_cols, progress_steps):
        with col:
            st.markdown(f"""
            <div style="
                background:#e0f2fe;
                border:1px solid #bae6fd;
                padding:12px 4px;
                border-radius:13px;
                text-align:center;
            ">
                <h3 style="color:#0284c7;margin:0;">{number}</h3>
                <small style="color:#164e63;">{label}</small>
            </div>
            """, unsafe_allow_html=True)

    st.progress(0.20)
    st.caption("Step 1 of 5 — Student Profile")

    st.markdown("## 👤 Tell Us About Yourself")

    student_type = st.radio(
        "Who are you?",
        ["School Student", "College Student"],
        horizontal=True
    )

    if student_type == "School Student":
        st.info("🏫 Let's explore your school subjects and future possibilities.")

    else:
        st.info("🎓 Let's connect your college education with future career paths.")

    with st.form("student_assessment"):

        st.markdown("### 📝 Personal Information")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        if student_type == "School Student":

            education = st.selectbox(
                "Which class are you studying in?",
                [
                    "Class 6", "Class 7", "Class 8",
                    "Class 9", "Class 10", "Class 11", "Class 12"
                ]
            )

            stream = st.selectbox(
                "Choose your stream (if applicable)",
                [
                    "Not Selected", "Science", "Commerce",
                    "Arts / Humanities", "Other"
                ]
            )

            subjects_options = school_subjects

        else:

            education = st.selectbox(
                "Select your education level",
                [
                    "Diploma", "Undergraduate",
                    "Postgraduate", "Other"
                ]
            )

            stream = st.selectbox(
                "Select your course / specialization",
                [
                    "Computer Science", "Engineering",
                    "BCA / MCA", "BBA / MBA",
                    "B.Com / M.Com", "B.Sc / M.Sc",
                    "Medical / Healthcare", "Arts / Humanities",
                    "Law", "Design", "Other"
                ]
            )

            subjects_options = college_subjects

        st.divider()

        st.markdown("### 💡 Discover Your Interests")
        st.caption("Choose the fields you enjoy exploring.")

        interests = st.multiselect(
            "Your interests",
            interests_list,
            help="You can select multiple interests."
        )

        st.divider()

        st.markdown("### 📖 Your Favourite Subjects")
        st.caption("Select the subjects you enjoy studying.")

        subjects = st.multiselect(
            "Your subjects",
            subjects_options
        )

        st.divider()

        st.markdown("### ⚡ Your Skills & Strengths")
        st.caption("Select the skills you already have or are developing.")

        skills = st.multiselect(
            "Your skills",
            skills_list,
            help="Choose all skills that describe you."
        )

        st.markdown("""
        <div style="
            background:#fff7ed;
            padding:15px;
            border-radius:13px;
            border-left:5px solid #fb923c;
        ">
            <b style="color:#9a3412;">💡 Helpful Tip</b>
            <p style="color:#7c2d12;margin-bottom:0;">
                Be honest about your interests and current skills.
                You don't need to be an expert. This assessment
                helps you explore possibilities and learning goals.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        submitted = st.form_submit_button(
            "🚀 Generate My Career Recommendations",
            use_container_width=True
        )

    if submitted:

        if not name.strip() or not interests or not subjects or not skills:

            st.error(
                "Please enter your name and select at least one "
                "interest, subject and skill."
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
                "Your assessment has been completed successfully! "
                "Open Career Recommendations from the sidebar."
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
    <h3 style="color:#6d28d9;">🎓 Career Compass</h3>
    <p style="color:#64748b;">
        AI-Based Student Career Guidance Expert System
    </p>
    <p style="color:#64748b; font-size:12px;">
        Explore your interests. Discover your strengths.
        Plan your future.
    </p>
</div>
""", unsafe_allow_html=True)
