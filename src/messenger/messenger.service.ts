import { Entry, Event, VerifyRequest } from './messenger.interface';
import { handleMessage } from './message/message.service';

export const verifyService = (verification: VerifyRequest) =>
    verification['hub.mode'] === 'subscribe' &&
    verification['hub.verify_token'] === process.env.WEBHOOK_TOKEN
        ? verification['hub.challenge']
        : null;

export const webhookService = (event: Event) =>
    Promise.all(event.entry.map((entry) => entryRouter(entry)));

export const entryRouter = (entry: Entry) => {
    const messaging = entry.messaging[0];

    if ('message' in messaging) {
        return handleMessage(messaging);
    }
};
