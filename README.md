# 🔬 Nexus - AI Research Assistant

An intelligent PDF analysis tool powered by Google Gemini AI for researchers.

## ✨ Features

- 💬 **Interactive Q&A** - Ask questions about your research papers
- 📋 **Paper Summary** - Automatic structured summaries
- 🌟 **Future Scope** - AI-generated research directions
- 📑 **Citation Generator** - Auto-generate APA, IEEE, MLA citations
- 🔍 **Gap Analyzer** - Identify research gaps automatically

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google AI API Key (free at [makersuite.google.com](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/AI_Research_Assistant.git
cd AI_Research_Assistant

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run app
streamlit run app.py
```

## 📖 Usage

1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Enter API key in the sidebar
3. Upload a PDF research paper
4. Choose from 5 powerful features
5. Get instant AI-powered insights

## 🔑 Get API Key

Visit: https://makersuite.google.com/app/apikey
- Sign in with Google account
- Click "Create API Key"
- Copy and paste into app

## 📝 Project Structure

```
AI_Research_Assistant/
├── app.py                 # Main Streamlit application
├── gemini_helper.py       # Google Gemini API helper
├── pdf_reader.py          # PDF extraction utilities
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (local only)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🛠️ Tech Stack

- **Streamlit** - Web UI framework
- **Google Gemini** - AI model for analysis
- **PyPDF** - PDF text extraction
- **Python-dotenv** - Environment management

## 📝 License

MIT License - feel free to use and modify

## 🤝 Support

For issues or questions, open an issue on GitHub.

---

**Made with ❤️ for researchers**