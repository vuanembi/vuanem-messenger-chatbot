import dayjs from 'dayjs';

import { Message } from './message.interface';
import { store } from './store.service';

const cases = ['0773314401', '+84 7733144 03', '077.331.4401'];

describe('Store', () => {
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

        return store(message)?.then((res) => expect(res).toBeTruthy());
    });
});
