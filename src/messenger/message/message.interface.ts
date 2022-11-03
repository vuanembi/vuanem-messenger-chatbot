import { Messaging } from '../messenger.interface';

export type Message = Messaging & {
    message: {
        mid: string;
        text?: string;
        quick_reply?: { payload: string };
        reply_to?: { mid: string };
    };
};
