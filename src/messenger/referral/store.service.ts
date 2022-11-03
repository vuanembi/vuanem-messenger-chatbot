import dayjs from 'dayjs';

import { stream } from '../../db/bigquery.service';
import { Referral } from './referral.interface';

export const store = (message: Referral) =>
    stream(
        [
            {
                ...message,
                timestamp: dayjs(message.timestamp).toISOString,
            },
        ],
        {
            table: 'p_Referral',
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
                    name: 'postback',
                    type: 'RECORD',
                    fields: [
                        { name: 'mid', type: 'STRING' },
                        { name: 'title', type: 'STRING' },
                        { name: 'payload', type: 'STRING' },
                        {
                            name: 'referral',
                            type: 'RECORD',
                            fields: [
                                { name: 'source', type: 'STRING' },
                                { name: 'type', type: 'STRING' },
                                { name: 'ref', type: 'STRING' },
                                { name: 'referer_uri', type: 'STRING' },
                                { name: 'is_guest_user', type: 'STRING' },
                                { name: 'ad_id', type: 'STRING' },
                                {
                                    name: 'ads_context_data',
                                    type: 'RECORD',
                                    fields: [
                                        { name: 'ad_title', type: 'STRING' },
                                        { name: 'post_id', type: 'STRING' },
                                        { name: 'video_url', type: 'STRING' },
                                        { name: 'photo_url', type: 'STRING' },
                                        { name: 'product_id', type: 'STRING' },
                                    ],
                                },
                            ],
                        },
                    ],
                },
            ],
        },
    );
