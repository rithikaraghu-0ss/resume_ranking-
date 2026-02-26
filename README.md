# 📄 AI-Powered Resume Ranking Tool

An intelligent, web-based tool built with **Streamlit** and **Python** to automate the process of screening resumes. It uses NLP (TF-IDF Vectorization & Cosine Similarity) to rank candidates based on their relevance to a specific job description.

## 🚀 Features
- **Multi-format Support**: Upload resumes in PDF, DOCX, or TXT formats.
- **Smart Ranking**: Calculates similarity scores between resumes and job descriptions using Scikit-Learn.
- **Progress Tracking**: Real-time progress bar for bulk processing.
- **Data Export**: Download the ranked results as a CSV file for further analysis.
- **Clean UI**: Gradient-colored rankings and easy-to-use interface.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **File Parsing**: `pdfplumber`, `python-docx`
- **NLP**: `scikit-learn` (TF-IDF, Cosine Similarity)
- **Data Handling**: `pandas`, `numpy`

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rithikaraghu-0ss/resume_ranking-
   cd resume_ranking-
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run resume_app.py
   ```

## 🗺️ How it Works
1. **Extraction**: The tool extracts raw text from uploaded files using specialized libraries.
2. **Preprocessing**: It cleans the text by removing special characters and normalizing whitespace.
3. **Vectorization**: It converts the text into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) which highlights important keywords.
4. **Comparison**: It calculates the cosine of the angle between the job description vector and each resume vector to determine a similarity percentage.
5. **Ranking**: Results are sorted and displayed in a tiered table.

## 📄 License
This project is licensed under the MIT License.
