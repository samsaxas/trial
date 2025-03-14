import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Samriddhi Saxena - Data Scientist",
    layout="wide",
    page_icon="📊"
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .header {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #fffff;
            padding: 20px;
            background: linear-gradient(90deg, #2E86C1, #3498DB);
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
            border-bottom: 3px solid #2E86C1;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        .subsection-title {
            font-size: 28px;
            font-weight: bold;
            color: #2E86C1;
            margin-top: 20px;
        }
        .content {
            font-size: 20px;
            color: #34495E;
            margin-left: 20px;
            line-height: 1.6;
        }
        .footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            font-size: 18px;
            color: #7F8C8D;
            background: #ECF0F1;
            border-radius: 10px;
        }
        .emoji {
            font-size: 24px;
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with emoji
st.markdown('<div class="header">📊 Samriddhi Saxena - Data Scientist</div>', unsafe_allow_html=True)

# Work Experience
st.markdown('<div class="section-title">💼 Work Experience</div>', unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Data Visualization Intern - Infosys</div>', unsafe_allow_html=True)
st.markdown('<div class="content"><strong>📅 December 2024 - January 2025</strong></div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <br>
        <span class="emoji">🧹</span> Cleaned and preprocessed data, improving data quality and reducing processing time by 80% and boosting cost efficiency.<br>
        <span class="emoji">📈</span> Used PowerBI and Python Streamlit to deliver the solution.<br>
        <span class="emoji">📊</span> Created 4 dashboards, improving decisions and Streamlit UI to raise engagement by 65%.<br><br>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Machine Learning Intern - Compsoft Technologies</div>', unsafe_allow_html=True)
st.markdown('<div class="content"><strong>📅 October 2023 - December 2023</strong></div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <br>
        <span class="emoji">🤖</span> Developed a machine learning-based solution to optimize automatic parking, reducing operational costs by 80%.<br>
        <span class="emoji">🐍</span> Utilized Python libraries for data processing, ML modeling, and computer vision like Pandas, NumPy, Scikit-learn, and OpenCV.<br>
        <span class="emoji">⏱️</span> Reduced search time by 80%, saved 50+ hours weekly, and enhanced user experience via automation.<br><br><br><br>
    </div>
""", unsafe_allow_html=True)

# Projects
st.markdown('<div class="section-title">🚀 Projects</div>', unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Integrated Intelligent Traffic Management System</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🚦</span> Built a solution using ML, boosting safety and efficiency by 30%.<br>
        <span class="emoji">🛠️</span> <strong>Tech Stack:</strong> Used MongoDB, Google Cloud, and Python (Matplotlib, Pandas, NumPy) for data storage and analysis.<br>
        <span class="emoji">🎯</span> <strong>Achievements:</strong> Improved accuracy by 95%, reduced violations, and enabled data-driven decisions.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Sentiment Analysis using NLP</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🧠</span> Designed a system using NLP, achieving 90% accuracy on 10,000+ data points.<br>
        <span class="emoji">📊</span> Presented sentiment insights with Seaborn visualizations, and robust data pipelines, leveraging statistics for analysis.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Online Examination System</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">💻</span> Built a full-stack exam system with SQL, securely managing 1,000+ user accounts and boosting process efficiency by 40%.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-title">Automated Parking System using Machine Learning</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🅿</span> Optimized parking allocation with machine learning algorithms, reducing search time by 99%.<br>
        <span class="emoji">🤖</span> Automated business processes, cutting labor expenses by 80% and enhancing the user experience.<br><br><br><br>
    </div>
""", unsafe_allow_html=True)

# Education
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
st.markdown('<div class="subsection-title">B.E. in Computer Science Engineering with Data Science</div>', unsafe_allow_html=True)
st.markdown('<div class="content">🏫 Visvesvaraya Technological University (VTU)<br><br><br><br></div>', unsafe_allow_html=True)

# Co-Curriculars
st.markdown('<div class="section-title">🌟 Co-Curriculars</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">💡</span> Engaged in “Code-6-Craze”, a 6-hour Hackathon, analyzed social media sentiment for Instagram, Twitter, etc., using NLP.<br><br><br><br>
    </div>
""", unsafe_allow_html=True)

# Certifications
st.markdown('<div class="section-title">📜 Certifications</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🎖️</span> Accenture Data Analytics & Visualization Job Sim<br>
        <span class="emoji">🎖️</span> Tata Data Visualization Job Sim<br>
        <span class="emoji">🎖️</span> Quantium Data Analytics Job Sim<br>
        <span class="emoji">🎖️</span> Data Analyst Training<br>
        <span class="emoji">🎖️</span> Data Warehousing<br>
        <span class="emoji">🎖️</span> Power BI<br>
        <span class="emoji">🎖️</span> Data Analysis with Python<br>
        <span class="emoji">🎖️</span> Data Science<br>
        <span class="emoji">🎖️</span> Machine Learning with Python<br><br><br><br>
    </div>
""", unsafe_allow_html=True)

# Skills
st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🐍</span> <strong>Programming Languages:</strong> Python, SQL, MongoDB (NoSQL), R Programming, Java<br>
        <span class="emoji">📊</span> <strong>Technical Skills:</strong> Data Analysis, Machine Learning, NLP, Data Visualization, Big Data Analysis<br>
        <span class="emoji">🛠️</span> <strong>Tools & Others:</strong> Power BI, Tableau, Flask, Streamlit, DSA, Git/GitHub, Jupyter Notebook, VS Code<br><br><br><br>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 Samriddhi Saxena</div>', unsafe_allow_html=True)
