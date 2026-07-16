from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
}

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
}


def get_source_files(repo_path: Path):
    files = []

    for file in repo_path.rglob("*"):
        if not file.is_file():
            continue

        if file.suffix not in SUPPORTED_EXTENSIONS:
            continue

        if any(folder in IGNORE_DIRS for folder in file.parts):
            continue

        files.append(file)

    return files