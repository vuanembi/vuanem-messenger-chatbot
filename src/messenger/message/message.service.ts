import { Message } from './message.interface';
import { detectPhone } from './phone-detection.service';
import { debug } from './debug.service';
import { store } from './store.service';

export const handleMessage = (message: Message) =>
    Promise.all([debug, detectPhone, store].map((service) => service(message)));
