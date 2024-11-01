import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
from dotenv import load_dotenv
import pandas as pd

from csv_generator import csv_generator

# Repoクラス


class Repo:
    def __init__(self, owner, repo_name, labels):
        self.owner = owner
        self.repo_name = repo_name
        self.labels = labels


# スレッドを使ってリポジトリを並列に処理する関数
def process_repositories_in_threads(repos):
    with ThreadPoolExecutor(max_workers=5) as executor:  # スレッド数は調整可能
        futures = [executor.submit(
            csv_generator, repo.owner, repo.repo_name, repo.labels) for repo in repos]
        for future in futures:
            future.result()  # 各スレッドの完了を待つ


# マルチプロセスでリポジトリを並列に処理する関数
def process_repositories_in_parallel(repos):
    # CPUコア数に基づいてリポジトリをプロセスごとに分割
    num_processes = min(cpu_count(), len(repos))  # CPUコア数かリポジトリ数の少ない方
    chunk_size = len(repos) // num_processes

    repo_chunks = [repos[i:i + chunk_size]
                   for i in range(0, len(repos), chunk_size)]

    with Pool(processes=num_processes) as pool:
        pool.map(process_repositories_in_threads, repo_chunks)


# メイン処理
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

    # マルチプロセスとマルチスレッドを組み合わせてリポジトリを処理
    process_repositories_in_parallel(repos)


if __name__ == "__main__":
    main()
