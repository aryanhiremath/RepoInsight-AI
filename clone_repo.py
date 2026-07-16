import os
import subprocess
from pathlib import Path


def clone_repository(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]

    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    repo_folder = Path("repos") / repo_name

    # Create repos folder
    os.makedirs("repos", exist_ok=True)

    # If already cloned
    if repo_folder.exists():
        print(f"✅ Repository already exists: {repo_folder}")
        return repo_folder

    print(f"📥 Cloning '{repo_name}'...")

    subprocess.run(
        [
            "git",
            "clone",
            repo_url,
            str(repo_folder)
        ],
        check=True
    )

    print("✅ Repository cloned successfully!")

    return repo_folder