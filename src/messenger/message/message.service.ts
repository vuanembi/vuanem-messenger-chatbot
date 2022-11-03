import { Message } from './message.interface';
import { phoneDetection } from './phone-detection.service';
import { store } from './store.service';

export const handleMessage = (message: Message) =>
    Promise.all([phoneDetection, store].map((service) => service(message)));
