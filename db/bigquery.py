from google.cloud import bigquery

client = bigquery.Client()

DATASET = "IP_Messenger"


def insert(table: str, rows: list[dict]):
    return client.insert_rows_json(f"{DATASET}.{table}", rows)
