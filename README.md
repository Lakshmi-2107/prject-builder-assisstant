# 🚀 AI Project Builder Pro

AI Project Builder Pro is an intelligent system that converts a simple idea into a **complete AI-powered project**, including planning, code generation, live demo, and export.

---

## 📌 Problem Understanding

Many developers and students struggle to convert an idea into a complete working project.  
They often lack:
- Structured planning  
- Proper tech stack decisions  
- Implementation guidance  
- Working demo  

This system automates the **entire project lifecycle**.

---

## 🔍 Research & Existing Solutions

### Existing Systems
- AutoGPT  
- LangChain Agents  
- OpenAI GPT Builder  

### Limitations
- Complex setup  
- Not beginner-friendly  
- No dynamic UI generation  
- No full lifecycle support  
- Limited structured outputs  

### Our Improvement
- Simple UI  
- Dynamic UI generation  
- End-to-end automation  
- Structured outputs  
- Exportable working code  

---

## ✨ Features

### 🧠 AI Project Planning
- Problem statement  
- Functional & Non-functional requirements  
- Tech stack  
- Architecture  
- Milestones  

---

### ⚡ Dynamic UI
- Text input  
- Number input  
- Dropdown  
- Slider  
- Auto-generated based on idea  

---

### 🌐 Live Demo
- Real application simulation  
- Structured outputs:
  - Health → Diagnosis  
  - Travel → Itinerary  
  - Finance → Insights  

---

### 💻 Code Generation
- Complete Streamlit app  
- UI + Logic + Output  
- Ready to run  

---

### 📦 Export
- Download ZIP  
- Includes:
  - `app.py`
  - `requirements.txt`

---

## 🏗️ Architecture
User Input
↓
Plan Generator (Mistral)
↓
UI Generator (Phi3)
↓
Code Generator (Mistral)
↓
Demo Engine (Phi3)
↓
Output (Plan + Code + Demo)


---

## ⚙️ Approach

- Multi-model system:
  - Mistral → Planning + Code  
  - Phi3 → UI + Demo  

- Modular design:
  - Separate components  
  - Dynamic rendering  
  - Real-time processing  

---

## 🔄 Failed Attempts

### ❌ Static UI
- Hardcoded inputs  
- Not scalable  

### ❌ Single Model
- Poor output quality  
- Inconsistent responses  

### ✅ Final Solution
- Multi-model architecture  
- Improved accuracy  

---

## ⚠️ Challenges

- Ollama timeout issues  
- UI JSON parsing errors  
- Output formatting  
- Handling dynamic inputs  

---

## 📚 Learnings

- Prompt engineering is critical  
- Multi-model systems work better  
- Real systems need error handling  
- Dynamic UI is complex but powerful  

---

## 🛠️ Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- AI Models: Mistral, Phi3 (Ollama)  
- API: REST (local)  
- Packaging: Zip  

---

## ⚙️ Installation

### Clone Repo
```bash
git clone https://github.com/your-username/ai-project-builder.git
cd ai-project-builder

Install Dependencies
pip install streamlit requests
Install Ollama

Download from: https://ollama.com

Pull Models
ollama pull mistral
ollama pull phi3
Start Server
ollama serve
Run App
streamlit run app.py

##🚀 Usage
Enter project idea
Click "Generate Project"
Explore:
Plan
Code
Demo
Export