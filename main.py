from clone_repo import clone_repository
from ingest import get_source_files


def main():
    repo_url = input("Enter GitHub Repository URL: ").strip()

    repo_path = clone_repository(repo_url)

    files = get_source_files(repo_path)

    print(f"\nFound {len(files)} files\n")

    for file in files[:10]:
        print(file)


if __name__ == "__main__":
    main()