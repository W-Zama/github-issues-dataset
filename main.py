import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
from dotenv import load_dotenv
import pandas as pd
from dotenv import load_dotenv

from csv_generator import csv_generator


class Repo:
    def __init__(self, owner, repo_name, labels, token=None):
        self.owner = owner
        self.repo_name = repo_name
        self.labels = labels
        self.token = token

    def set_token(self, token):
        self.token = token


def main():
    load_dotenv()

    # tokenを格納するリスト
    tokens = []
    for i in range(1, 11):
        tokens.append(os.getenv(f"ACCESS_TOKEN{i}"))

    # ownerとrepo_nameとlabelsの辞書リスト（tokensは要素に入れないでください）

    # 処理するリポジトリのリスト
    repos = [
        # Repo("vercel", "next.js", ["bug"]),
        # Repo("facebook", "react", ["Type: Bug"]),
        # Repo("jestjs", "jest", ["Bug Report"]),
        # Repo("prisma", "prisma", ["kind/bug"]),
        Repo("microsoft", "TypeScript", ["Bug"]),
        Repo("microsoft", "vscode", ["bug"]),
        Repo("microsoft", "terminal", ["Issue-Bug"]),
        # Repo("microsoft", "PowerToys", ["Issue-Bug"]),
        # Repo("swiftlang", "swift", ["bug"]),
        # Repo("TensorFlow", "tensorflow", ["type:bug"]),
    ]

    # リポジトリごとにトークンを割り当てる
    for i, repo in enumerate(repos):
        repo.set_token(tokens[i % len(tokens)])

    for repo in repos:
        csv_generator(repo.owner, repo.repo_name, repo.labels, repo.token)


if __name__ == "__main__":
    main()
