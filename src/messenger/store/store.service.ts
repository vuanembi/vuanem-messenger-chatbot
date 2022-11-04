import dayjs from 'dayjs';

import { stream } from '../../db/bigquery.service';
import { Entry } from '../messenger.interface';
import { isMessage } from '../message/message.service';
import { isReferral } from '../referral/referral.service';
import { Message } from '../message/message.interface';
import { Referral } from '../referral/referral.interface';

export const parseData = (entry: Entry) => {
    const messaging = entry.messaging[0];

    const parseMessage = ({ message }: Message) => ({
        mid: message.mid,
        text: message.text,
        quick_reply: {
            payload: message.quick_reply?.payload,
        },
        reply_to: {
            mid: message.reply_to?.mid,
        },
    });

    const parseReferral = ({ referral }: Referral) => ({
        source: referral.source,
        type: referral.type,
        ref: referral.ref,
        referer_uri: referral.referer_uri,
        is_guest_user: referral.is_guest_user,
        ad_id: referral.ad_id,
        ads_context_data: {
            ad_title: referral.ads_context_data.ad_title,
            post_id: referral.ads_context_data.post_id,
            video_url: referral.ads_context_data.video_url,
            photo_url: referral.ads_context_data.photo_url,
            product_id: referral.ads_context_data.product_id,
        },
    });

    return {
        id: entry.id,
        time: dayjs(entry.time).toISOString(),
        messaging: {
            sender: messaging.sender,
            recipient: messaging.recipient,
            timestamp: dayjs(messaging.timestamp).toISOString(),
            message: isMessage(messaging) ? parseMessage(messaging) : undefined,
            referral: isReferral(messaging)
                ? parseReferral(messaging)
                : undefined,
        },
    };
};

export const storeService = async (entries: Entry[]) =>
    stream(
        entries.map((entry) => parseData(entry)),
        {
            table: 'p_Entry',
            schema: [
                { name: 'id', type: 'STRING' },
                { name: 'time', type: 'TIMESTAMP' },
                {
                    name: 'messaging',
                    type: 'RECORD',
                    fields: [
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
                                    fields: [
                                        { name: 'payload', type: 'STRING' },
                                    ],
                                },
                                {
                                    name: 'reply_to',
                                    type: 'RECORD',
                                    fields: [{ name: 'mid', type: 'STRING' }],
                                },
                            ],
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
            ],
        },
    );
