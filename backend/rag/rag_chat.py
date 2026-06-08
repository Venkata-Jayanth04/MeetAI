from rag.vector_store import search_query
from rag.chatbot import ask_llm


def rag_chat(question):

    retrieved_chunks = search_query(question)

    context = "\n".join(retrieved_chunks)

    answer = ask_llm(
        context=context,
        question=question
    )

    return answer