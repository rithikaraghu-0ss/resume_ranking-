# 📄 AI-Powered Resume Ranking Tool (Flask Edition)

A robust, intelligent web application designed to streamline the recruitment process. This tool uses Natural Language Processing (NLP) to rank candidate resumes against a job description and extract specific mandatory skills.

## 🚀 Key Features
- **Intelligent Ranking**: Uses TF-IDF Vectorization and Cosine Similarity to calculate a percentage match between job requirements and resumes.
- **Skill Extraction**: Automatically detects and highlights mandatory keywords/skills (e.g., "Python", "SQL", "React") within the resumes.
- **Multi-Format Support**: Processes `.pdf`, `.docx`, and `.txt` files seamlessly.
- **Modern Responsive UI**: A high-end, user-friendly interface with real-time feedback and loading animations.
- **Bulk Processing**: Upload and analyze multiple resumes simultaneously.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **NLP & ML**: Scikit-Learn (TF-IDF), Regex
- **File Parsing**: `pdfplumber` (PDF), `python-docx` (Word)
- **Frontend**: HTML5, Vanilla CSS, JavaScript (Fetch API)
- **Deployment Ready**: Configured for Render, Vercel, and Heroku.

## 📦 Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rithikaraghu-0ss/resume_ranking-
   cd resume_ranking-
   ```

2. **Set up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.

## 🚀 Deployment Guide (Render)

Render is an excellent platform for hosting this Flask application for free.

1. Create a new **Web Service** on Render.
2. Connect this GitHub repository.
3. Configure the following settings:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Click **Deploy**.

## 🗺️ How it Works
1. **Extraction**: The server extracts raw text from various file formats.
2. **Preprocessing**: Text is normalized (lowercased, special characters removed) to ensure accurate matching.
3. **Keyword Search**: The tool searches for specific user-defined skills using precise word-boundary regex.
4. **Vectorization**: The job description and all resumes are converted into TF-IDF vectors.
5. **Similarity Calculation**: Cosine similarity is used to determine the mathematical "closeness" of each resume to the job requirements.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
