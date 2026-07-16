from pathlib import Path
import shutil
from git import Repo


REPOS_DIR = Path("repos")
REPOS_DIR.mkdir(exist_ok=True)


def clone_repository(repo_url: str) -> Path:
    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = REPOS_DIR / repo_name

    if clone_path.exists():
        shutil.rmtree(clone_path)

    print(f"📥 Cloning {repo_name}...")

    Repo.clone_from(repo_url, clone_path)

    print("✅ Repository cloned successfully!")

    return clone_path