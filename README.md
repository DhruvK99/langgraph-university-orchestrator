# LangGraph University Orchestrator 🏛️🔀

A production-grade, stateful multi-agent system built with LangGraph. This orchestrator acts as an intelligent university router, dynamically classifying incoming student queries and routing them to specialized, domain-specific AI agents (Admissions, Hostel, Placement, and Academic) for highly accurate resolution.

## 🚀 Overview
Unlike standard linear conversational agents, this project utilizes graph-based orchestration to manage complex workflows entirely locally. By implementing a cyclical state graph with persistent SQLite memory, the system can parse intent, extract student profiles, route to the appropriate departmental agent, and maintain continuous conversational context with zero API latency.

## 🧠 Architecture & Features
* **Stateful Memory:** Implements LangGraph's `SqliteSaver` to maintain persistent conversation history (thread tracking) across sessions.
* **Hybrid Routing System:** Combines fast, rule-based keyword classification with LLM-fallback profiling to extract student details and route queries efficiently.
* **Domain-Specific Agents:** Features isolated nodes representing different university departments, grounded in local Knowledge Base (KB) dictionaries to prevent hallucination.
* **100% Local Processing:** Built on Ollama, ensuring total data privacy and zero API costs.

## 🛠️ Tech Stack
* **Framework:** LangGraph, LangChain
* **Local LLM Engine:** Ollama
* **Model:** Qwen 2.5 (3B parameters)
* **Database:** SQLite (for checkpointing)
* **Language:** Python 3.x

## 💻 Quick Start
1. Ensure [Ollama](https://ollama.com/) is installed and running on your machine.
2. Pull the required local model:
   ```bash
   ollama run qwen2.5:3b
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the orchestration graph:
   ```bash
   python app.py
