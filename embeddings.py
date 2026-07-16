from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks):

    texts = []

    metadatas = []


    for chunk in chunks:

        texts.append(
            chunk["content"]
        )

        metadatas.append(
            {
                "source": chunk["source"]
            }
        )


    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )


    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )


    return vector_store