# 🩺 AI-Powered Medical Lab Report Analyzer

This is an AI-based web application that analyzes standard blood test results and provides medical interpretations using LLaMA3 (via Groq), LangChain, and Streamlit.

---

## 📌 Features

* Accepts manual input for key lab values:

  * Hemoglobin (g/dL)
  * WBC (/mm³)
  * Platelet Count (/ µL)
  * ESR (mm/hr)
  * Fasting Blood Sugar (mg/dL)
  * Gender (Male / Female)
* Classifies each parameter as:

  * ✅ Normal
  * 🔸 Borderline Abnormal (within \~5% of range)
  * ⚠️ Abnormal
* Uses gender-specific ranges for Hemoglobin and ESR
* AI-generated markdown report with interpretation, conditions, and next steps
* Built with Streamlit for easy interaction

---

## 🧠 How It Works

1. User enters lab values in the Streamlit web interface
2. Values are evaluated against medical reference ranges
3. A prompt is created using LangChain and passed to LLaMA3
4. AI generates a report with structured medical feedback
5. Report is shown in Markdown format in the Streamlit app

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nazzzzzz096/AI-lab-report-analyser.git 
cd ai-medical-lab-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env`

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Sample Input

| Parameter      | Value  |
| -------------- | ------ |
| Gender         | Female |
| Hemoglobin     | 11.5   |
| WBC            | 8000   |
| Platelet Count | 470000 |
| ESR            | 22     |
| Fasting Sugar  | 101    |

---

## 📊 Example Output

```
### 2. ⚠️ Abnormal Values
- Hemoglobin: 11.5 g/dL (Low) – May suggest anemia
- Platelet Count: 470000 µL (High) – May suggest inflammation

### 3. 🔸 Borderline Abnormal
- Fasting Blood Sugar: 101 mg/dL (Slightly High)

### 4. 💡 Possible Conditions
- Mild anemia
- Possible early-stage metabolic imbalance

### 5. 📝 Recommended Next Steps
- Repeat blood test in 1-2 weeks
- Consider iron supplementation
```

---

## 📦 Tech Stack

* 🧠 LLaMA3 via Groq API
* 🔗 LangChain
* 🌐 Streamlit
* 🐍 Python
* 📁 dotenv (for managing secrets)

---

## 📚 Reference Ranges Used

| Parameter     | Male          | Female    |
| ------------- | ------------- | --------- |
| Hemoglobin    | 13.5–17.5     | 12.0–15.5 |
| WBC           | 4500–11000    | Same      |
| Platelets     | 150000–450000 | Same      |
| ESR           | 0–10          | 0–20      |
| Fasting Sugar | 70–100        | Same      |

---

## 📈 Future Enhancements

* Add support for PDF input and OCR
* Add more lab tests (thyroid, liver, lipid panels)
* Export reports to PDF
* Deploy on Streamlit Cloud or Hugging Face
* Multilingual support

---

## 🤝 Contributions

Pull requests welcome! Please open an issue first for discussion.


---
