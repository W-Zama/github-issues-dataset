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
        success = False  # 成功フラグ
        while not success:  # 成功するまでループ
            try:
                print("Collecting data from", repo.owner, repo.repo_name)
                collector.generate_csv(
                    repo.owner, repo.repo_name, labels=repo.labels, dir_path="dataset")
                success = True  # 成功した場合、フラグをTrueにしてループを抜ける

            except GithubException.RateLimitExceededException as e:
                # レート制限に達した場合の処理
                reset_time = collector.github.rate_limiting_resettime
                wait_time = reset_time - time.time()
                print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
                time.sleep(wait_time)  # レート制限がリセットされるまで待つ

            except Exception as e:
                # その他の例外の処理
                print(f"An error occurred: {e}")
                break  # 重大なエラーの場合、ループを終了


if __name__ == "__main__":
    main()
