
# 🧠⚖️ AI Inner Critic vs Inner Coach

An AI-powered self-reflection tool that helps users understand their thoughts by presenting **two contrasting perspectives** — the Inner Critic and the Inner Coach — along with a balanced, actionable insight.

---

## 💡 Overview

This application simulates internal cognitive dialogue:

- 😈 **Inner Critic** → Highlights doubts, fears, and negative self-talk  
- 😇 **Inner Coach** → Provides rational, supportive, and constructive thinking  
- ⚖️ **Balanced Insight** → Combines both perspectives into a practical takeaway  

The goal is to improve **self-awareness, emotional clarity, and decision-making**.

---

## 🚀 Features

- 📝 Thought-based input analysis
- 😈 Realistic inner critic perspective
- 😇 Supportive inner coach reframing
- ⚖️ Balanced and actionable insight
- 📜 Thought history tracking
- ⚡ Interactive UI with Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Session State (for storing reflections)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/inner-critic-coach-agent.git
cd inner-critic-coach-agent
````

---

### 2️⃣ Install Dependencies

```bash id="install-inner-critic"
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```env id="env-inner-critic"
GOOGLE_API_KEY=your_gemini_api_key
```

### 4️⃣ Run the Application

```bash id="run-inner-critic"
streamlit run app.py
```

---

## 🧪 How It Works

1. Enter a thought or concern
2. Click **Analyze Thought**
3. AI generates:

   * Inner Critic (negative perspective)
   * Inner Coach (positive reframing)
   * Balanced Insight (actionable advice)
4. Review past reflections

---

## 💡 Example

**Input:**
"I feel like I'm not good enough"

**Output:**

* **Inner Critic:**
  Points out self-doubt and perceived shortcomings

* **Inner Coach:**
  Reframes the situation with logic and encouragement

* **Balanced Insight:**
  Suggests a small actionable step to improve

---


