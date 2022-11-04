import dayjs from 'dayjs';

import { stream } from '../../db/bigquery.service';
import { Referral } from './referral.interface';

export const store = (message: Referral) =>
    stream(
        [
            {
                sender: message.sender,
                recipient: message.recipient,
                timestamp: dayjs(message.timestamp).toISOString,
                referral: {
                    source: message.referral.source,
                    type: message.referral.type,
                    ref: message.referral.ref,
                    referer_uri: message.referral.referer_uri,
                    is_guest_user: message.referral.is_guest_user,
                    ad_id: message.referral.ad_id,
                    ads_context_data: {
                        ad_title: message.referral.ads_context_data.ad_title,
                        post_id: message.referral.ads_context_data.post_id,
                        video_url: message.referral.ads_context_data.video_url,
                        photo_url: message.referral.ads_context_data.photo_url,
                        product_id:
                            message.referral.ads_context_data.product_id,
                    },
                },
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
    );
