from github_bug_data_collector.data_collector import DataCollector
from dotenv import load_dotenv
import os
import pandas as pd


def csv_generator(owner, repo, labels, token):
    load_dotenv()

    end_time = os.getenv("END_TIME")

    collector = DataCollector(token)

    df = collector.generate_dataframe(
        owner, repo, labels=labels, until=pd.to_datetime(end_time))

    # datasetディレクトリが存在しない場合は作成
    if not os.path.exists("dataset"):
        os.makedirs("dataset")

    df.to_csv(f"dataset/{owner}_{repo}.csv", index=False)
