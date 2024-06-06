from pathlib import Path
import time
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-jetelova-CZ.pdf"
profile_pic = current_dir / "assets" / "profile-picture.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Markéta Jetelová"
PAGE_ICON = ":wave:"
NAME = "Markéta Jetelová"
DESCRIPTION = """
Junior Data Analyst, currently studying at Czechitas, with a background in online advertising.
"""
EMAIL = "jetelovamarketa@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "http://www.linkedin.com/in/marketajetelova/",
}
PROJECTS = {
    "🏆 Analýza cukráren pro lidi s dietními omezeními": "https://medium.com/@jetelovamarketa/anal%C3%BDza-cukr%C3%A1ren-pro-lidi-s-dietn%C3%ADmi-omezen%C3%ADmi-3327c0dc46d0",
}
SECTIONS = {
    "Experience": "Experience",
    "Tech stack": "Tech Stack",
    "Career history": "Career History",
    "Portfolio": "Projects",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- LOAD PDF ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- PROFILE PIC ---
profile_pic = Image.open(profile_pic)

with st.sidebar:
    my_radio = st.radio("Select section", list(SECTIONS.keys()))
    awesomeness_level = st.slider("Awesomeness level", 0, 10, 0)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

if my_radio == "Experience":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write("""
    - ✔️ Currently studying Data Academy at Czechitas
    - ✔️ Background in online advertising with data analysis tasks
    - ✔️ Strong knowledge in Microsoft Excel and data visualization tools
    - ✔️ Passionate about data and eager to transition to a data analysis role
    """)

if my_radio == "Tech stack":
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Tech Stack")
    st.write("""
    - 👩‍💻 Programming: Python (Pandas), SQL, GitHub
    - 📊 Data Visualization: Tableau, Power BI, Google Looker Studio
    - 📚 Modeling: Basic statistical and machine learning models
    - 🗄️ Databases: Basic knowledge of Postgres, MongoDB, MySQL
    """)

if my_radio == "Career history":
    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Career History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Biddable Media Lead | Vodafone**")
    st.write("03/2023 – 10/2023")
    st.write("""
    - ► Led a team of online advertising specialists
    - ► Developed campaign strategies and communicated with clients
    - ► Educated and trained team members
    """)

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Paid Social Ads Specialist | Vodafone**")
    st.write("05/2019 – 02/2023")
    st.write("""
    - ► Managed and optimized social media campaigns
    - ► Conducted A/B testing and reported results
    """)

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Performance Team Leader | ACOMWARE**")
    st.write("05/2018 – 04/2019")
    st.write("""
    - ► Led a team of paid social specialists
    - ► Developed campaigns and trained team members
    """)

if my_radio == "Portfolio":
    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

# --- AWESOMENESS LEVEL ---
for i in range(awesomeness_level + 1):
    awesomeness_level = i
    with st.sidebar:
        st.write("🎉" * i)
    time.sleep(0.2)
