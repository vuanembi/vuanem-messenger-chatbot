from google.cloud import bigquery

client = bigquery.Client()
DATASET = "IP_Messenger"


def load(table, schema, id_key, cursor_key, rows) -> int:
    output_rows = (
        client.load_table_from_json(
            rows,
            f"{DATASET}.{table}",
            job_config=bigquery.LoadJobConfig(
                schema=schema,
                create_disposition="CREATE_IF_NEEDED",
                write_disposition="WRITE_APPEND" if id_key else "WRITE_TRUNCATE",
            ),
        )
        .result()
        .output_rows
    )

    if id_key and cursor_key:
        _update(table, id_key, cursor_key)

    return output_rows


def _update(table, id_key, cursor_key) -> None:
    client.query(
        f"""
        CREATE OR REPLACE TABLE {DATASET}.{table} AS
        SELECT * EXCEPT (row_num)
        FROM
        (
            SELECT
                *,
                ROW_NUMBER() over (
                    PARTITION BY {id_key}
                    ORDER BY {cursor_key} DESC
                ) AS row_num
            FROM {DATASET}.{table}
        ) WHERE row_num = 1
        """
    ).result()
