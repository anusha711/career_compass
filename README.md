# 🎯 CareerCompass:Precision-Driven Career Alignment Agent (Capstone Project)

> 💡 **Current deployment:** CareerCompass is currently deployed and running as a **Kaggle Notebook**.  
> You can explore, run, and modify the full workflow directly here:

 <a href="https://www.kaggle.com/code/anusha711/careercompass-capstone" target="_blank">
 <img align="centre" alt="Open in Kaggle" src="https://kaggle.com/static/images/open-in-kaggle.svg">
 </a>

<br clear="both" />

> A multi-agent system that parses your resume, matches it to job descriptions, scores the fit, and generates tailored interview prep and cover letters.

Built as part of the **Google 5-Day AI Agents Intensive (Kaggle Capstone)**, this project demonstrates how to design, orchestrate, and evaluate AI agents using modern agentic patterns and Google’s Gemini models.

---

## 🚀 What does CareerCompass do?

Given a candidate’s **resume** and one or more **job descriptions**, CareerCompass:

1. **Parses the resume** to extract technical & soft skills  
2. **Matches** the resume against a selected Job Description (JD)  
3. **Generates a match score** (0–10) with reasoning  
4. **Routes the workflow** based on the score:
   - **Score > 6** → strong match  
     - Generate a tailored **cover letter**  
     - Generate **hard-level** interview questions  
   - **Score 4–6** → moderate match  
     - Generate **medium-level** interview questions  
   - **Score < 4** → weak match  
     - Generate **easy, step-by-step** interview questions  
5. Supports **human-in-the-loop** interaction (e.g., ask for 5 more questions, new JD, different resume, etc.)

---

## 🧠 Multi-Agent Architecture

CareerCompass follows a **modular, multi-agent architecture**:

1. **Agent 1: Skill Extraction Agent (`skill_agent.py`)**
   - Extracts:
     - `technical_skills`: tools, frameworks, languages, platforms  
     - `soft_skills`: communication, leadership, problem-solving, etc.
   - Uses a structured JSON schema to keep responses clean & machine-readable.

2. **Agent 2: Scoring & Difficulty Agent (`scoring_agent.py`)**
   - Compares the resume against the selected JD.
   - Produces:
     - A **match score** out of 10  
     - A **difficulty level**: `Easy`, `Medium`, or `Hard` (used by the interview agent)
   - Includes short reasoning for transparency.

3. **Agent 3: Technical Interview Coach (`interview_agent.py`)**
   - Generates **exactly 5** technical questions + answers per round.
   - Inputs:
     - `top_skills` from Agent 1  
     - `difficulty_level` from Agent 2  
     - `context` to avoid repeating previous questions  
   - **Human-in-the-loop**: after 5 Q&A, asks if the user wants 5 more, while maintaining context.

4. **Agent 4: Professional Writer – Cover Letter Agent (`cover_letter_agent.py`)**
   - Drafts a **personalized cover letter**:
     - Uses resume highlights  
     - Uses the selected JD  
     - Mirrors tone & keywords relevant to the role

5. **Orchestrator (`main.py`)**
   - Controls the full workflow:
     - Load resume → Extract skills → Score match → Route to cover letter / interview logic.
   - Implements **routing pattern** based on score thresholds.
   - Logs key steps for basic **observability** (e.g., `log_event(agent_name, stage, message, extra={})`).

---

## 🧱 Tech Stack

- **Language:** Python  
- **Models:** Google Gemini (e.g., `gemini-2.5` / Gemini Pro via Google GenAI SDK)  
- **Environment:** Kaggle Notebook / Local Python environment  
- **Patterns Used:**
  - Multi-agent orchestration  
  - Context engineering (sessions & memory hints)  
  - Simple evaluation & logging hooks  

---



## 📂 Project Structure (Still working on GitHub Repository)

```bash
career_compass/
│
├── .env                     # Stores your API key locally (for non-Kaggle use)
├── requirements.txt         # Python dependencies
├── config.py                # Model configuration & API setup
├── utils.py                 # Shared helpers (JSON parsing, logging, etc.)
├── main.py                  # The Orchestrator (entry point)
│
└── agents/                  # Individual agents
    ├── __init__.py
    ├── skill_agent.py       # Agent 1 – Skill Extraction
    ├── scoring_agent.py     # Agent 2 – Scoring & Difficulty
    ├── interview_agent.py   # Agent 3 – Interview Coach
    └── interview_agent.py   # Agent 3 – Interview Coach
