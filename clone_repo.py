from pathlib import Path
from git import Repo

# Folder where all repositories will be stored
REPOS_DIR = Path("repos")
REPOS_DIR.mkdir(exist_ok=True)


def clone_repository(repo_url: str) -> Path:
    """
    Clone a GitHub repository if it doesn't already exist.
    Returns the path to the cloned repository.
    """

    # Extract repository name from URL
    repo_name = repo_url.rstrip("/").split("/")[-1]

    # Destination path
    clone_path = REPOS_DIR / repo_name

    # If already cloned, reuse it
    if clone_path.exists():
        print(f"✅ Repository '{repo_name}' already exists.")
        return clone_path

    print(f"📥 Cloning '{repo_name}'...")

    Repo.clone_from(repo_url, clone_path)

    print("✅ Repository cloned successfully!")

    return clone_path