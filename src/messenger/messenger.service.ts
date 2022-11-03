import {
    VerifyRequest,
    Event,
    Entry,
    MessagingType,
} from './messenger.interface';
import { Message } from './message/message.interface';
import { Referral } from './referral/referral.interface';

import { handleMessage } from './message/message.service';
import { handleReferral } from './referral/referral.service';

export const verifyService = (verification: VerifyRequest) =>
    verification['hub.mode'] === 'subscribe' &&
    verification['hub.verify_token'] === process.env.WEBHOOK_TOKEN
        ? verification['hub.challenge']
        : null;

export const webhookService = <M extends MessagingType>(event: Event<M>) =>
    Promise.all(event.entry.map((entry) => entryRouter(entry)));

export const entryRouter = <M extends Message | Referral>(entry: Entry<M>) => {
    const messaging = entry.messaging.pop() as M;

    if ('message' in messaging) {
        return handleMessage(messaging);
    } else if ('referral' in messaging) {
        return handleReferral(messaging);
    }
};
