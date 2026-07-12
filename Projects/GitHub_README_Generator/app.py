import streamlit as st
from chains import chain

st.set_page_config(
    page_title="GitHub README Generator",
    page_icon="📄",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.block-container{
    max-width:850px;
    margin:auto;
    padding-top:2rem;
}

h1{
    text-align:center;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:35px;
}

div.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ---------------- #

st.title("📄 GitHub README Generator")

st.markdown(
    "<p class='subtitle'>Generate professional GitHub README files using Gemini + LangChain</p>",
    unsafe_allow_html=True
)

# ---------------- Inputs ---------------- #

project_name = st.text_input(
    "Project Name",
    placeholder="AI Resume Analyzer"
)

description = st.text_area(
    "Project Description",
    height=120,
    placeholder="Describe your project..."
)

col1, col2 = st.columns(2)

with col1:
    tech_stack = st.text_input(
        "Tech Stack",
        placeholder="Python, Streamlit, LangChain"
    )

with col2:
    style = st.selectbox(
        "README Style",
        [
            "Professional",
            "Modern",
            "Minimal"
        ]
    )

features = st.text_area(
    "Features",
    height=120,
    placeholder="Authentication, Dashboard, AI Chat..."
)

installation = st.text_area(
    "Installation Steps",
    height=120,
    placeholder="pip install -r requirements.txt"
)

# ---------------- Session State ---------------- #

if "generated_readme" not in st.session_state:
    st.session_state.generated_readme = ""

# ---------------- Generate Button ---------------- #

if st.button("Get README"):

    with st.spinner("Generating README..."):

        response = chain.invoke(
            {
                "project_name": project_name,
                "description": description,
                "tech_stack": tech_stack,
                "features": features,
                "installation": installation,
            }
        )

        st.session_state.generated_readme = response

# ---------------- Output ---------------- #

if st.session_state.generated_readme:

    st.divider()

    st.header("Preview")

    st.subheader("Rendered Preview")

    st.markdown(st.session_state.generated_readme)

    st.divider()

    st.subheader("Markdown Source")

    st.code(
        st.session_state.generated_readme,
        language="markdown"
    )

    st.download_button(
        label="Download README.md",
        data=st.session_state.generated_readme,
        file_name="README.md",
        mime="text/markdown"
    )