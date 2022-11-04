import dayjs from 'dayjs';

import { Message } from './message.interface';
import { parsePhone, detectPhone } from './phone-detection.service';

const cases: [string, string | undefined][] = [
    ['0773314401', '0773314401'],
    ['+84 7733144 01', '0773314401'],
    ['077.331.4401', '0773314401'],
    ['11', undefined],
    ['123', undefined],
];

describe('Parse', () => {
    it.each(cases)('%p', (phone, expected) => {
        const result = parsePhone(phone);
        expect(result).toBe(expected);
    });
});

describe('Phone Detection', () => {
    it.each(cases)('%p', async (phone) => {
        const message: Message = {
            sender: { id: 'id' },
            recipient: { id: 'id' },
            timestamp: dayjs().valueOf(),
            message: {
                mid: 'mid',
                text: phone,
            },
        };

        return detectPhone(message)?.then((res) => expect(res).toBeTruthy());
    });
});
