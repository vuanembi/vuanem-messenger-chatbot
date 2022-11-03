import { BigQuery } from '@google-cloud/bigquery';

const bigquery = new BigQuery();

const dataset = 'IP_Messenger';

type StreamOptions = {
    table: string;
    schema: Record<string, any>[];
};

export const stream = <D extends Record<string, any>>(
    rows: D[],
    options: StreamOptions,
) =>
    bigquery
        .dataset(dataset)
        .table(options.table)
        .insert(rows, { schema: { fields: options.schema } })
        .then(() => rows)
        .catch((err) => console.log(err));
