import dayjs from 'dayjs';
import { stream } from '../../db/bigquery.service';
import { Message } from './message.interface';

export const store = (message: Message) =>
    stream(
        [
            {
                ...message,
                timestamp: dayjs(message.timestamp).toISOString,
            },
        ],
        {
            table: 'p_Message',
            schema: [
                {
                    name: 'sender',
                    type: 'RECORD',
                    fields: [{ name: 'id', type: 'STRING' }],
                },
                {
                    name: 'recipient',
                    type: 'RECORD',
                    fields: [{ name: 'id', type: 'STRING' }],
                },
                {
                    name: 'timestamp',
                    type: 'TIMESTAMP',
                },
                {
                    name: 'message',
                    type: 'RECORD',
                    fields: [
                        { name: 'mid', type: 'STRING' },
                        { name: 'text', type: 'STRING' },
                        {
                            name: 'quick_reply',
                            type: 'RECORD',
                            fields: [{ name: 'payload', type: 'STRING' }],
                        },
                        {
                            name: 'reply_to',
                            type: 'RECORD',
                            fields: [{ name: 'mid', type: 'STRING' }],
                        },
                    ],
                },
            ],
        },
    );
