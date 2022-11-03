import dayjs from 'dayjs';

import { Message } from './message.interface';
import { parsePhone, phoneDetection } from './phone-detection.service';

const cases = ['0773314401', '+84 7733144 03', '077.331.4401'];

describe('Parse', () => {
    it.each(cases)('%p', (phone) => {
        const result = parsePhone(phone);
        expect(result).toBeTruthy();
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

        return phoneDetection(message)?.then((res) => expect(res).toBeTruthy());
    });
});
