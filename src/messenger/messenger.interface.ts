import { Message } from './message/message.interface';
import { Referral } from './referral/referral.interface';

export type VerifyRequest = {
    "hub.challenge": string;
    "hub.mode": string;
    "hub.verify_token": string;
}

export type Messaging = {
    sender: { id: string };
    recipient: { id: string };
    timestamp: number;
};

export type MessagingType = Message | Referral

export type Entry = {
    id: string;
    time: number;
    messaging: [MessagingType];
};

export type Event= {
    object: 'page';
    entry: Entry[];
};
