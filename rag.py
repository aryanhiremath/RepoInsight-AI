from langchain_ollama import ChatOllama


def ask_question(vector_store, question):

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 4
        }
    )


    docs = retriever.invoke(question)


    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )


    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0
    )


    prompt = f"""
        You are RepoInsight AI.

        Answer the question based only on this repository context.

        Repository Context:
        {context}


        Question:
        {question}


        Answer:
    """


    response = llm.invoke(prompt)

    return response.content