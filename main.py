import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
from dotenv import load_dotenv
import pandas as pd

from csv_generator import csv_generator


class Repo:
    def __init__(self, owner, repo_name, labels):
        self.owner = owner
        self.repo_name = repo_name
        self.labels = labels


def main():
    # 処理するリポジトリのリスト
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
        csv_generator(repo.owner, repo.repo_name, repo.labels)


if __name__ == "__main__":
    main()
