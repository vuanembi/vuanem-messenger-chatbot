import dayjs from 'dayjs';
import { PhoneNumberUtil, PhoneNumberFormat } from 'google-libphonenumber';

import { Message } from './message.interface';
import { stream } from '../../db/bigquery.service';

const phoneUtil = PhoneNumberUtil.getInstance();

export const parsePhone = (raw: string) => {
    try {
        return phoneUtil.parse(raw, 'VN');
    } catch (err) {
        return undefined;
    }
};

export const phoneDetection = (message: Message) => {
    const number = parsePhone(message.message.text);

    if (!number) return;

    const data = {
        mid: message.message.mid,
        timestamp: dayjs(message.timestamp).toISOString(),
        text: message.message.text,
        phone: phoneUtil
            .format(number, PhoneNumberFormat.NATIONAL)
            .replace(/[^\d]/g, ''),
    };

    return stream([data], {
        table: 'p_PhoneDetection',
        schema: [
            { name: 'mid', type: 'STRING' },
            { name: 'timestamp', type: 'TIMESTAMP' },
            { name: 'text', type: 'STRING' },
            { name: 'phone', type: 'STRING' },
        ],
    });
};
