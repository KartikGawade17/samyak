from pathlib import Path
import streamlit as st
from PIL import Image

import base64

def load_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

linkedin_base64 = load_base64("logo.png")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent
css_file = current_dir / "main.css"
resume_file = current_dir / "Samyak_Ajmera.pdf"
profile_pic = current_dir / "samyak_image.jpeg"
linkedin_icon = current_dir / "linkedin.png"   # Add linkedin.png in repo

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

    # Email Box Improved
    st.markdown(
        f"""
        <div style="padding:10px; margin-top:10px; border-radius:8px;
        background:#f2f2f2; border:1px solid #ddd;">
        <strong>Email:</strong><br>{EMAIL}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # LinkedIn Box with Icon
    st.markdown(
        f"""
        <div style="padding:10px; margin-top:10px; border-radius:8px;
        background:#eef6ff; border:1px solid #c2d7ff; display:flex; gap:10px;
        align-items:center;">
            <img src="data:image/png;base64,{linkedin_base64}" width="24">
            <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank"
                style="text-decoration:none; font-weight:600; color:#1a0dab;">
                LinkedIn Profile
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


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
st.markdown(
    """
To start my professional journey as an Article Assistant in a reputed CA firm offering learning and growth opportunities. I aim to gain hands-on experience in Statutory Audit, apply my academic knowledge to real-world business challenges, and grow into a competent Chartered Accountant with strong analytical and ethical values.
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
- Good hands-on experience in **MS Excel**  
- Basic knowledge of **MS Word**, **PowerPoint**, **Windows**  
- Understanding of **Accounting Standards**, **Income Tax Act**, **Audit Standards**, **GST Laws**  
"""
)

# --- SOFT SKILLS ---
st.subheader("🤝 Soft Skills")
st.write(
    """
- Completed **90-hour ICAI Soft Skills Orientation Course**  
- Strong communication & interpersonal skills  
- Good management and multitasking abilities  
- Practical and problem-solving mindset  
- Adaptable, team player, quick learner  
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

# Email Box
st.markdown(
    f"""
    <div style="padding:12px; border:1px solid #ddd; border-radius:10px;
    background:#f7f7f7; margin-bottom:12px;">
        <strong>Email:</strong> {EMAIL}
    </div>
    """,
    unsafe_allow_html=True,
)

# LinkedIn Box
st.markdown(
    f"""
    <div style="padding:10px; margin-top:10px; border-radius:8px;
    background:#eef6ff; border:1px solid #c2d7ff; display:flex; gap:10px;
    align-items:center;">
        <img src="data:image/png;base64,{linkedin_base64}" width="24">
        <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank"
            style="text-decoration:none; font-weight:600; color:#1a0dab;">
            LinkedIn Profile
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")
st.caption("© 2025 Samyak Ajmera | Built with Streamlit")
