import { MessagingType } from '../messenger.interface';
import { Message } from './message.interface';
import { detectPhone } from './phone-detection.service';
import { debug } from './debug.service';

export const isMessage = (messaging: MessagingType): messaging is Message =>
    'message' in messaging;

export const handleMessage = (message: Message) =>
    Promise.all([debug, detectPhone].map((service) => service(message)));
