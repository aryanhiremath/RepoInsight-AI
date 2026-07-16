from clone_repo import clone_repository
from ingest import get_source_files, load_documents
from chunker import split_documents
from embeddings import create_vector_store
from rag import ask_question


def main():

    # Get repository URL
    repo_url = input(
        "Enter GitHub Repository URL: "
    )


    # Clone repository
    repo_path = clone_repository(repo_url)


    print("\nRepository:")
    print(repo_path)



    # Find source files
    files = get_source_files(repo_path)


    print(
        f"\nFound {len(files)} files\n"
    )


    for file in files[:10]:
        print(file)



    # Load documents
    documents = load_documents(files)


    print(
        f"\nLoaded {len(documents)} documents"
    )



    # Split documents into chunks
    chunks = split_documents(documents)


    vector_store = create_vector_store(chunks)


    print(
        "\nFAISS Vector Store Created ✅"
    )


    print(
        f"\nCreated {len(chunks)} chunks"
    )



    # Display first chunk
    if chunks:

        print("\nFirst Chunk")
        print("-" * 50)

        print(
            chunks[0]["content"]
        )


        print("\nSource:")
        print(
            chunks[0]["source"]
        )



    print("\n" + "="*50)
    print("RepoInsight Ingestion Complete ✅")
    print("="*50)



    # Ask questions
    while True:

        question = input(
            "\nAsk about repository (q to exit): "
        )


        if question.lower() == "q":
            break


        answer = ask_question(
            vector_store,
            question
        )


        print("\nRepoInsight AI:")
        print(answer)



if __name__ == "__main__":
    main()