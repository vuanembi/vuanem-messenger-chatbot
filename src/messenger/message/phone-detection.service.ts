import dayjs from 'dayjs';
import { PhoneNumberUtil, PhoneNumberFormat } from 'google-libphonenumber';

import { Message } from './message.interface';
import { stream } from '../../db/bigquery.service';

const phoneUtil = PhoneNumberUtil.getInstance();

export const parsePhone = (raw: string) => {
    try {
        const number = phoneUtil.parse(raw, 'VN');
        const phone = phoneUtil
            .format(number, PhoneNumberFormat.NATIONAL)
            .replace(/[^\d]/g, '');

        if (!phone || !phone.match(/(84|0[3|5|7|8|9])+([0-9]{8})\b/g)) {
            return undefined;
        } else {
            return phone;
        }
    } catch (err) {
        return undefined;
    }
};

export const detectPhone = (message: Message) => {
    const { text } = message.message;

    const phone = text && parsePhone(text);

    return (
        phone &&
        stream(
            [
                {
                    mid: message.message.mid,
                    timestamp: dayjs(message.timestamp).toISOString(),
                    text: message.message.text,
                    phone,
                },
            ],
            {
                table: 'p_PhoneDetection',
                schema: [
                    { name: 'mid', type: 'STRING' },
                    { name: 'timestamp', type: 'TIMESTAMP' },
                    { name: 'text', type: 'STRING' },
                    { name: 'phone', type: 'STRING' },
                ],
            },
        )
    );
};
