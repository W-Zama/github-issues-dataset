from github_bug_data_collector.data_collector import DataCollector
import os
from dotenv import load_dotenv
from github import Github, GithubException
import time
from datetime import datetime


class Repo:
    def __init__(self, owner, repo_name, labels):
        self.owner = owner
        self.repo_name = repo_name
        self.labels = labels


def main():
    load_dotenv()

    token = os.getenv("ACCESS_TOKEN")
    collector = DataCollector(token)

    repos = [
        Repo("vercel", "next.js", ["bug"]),
        Repo("facebook", "react", ["Type: Bug"]),
        Repo("jestjs", "jest", ["Bug Report"]),
        Repo("prisma", "prisma", ["kind/bug"]),
        Repo("microsoft", "TypeScript", ["Bug"]),
        Repo("microsoft", "vscode", ["bug"]),
        Repo("microsoft", "terminal", ["Issue-Bug"]),
        Repo("microsoft", "PowerToys", ["Issue-Bug"]),
        Repo("swiftlang", "swift", ["bug"]),
        Repo("TensorFlow", "tensorflow", ["type:bug"]),
    ]

    for repo in repos:
        print("Collecting data from", repo.owner, repo.repo_name)
        collector.generate_csv(
            repo.owner, repo.repo_name, labels=repo.labels, dir_path="dataset")


if __name__ == "__main__":
    main()
