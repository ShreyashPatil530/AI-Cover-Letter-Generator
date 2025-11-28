# 🚀 AI Cover Letter Generator

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-API-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Generate professional, ATS-optimized cover letters in seconds using AI!**

An intelligent Streamlit web application that creates personalized cover letters from your resume and job descriptions using the powerful **Groq LLM API**. Save hours of writing time and land more interviews with AI-powered customization.

---

## 📺 Demo

https://github.com/ShreyashPatil530/AI-Cover-Letter-Generator/assets/your-user-id/SAMPLE_VIDEO.mp4

> **Note:** If the video doesn't play above, [click here to watch the demo](./SAMPLE_VIDEO.mp4)

Alternatively, view the demo GIF:

![App Demo](./demo.gif)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📄 **Smart Resume Parsing** | Upload resumes in PDF or DOCX format with automatic text extraction |
| 🎯 **Job Description Analysis** | Paste any job posting to generate tailored content |
| 🎨 **Customizable Tone** | Choose from Professional, Friendly, or Formal writing styles |
| 🤖 **AI-Powered Generation** | Leverage Groq's advanced LLM for human-like cover letters |
| 📊 **ATS Optimization** | Built-in keyword analysis to pass Applicant Tracking Systems |
| 💾 **Easy Download** | Save generated letters as text files instantly |
| ⚡ **Fast & Efficient** | Generate cover letters in under 10 seconds |

---

## 🏗️ Project Structure

```
ai_cover_letter_generator/
│
├── 📄 app.py                          # Main Streamlit application
├── 📄 resume_parser.py                # Extract text from PDF/DOCX files
├── 📄 cover_letter_generator.py       # Groq API integration for generation
├── 📄 ats_analyzer.py                 # ATS keyword matching analysis
├── 📄 requirements.txt                # Python dependencies
├── 📄 .gitignore                      # Ignore sensitive files
├── 📄 .env.example                    # Example environment variables
├── 📄 README.md                       # Project documentation
├── 📹 SAMPLE_VIDEO.mp4                # Application demo video
├── 🖼️ demo.gif                        # Demo GIF (optional)
│
├── 📁 downloads/
│   └── generated_letters/             # Storage for generated cover letters
│
└── 📁 assets/
    └── screenshots/                   # App screenshots for documentation
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShreyashPatil530/AI-Cover-Letter-Generator.git
   cd AI-Cover-Letter-Generator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Groq API key**
   
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your key:
   ```
   GROQ_API_KEY="your_groq_api_key_here"
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501`

---

## 📖 Usage Guide

### Step-by-Step Instructions

1. **Upload Your Resume**
   - Click "Browse files" or drag and drop
   - Supports PDF and DOCX formats
   - Resume text will be automatically extracted

2. **Paste Job Description**
   - Copy the job posting from any source
   - Paste into the text area
   - Include key requirements and responsibilities

3. **Select Tone**
   - **Professional**: Balanced and business-appropriate
   - **Friendly**: Warm and approachable
   - **Formal**: Traditional and conservative

4. **Generate Cover Letter**
   - Click "Generate Cover Letter"
   - Wait 5-10 seconds for AI processing
   - Review the generated content

5. **Analyze ATS Keywords** (Optional)
   - Enable "Show ATS Analysis"
   - View keyword match percentage
   - See missing important keywords

6. **Download**
   - Click "Download Cover Letter"
   - File saved as `cover_letter_YYYYMMDD_HHMMSS.txt`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.11** | Core programming language |
| **Streamlit** | Web application framework |
| **Groq API** | LLM for text generation |
| **PyPDF2** | PDF parsing |
| **python-docx** | DOCX parsing |
| **scikit-learn** | ATS keyword analysis (TF-IDF) |
| **python-dotenv** | Environment variable management |

---

## 📦 Dependencies

Create `requirements.txt` with:

```txt
streamlit==1.30.0
groq==0.4.0
PyPDF2==3.0.1
python-docx==1.1.0
scikit-learn==1.4.0
python-dotenv==1.0.0
numpy==1.26.3
```

---

## 🔒 Security

- **Never commit your `.env` file** - It contains your API key
- The `.gitignore` file is configured to exclude:
  - `.env`
  - `__pycache__/`
  - `*.pyc`
  - `venv/`
  - `downloads/generated_letters/`

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🗺️ Roadmap

- [ ] PDF export for cover letters
- [ ] Multiple template designs
- [ ] Email integration to send letters directly
- [ ] Multi-language support (Spanish, French, German)
- [ ] Browser extension for one-click generation
- [ ] LinkedIn integration for profile import
- [ ] Cover letter version history
- [ ] AI-powered interview prep questions

---

## 📸 Screenshots

### Main Interface
![Main Interface](./assets/screenshots/main_interface.png)

### Generated Cover Letter
![Generated Letter](./assets/screenshots/generated_letter.png)

### ATS Analysis
![ATS Analysis](./assets/screenshots/ats_analysis.png)

---

## ❓ FAQ

**Q: Is this free to use?**  
A: Yes! The code is open-source. You only need a Groq API key (free tier available).

**Q: How accurate is the ATS analysis?**  
A: It uses TF-IDF matching to identify keyword overlap. While helpful, always review manually.

**Q: Can I use this for commercial purposes?**  
A: Yes, under the MIT License terms.

**Q: What resume formats are supported?**  
A: Currently PDF and DOCX. Plain text support coming soon.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

## 👨‍💻 Author

**Shreyash Patil**

- GitHub: [@ShreyashPatil530](https://github.com/ShreyashPatil530)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/shreyash-patil-ba921737b/)
- Email: shreyashpatil530@gmail.com

---

## 🌟 Show Your Support

If this project helped you, please give it a ⭐️!

[![GitHub stars](https://img.shields.io/github/stars/ShreyashPatil530/AI-Cover-Letter-Generator?style=social)](https://github.com/ShreyashPatil530/AI-Cover-Letter-Generator/stargazers)

---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing the powerful LLM API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- All contributors and users of this project

---

<p align="center">Made with ❤️ by Shreyash Patil</p>
<p align="center">
  <a href="#-ai-cover-letter-generator">Back to Top ↑</a>
</p>
