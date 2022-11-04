import dayjs from 'dayjs';

import { Referral } from './referral.interface';
import { store } from './store.service';

describe('Store', () => {
    it('Store', async () => {
        const message: Referral = {
            sender: { id: 'id' },
            recipient: { id: 'id' },
            timestamp: dayjs().valueOf(),
            postback: {
                mid: 'mid',
                title: 'title',
                payload: undefined,
                referral: {
                    source: 'source',
                    type: 'type',
                    ref: 'ref',
                    referer_uri: undefined,
                    is_guest_user: undefined,
                    ad_id: 'ad_id',
                    ads_context_data: {
                        ad_title: 'ad_title',
                        post_id: 'post_id',
                        video_url: 'video_url',
                        photo_url: 'photo_url',
                        product_id: 'product_id',
                    },
                },
            },
        };

        return store(message)?.then((res) => expect(res).toBeTruthy());
    });
});
