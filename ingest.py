from pathlib import Path


def get_source_files(repo_path):
    files = []

    allowed_extensions = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".scss",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml"
    }

    repo_path = Path(repo_path)

    for file in repo_path.rglob("*"):

        if file.is_file() and file.suffix.lower() in allowed_extensions:

            # Ignore unwanted folders
            if any(
                folder in file.parts
                for folder in [
                    ".git",
                    "node_modules",
                    "__pycache__",
                    "venv"
                ]
            ):
                continue

            files.append(file)

    return files



def load_documents(files):

    documents = []

    for file in files:

        try:
            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            documents.append(
                {
                    "content": content,
                    "source": str(file)
                }
            )

        except Exception as e:
            print(
                f"Skipping {file}: {e}"
            )

    return documents