import axios from 'axios';

const client = axios.create({
    baseURL: 'https://graph.facebook.com/v15.0',
    headers: { 'Content-Type': 'application/json' },
    params: { access_token: process.env.FB_PAGE_ACCESS_TOKEN },
});

type SendMessageOptions = {
    recipient: { id: string };
    messaging_type: string;
    message: {
        text: string;
    };
};

export const sendMessage = (data: SendMessageOptions) =>
    client.request({
        method: 'POST',
        url: '/me/messages',
        data,
    });
