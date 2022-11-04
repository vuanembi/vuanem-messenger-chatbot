import { Messaging } from '../messenger.interface';

export type Referral = Messaging & {
    referral: {
        source: string;
        type: string;
        ref?: string;
        referer_uri?: string;
        is_guest_user?: string;
        ad_id?: string;
        ads_context_data: {
            ad_title: string;
            post_id: string;
            video_url?: string;
            photo_url?: string;
            product_id?: string;
        };
    };
};
