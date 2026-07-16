from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            " ",
            ""
        ]
    )

    chunks = []

    for doc in documents:

        splits = splitter.split_text(
            doc["content"]
        )

        for chunk in splits:
            chunks.append(
                {
                    "content": chunk,
                    "source": doc["source"]
                }
            )

    return chunks