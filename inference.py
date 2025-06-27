import os
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create LLM instance using Groq
llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")

def get_reference_ranges(gender):
    gender = gender.lower()
    return {
        "hb": (13.5, 17.5) if gender == "male" else (12.0, 15.5),
        "wbc": (4500, 11000),
        "platelet": (150000, 450000),
        "esr": (0, 10) if gender == "male" else (0, 20),
        "sugar": (70, 100),
    }

def classify_value(value, low, high):
    def safe_deviation(val, ref):
        return abs(val - ref) / ref if ref != 0 else float('inf')
    
    if low <= value <= high:
        return f"{value} (normal)"
    elif safe_deviation(value, high) <= 0.05 or safe_deviation(value, low) <= 0.05:
        return f"{value} (borderline abnormal)"
    else:
        return f"{value} (abnormal)"



def get_medical_analysis(gender,hb, wbc, platelet, esr, sugar):
    ranges = get_reference_ranges(gender)
    tagged_inputs = {
        "gender": gender.capitalize(),
        "hb": classify_value(hb, *ranges["hb"]),
        "wbc": classify_value(wbc, *ranges["wbc"]),
        "platelet": classify_value(platelet, *ranges["platelet"]),
        "esr": classify_value(esr, *ranges["esr"]),
        "sugar": classify_value(sugar, *ranges["sugar"]),
    }
    prompt = PromptTemplate(
    input_variables=["gender","hb", "wbc", "platelet", "esr", "sugar"],
    template = """
You are a helpful and medically knowledgeable assistant. A patient has provided the following blood test values:

- Gender: {gender}
- Hemoglobin: {hb} g/dL
- WBC: {wbc} /mm³
- Platelet Count: {platelet} /µL
- ESR: {esr} mm/hr
- Fasting Blood Sugar: {sugar} mg/dL

Your task is to analyze the results using strict interpretation of the reference ranges provided below. Use the correct reference ranges for **Hemoglobin** and **ESR** based on the patient's gender.

🔍 Please provide the following analysis:

---

### 1. ✅ Normal Values
- List all values that are **strictly within (inclusive)** the reference range.
- Mention the patient's actual value and the exact reference range used.
- If **none are normal**, say: _"No lab values fall within the normal range."_

---

### 2. ⚠️ Abnormal Values
- List any value that is **outside** the reference range.
- Include:
  - The patient’s value
  - The exact reference range
  - Whether it is "high" or "low"
  - A brief clinical interpretation (e.g., may indicate anemia, inflammation, etc.)

---

### 3. 🔸 Borderline Abnormal Values
- If a value is **just outside** the normal range (within ~5% deviation), list it here.
- Clearly explain why it's borderline and what it might suggest clinically.
- **Do not include borderline values in the normal list.**

---

### 4. 💡 Possible Conditions
- Based **only** on the abnormal and borderline findings, list possible diseases or conditions.
- Be medically realistic and concise.

---

### 5. 📝 Recommended Next Steps
- Provide practical follow-up steps (e.g., repeat tests, further evaluations, lifestyle suggestions, or referrals).
- Only suggest tests or referrals relevant to the abnormal/borderline findings.

---

📚 Reference Ranges:
- Hemoglobin:
    - 13.5–17.5 g/dL (men)
    - 12.0–15.5 g/dL (women)
- WBC: 4,500–11,000 /mm³
- Platelet Count: 150,000–450,000 /µL
- ESR:
    - 0–10 mm/hr (men)
    - 0–20 mm/hr (women)
- Fasting Blood Sugar: 70–100 mg/dL

---

📌 Evaluation Rules:
- ✅ A value is **normal only if it is inside the reference range (inclusive).**
- ⚠️ A value **outside** the reference range must be labeled **abnormal**.
- 🔸 If a value is within **5% of the limit**, label it as **borderline abnormal** and explain why.
- ❗ Do **not classify any value as normal if it exceeds or falls short of the reference range.**
- ❗ If **Platelet Count is 490,000**, and the upper limit is 450,000 → it is **abnormal** (not borderline).
- Hemoglobin and ESR **must be classified based on gender**. Use inclusive boundary values (e.g., if upper limit is 450,000, then 450,000 is normal).
- For **WBC, Platelet, Sugar**, use strict inclusive bounds. If value = upper/lower bound, it's **normal**.
- Any value just 1–5% above/below the limit must be **"borderline abnormal"**.

---

🧠 Format the output in **Markdown with headers, bullets, and appropriate emojis** for clarity.
"""
    )

    
    chain = prompt | llm
    response = chain.invoke(tagged_inputs)

    
    
    return response.content









