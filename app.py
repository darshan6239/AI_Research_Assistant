import streamlit as st
from pdf_reader import extract_text_from_pdf
from gemini_helper import get_gemini_model
import os
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Nexus • AI Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subheader {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2rem;
        font-weight: 600;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
    }
    .feature-card {
        background: #0f172a;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #334155;
    }
    .answer-box {
        background: #f0f9ff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #6366f1;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SESSION STATE ====================
if 'api_key' not in st.session_state:
    st.session_state.api_key = os.getenv("GOOGLE_API_KEY", "")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/artificial-intelligence.png", width=80)
    st.title("🔬 Nexus")
    st.caption("AI Research Assistant")
    
    st.divider()
    
    api_key_input = st.text_input(
        "Gemini API Key", 
        type="password", 
        value=st.session_state.api_key,
        placeholder="Enter your Google AI API key"
    )
    
    if api_key_input:
        st.session_state.api_key = api_key_input
    
    if st.button("🔗 Connect to Gemini", use_container_width=True):
        if st.session_state.api_key:
            try:
                test_model = get_gemini_model(st.session_state.api_key)
                st.success("✅ Connected to Gemini!")
            except Exception as e:
                st.error(f"❌ Connection failed: {str(e)}")
        else:
            st.error("⚠️ Please enter an API key")

    st.divider()
    st.info("📌 **Get Free API Key:**\nVisit [Google AI Studio](https://makersuite.google.com/app/apikey)")
    
    st.divider()
    st.caption("**Status:** Phase 1-5 Active ✨")

# ==================== MAIN UI ====================
st.markdown('<h1 class="main-header">🔬 Nexus Research</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Intelligent PDF Analysis • Research Intelligence • Smart Insights</p>', unsafe_allow_html=True)

# ==================== PDF UPLOAD ====================
col1, col2 = st.columns([3, 1])
with col1:
    uploaded_file = st.file_uploader(
        "📄 Upload Research Paper (PDF)", 
        type="pdf",
        help="Upload any academic paper or research document"
    )

pdf_text = None
file_info = ""

if uploaded_file:
    try:
        with st.spinner("⏳ Extracting content from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file.getvalue())
            char_count = len(pdf_text)
            word_count = len(pdf_text.split())
            file_info = f"**{uploaded_file.name}** • {char_count:,} characters • {word_count:,} words"
        
        st.success(f"✅ Paper loaded successfully\n\n{file_info}", icon="📄")
    except Exception as e:
        st.error(f"❌ Error reading PDF: {str(e)}")
        pdf_text = None

# ==================== FEATURE TABS ====================
if pdf_text:
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "💬 Q&A",
        "📋 Summary",
        "🌟 Future Scope",
        "📑 Citations",
        "🔍 Gap Analysis"
    ])

    # ============ TAB 1: INTERACTIVE Q&A ============
    with tab1:
        st.subheader("💬 Ask Questions About Your Paper")
        
        question = st.text_area(
            "Type your question:",
            placeholder="e.g., What is the main limitation of this approach?",
            height=100
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            generate_answer = st.button("🚀 Get Answer", type="primary", use_container_width=True)
        
        if generate_answer and question:
            if not st.session_state.api_key:
                st.error("⚠️ Please enter API key in sidebar")
            else:
                try:
                    with st.spinner("🔍 Analyzing with Gemini..."):
                        model = get_gemini_model(st.session_state.api_key)
                        prompt = f"""You are an expert research analyst. Answer the following question based ONLY on the provided paper content. Be precise, academic, and cite specific parts if relevant.

PAPER CONTENT:
{pdf_text[:30000]}

QUESTION: {question}

Provide a comprehensive, well-structured answer."""
                        
                        response = model.generate_content(prompt)
                        
                        st.markdown("### 📖 Answer")
                        st.markdown(f'<div class="answer-box">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    # ============ TAB 2: PAPER SUMMARY ============
    with tab2:
        st.subheader("📋 Structured Research Summary")
        
        if st.button("📝 Generate Complete Summary", type="primary", use_container_width=True):
            if not st.session_state.api_key:
                st.error("⚠️ Please enter API key in sidebar")
            else:
                try:
                    with st.spinner("🔍 Creating structured summary..."):
                        model = get_gemini_model(st.session_state.api_key)
                        prompt = f"""Analyze the following research paper and provide a professional academic summary with these exact sections:

1. **Abstract Summary** - Brief overview of the paper
2. **Key Contributions** - Main innovations/findings
3. **Methodology** - Research approach and techniques
4. **Results & Findings** - Key results and outcomes
5. **Limitations** - Known limitations and weaknesses
6. **Impact & Significance** - Why this research matters

PAPER:
{pdf_text[:35000]}

Format your response with clear headers and bullet points where appropriate."""
                        
                        response = model.generate_content(prompt)
                        st.markdown(response.text)
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    # ============ TAB 3: FUTURE SCOPE ============
    with tab3:
        st.subheader("🌟 Future Research Directions")
        
        if st.button("💡 Generate Future Scope", type="primary", use_container_width=True):
            if not st.session_state.api_key:
                st.error("⚠️ Please enter API key in sidebar")
            else:
                try:
                    with st.spinner("🚀 Generating innovative future directions..."):
                        model = get_gemini_model(st.session_state.api_key)
                        prompt = f"""Based on this research paper, suggest 7-10 high-potential, specific, and innovative future research directions. For each direction:
- State the research direction clearly
- Explain why it's important
- Suggest potential methodologies
- Indicate potential impact

PAPER:
{pdf_text[:30000]}

Make suggestions that build upon or address gaps in the current work."""
                        
                        response = model.generate_content(prompt)
                        st.markdown(response.text)
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    # ============ TAB 4: CITATION GENERATOR ============
    with tab4:
        st.subheader("📑 Citation Generator")
        
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("📖 Paper Title", placeholder="Enter paper title")
            authors = st.text_input("✍️ Authors", placeholder="Author1, Author2, Author3")
        
        with col2:
            year = st.text_input("📅 Year", value=str(datetime.now().year))
            venue = st.text_input("🏛️ Venue", placeholder="Journal/Conference name")
        
        if st.button("🔗 Generate All Citations", type="primary", use_container_width=True):
            if not st.session_state.api_key:
                st.error("⚠️ Please enter API key in sidebar")
            elif not title or not authors:
                st.error("⚠️ Please fill in Title and Authors")
            else:
                try:
                    with st.spinner("📝 Generating citations..."):
                        model = get_gemini_model(st.session_state.api_key)
                        prompt = f"""Generate proper citations in APA, IEEE, and MLA formats for:
Title: {title}
Authors: {authors}
Year: {year}
Venue: {venue}

Provide each citation format clearly labeled."""
                        
                        response = model.generate_content(prompt)
                        st.code(response.text, language="markdown")
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    # ============ TAB 5: RESEARCH GAP ANALYZER ============
    with tab5:
        st.subheader("🔍 Research Gap Analyzer")
        
        if st.button("🎯 Find Research Gaps", type="primary", use_container_width=True):
            if not st.session_state.api_key:
                st.error("⚠️ Please enter API key in sidebar")
            else:
                try:
                    with st.spinner("🔬 Analyzing gaps..."):
                        model = get_gemini_model(st.session_state.api_key)
                        prompt = f"""Identify and analyze 5-8 clear, actionable research gaps in this paper. For each gap:
1. State the gap clearly
2. Explain why it's important
3. Suggest how it could be addressed
4. Indicate potential impact if addressed

PAPER:
{pdf_text[:32000]}

Be specific and provide actionable insights."""
                        
                        response = model.generate_content(prompt)
                        st.markdown(response.text)
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

else:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.info("👆 Upload a PDF to unlock all research intelligence features", icon="📤")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📄 Features")
        st.write("✅ Interactive Q&A\n✅ Paper Summary\n✅ Future Scope")
    with col2:
        st.markdown("### 🚀 Powered By")
        st.write("✅ Google Gemini\n✅ Streamlit\n✅ PyPDF")
    with col3:
        st.markdown("### 🔧 Setup")
        st.write("✅ Free API Key\n✅ Local & Cloud\n✅ Production Ready")

st.divider()
st.caption("🚀 **Nexus AI Research Assistant** • Built for Researchers • Version 1.0")