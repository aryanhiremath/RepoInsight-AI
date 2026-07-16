from git import Repo

repo = Repo(".")

print(f"Repository: {repo.working_dir}")
print(f"Current Branch: {repo.active_branch.name}")

# Total commits
total_commits = sum(1 for _ in repo.iter_commits())
print(f"Total Commits: {total_commits}")

# Contributors
contributors = set()
for commit in repo.iter_commits():
    contributors.add(commit.author.name)

print(f"Contributors: {', '.join(contributors)}")

# Latest commit
latest = repo.head.commit
print("\nLatest Commit")
print("-" * 40)
print(f"SHA     : {latest.hexsha[:7]}")
print(f"Author  : {latest.author.name}")
print(f"Message : {latest.message.strip()}")