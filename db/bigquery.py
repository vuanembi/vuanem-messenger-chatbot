import re
from google.cloud import bigquery
import numpy as np
from datetime import datetime

client = bigquery.Client()

DATASET = "IP_Messenger"


def insert(table: str, rows: list[dict]):
    return client.insert_rows_json(f"{DATASET}.{table}", rows)
