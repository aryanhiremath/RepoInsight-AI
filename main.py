from clone_repo import clone_repository


def main():
    repo_url = input("Enter GitHub Repository URL: ").strip()

    repo_path = clone_repository(repo_url)

    print(f"\nRepository stored at: {repo_path}")


if __name__ == "__main__":
    main()