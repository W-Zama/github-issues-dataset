from github_bug_data_collector.data_collector import DataCollector
from dotenv import load_dotenv
import os
import pandas as pd


def csv_generator(ower, repo, labels):
    load_dotenv()

    token = os.getenv("ACCESS_TOKEN")
    end_time = os.getenv("END_TIME")

    collector = DataCollector(token)

    df = collector.generate_dataframe(ower, repo, labels=
        labels, until=pd.to_datetime(end_time))

    df.to_csv(f"dataset/{ower}_{repo}.csv", index=False)

