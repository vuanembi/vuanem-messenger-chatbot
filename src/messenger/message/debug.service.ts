import { Message } from './message.interface';
import { sendMessage } from '../messenger.repository';

export const debug = async (message: Message) => {
    const { text } = message.message;
    if (text && text.match(/\/debug (\w*)/)) {
        return sendMessage({
            recipient: message.sender,
            messaging_type: 'RESPONSE',
            message: { text: JSON.stringify(message) },
        });
    }
};
