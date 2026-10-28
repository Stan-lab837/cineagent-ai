
import os
from typing import Dict, Any
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

# 1. Определяем структуру состояния агента (State)
class AgentState(TypedDict):
    movie_title: str
    runtime_minutes: int
    has_dubbing: bool
    compliance_status: str
    generated_email: str
    errors: list

# 2. Шаг 1: Проверка комплаенса (Technical Compliance Node)
def check_compliance_node(state: AgentState) -> Dict[str, Any]:
    print("--- [CineAgent AI] Running Technical Compliance Check... ---")
    
    # Имитация проверки через FFmpeg (проверяем хронометраж и наличие дубляжа)
    errors = []
    if state["runtime_minutes"] < 90:
        errors.append("Film is too short for a feature-length category.")
    if not state["has_dubbing"]:
        errors.append("Missing international dubbing track.")
        
    status = "PASSED" if not errors else "FAILED"
    
    return {
        "compliance_status": status,
        "errors": errors
    }

# 3. Шаг 2: Генерация B2B-письма (Email Generation Node)
def generate_email_node(state: AgentState) -> Dict[str, Any]:
    print("--- [CineAgent AI] Generating Personalized B2B Pitch... ---")
    
    if state["compliance_status"] == "FAILED":
        return {"generated_email": "Blocker: B2B outreach aborted due to compliance failure."}
    
    # Инициализация LLM (требуется ANTHROPIC_API_KEY в окружении)
    # Для тестов без ключа можно заменить на простую f-строку
    try:
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.3)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an elite B2B sales agent for movie distribution. Write a short 2-paragraph outreach email based on the movie details provided."),
            ("human", "Title: {title}, Runtime: {runtime} min, Dubbing: French. Write a pitch to an acquisition manager.")
        ])
        
        chain = prompt | llm
        response = chain.invoke({
            "title": state["movie_title"],
            "runtime": state["runtime_minutes"]
        })
        email_text = response.content
    except Exception:
        # Резервный вариант, если API-ключ не задан
        email_text = f"Subject: Pitch for {state['movie_title']}\n\nDear Buyer,\nThis is a fallback pitch for our {state['runtime_minutes']}-minute thriller."

    return {"generated_email": email_text}

# 4. Построение графа LangGraph
workflow = StateGraph(AgentState)

# Добавляем узлы в граф
workflow.add_node("compliance_checker", check_compliance_node)
workflow.add_node("email_generator", generate_email_node)

# Задаем логику переходов (Эдmanagement)
workflow.set_entry_point("compliance_checker")
workflow.add_edge("compliance_checker", "email_generator")
workflow.add_edge("email_generator", END)

# Компилируем приложение
cine_agent = workflow.compile()

# 5. Запуск прототипа с начальными данными вашего фильма
if __name__ == "__main__":
    initial_state = {
        "movie_title": "Paris 1970",
        "runtime_minutes": 110,
        "has_dubbing": True,
        "compliance_status": "PENDING",
        "generated_email": "",
        "errors": []
    }
    
    print("Starting CineAgent AI Execution Loop...")
    final_output = cine_agent.invoke(initial_state)
    
    print("\n=== FINAL AGENT OUTPUT ===")
    print(f"Compliance Status: {final_output['compliance_status']}")
    print("\nGenerated Pitch Email:")
    print(final_output['generated_email'])
