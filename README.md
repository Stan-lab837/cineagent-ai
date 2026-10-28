# CineAgent AI: Autonomous B2B Film Distribution Agent

**CineAgent AI** is an advanced, production-ready MediaTech solution designed to streamline, automate, and democratize global film distribution for independent filmmakers and production studios. 

Built on top of a cutting-edge **Agentic AI architecture**, CineAgent AI shifts the industry paradigm from fragmented generative assistants to full, end-to-end task execution. It autonomously handles the technical compliance, asset generation, and B2B negotiation layers required to license content to international streaming platforms like Netflix and Amazon Prime.

---

## 🔥 Key Features & Capabilities

*   **Multimodal Technical Compliance Engine:** Utilizing integration scripts (`FFmpeg`), the agent automatically inspects raw video/audio metadata, verifying constraints such as runtime guidelines, audio loudness standards, and language asset profiles (subtitles/dubbing).
*   **Cyclic Reason & Self-Correction Loops:** Powered by `LangGraph`, the agent operates through robust finite state machines. If generated outputs do not match precise platform delivery specifications, the system loops back to execute automated self-correction.
*   **Autonomous B2B Outreach:** Programmatically drafts hyper-personalized distribution pitches and orchestrates outreach to targeted global content buyers through communication APIs, seamlessly syncing interaction logs with CRM data.

---

## 🛠️ Architecture & Tech Stack

*   **Agentic Framework:** `LangGraph` (for complex cyclic state graphs and reasoning loops)
*   **Orchestration & RAG:** `LlamaIndex` & `LangChain`
*   **Core Reasoning Model:** `Claude 3.5 Sonnet` (Anthropic)
*   **Multimodal File Inspection:** `GPT-4o` (OpenAI) & `FFmpeg`
*   **Vector Database:** `Qdrant` / `Pinecone` (for legal documents and platform guidelines)
*   **Backend Interface:** `FastAPI` (Python)

---

## 🚀 Quick Start & MVP Simulation

To run the core agent state logic simulating technical compliance verification and automated pitch generation locally, execute the following script:

```bash
# Install dependencies
pip install langgraph langchain-core langchain-anthropic

# Run the agent
python agent.py
```

---

## 🏆 Competition Note

This project is explicitly developed for the **Create AI Agents Championship** hosted by the **Dubai Chamber of Digital Economy** (January 2027 Deadline). CineAgent AI addresses critical bottlenecks in the Middle East and global creative economy by digitizing and automating global B2B media supply chains.
