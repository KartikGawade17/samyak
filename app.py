from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent
css_file = current_dir / "main.css"
resume_file = current_dir / "Samyak_Ajmera.pdf"
profile_pic = current_dir / "samyak_image.jpeg"  # or samyak.jpg

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Samyak Ajmera"
PAGE_ICON = "📑"
NAME = "Samyak Ajmera"
DESCRIPTION = """
Aspiring Article Assistant | CA Intermediate Candidate | Committed to learning, ethics, and professional growth.
"""
EMAIL = "samajmera1301@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/samyak-ajmera-090015270",
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- SIDEBAR ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    
    for platform, link in SOCIAL_MEDIA.items():
        st.markdown(f"[{platform}]({link})")
    
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- MAIN CONTENT ---
st.title("📘 My Portfolio")
st.write("---")

# --- PROFILE SECTION ---
st.subheader("👤 Profile")
st.write(
    """
To start my professional journey as an Article Assistant in a reputed CA firm offering learning  
and growth opportunities. I aim to gain hands-on experience in Statutory Audit, apply academic  
knowledge to real-world business challenges, and grow into a competent Chartered Accountant  
with strong analytical and ethical values.
"""
)

# --- EDUCATION ---
st.subheader("🎓 Education")
st.write(
    """
- **ICAI — CA Intermediate** | Marks: 321/600 | 2024 – 2025  
- **ICAI — CA Foundation** | Marks: 225/400 | 2022  
- **KES’s Shroff College, Kandivali — B.Com** | Percentage: 73.83% | 2022 – 2025  
- **Shroff College — HSC (Commerce)** | 85.67% | 2022  
- **Poorna Prajna High School — SSC** | 86.40% | 2020  
"""
)

# --- TECHNICAL & IT SKILLS ---
st.subheader("💻 Technical & IT Skills")
st.write(
    """
- Completed **90 hours ITT Course** (ICAI)  
- Good hands-on experience in **MS Excel** (important formulas, spreadsheets)  
- Basic knowledge of **MS Word**, **PowerPoint**, **Windows**  
- Understanding of **Accounting Standards**, **Income Tax Act**, **Audit Standards**, **GST Laws**  
"""
)

# --- SOFT SKILLS ---
st.subheader("🤝 Soft Skills")
st.write(
    """
- Completed **90-hour ICAI Soft Skills Orientation Course**  
- Strong communication and interpersonal abilities  
- Good management and multitasking skills  
- Practical, problem-solving attitude  
- Adaptable, team player, and keen learner  
"""
)

# --- OTHER SKILLS ---
st.subheader("🧩 Other Skills")
st.write(
    """
- Basic Accounting Knowledge  
- Leadership Skills  
- Time Management  
- Effective Communication  
"""
)

# --- ACHIEVEMENTS ---
st.subheader("🏅 Achievements & Certifications")
st.write(
    """
- Scored **Exemption in Costing**  
- 32-Hour Certification in **Tally**  
- 32-Hour Certification in **Financial Statement Analysis**  
- 32-Hour Certification in **IFRS**  
- 32-Hour Certification in **Digital Finance & MIS**  
"""
)

# --- CONTACT INFO ---
st.write("---")
st.subheader("📩 Get in Touch")
st.write("Feel free to connect or collaborate!")
st.write("📧", EMAIL)
for platform, link in SOCIAL_MEDIA.items():
    st.markdown(f"[{platform}]({link})")

st.write("---")
st.caption("© 2025 Samyak Ajmera | Built with Streamlit")

