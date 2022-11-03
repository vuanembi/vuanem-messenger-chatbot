import { Router } from 'express';

import { VerifyRequest, Event, MessagingType } from './messenger.interface';
import { verifyService, webhookService } from './messenger.service';

export const messengerController = Router();

messengerController.get('/', ({ query }, res) => {
    const response = verifyService(query as VerifyRequest);

    response ? res.send(response) : res.status(403).end();
});

messengerController.post('/', ({ body }, res) => {
    webhookService(body as Event<MessagingType>)
        .catch((err) => {
            console.log(err);
            res.status(500).json({ err });
        })
        .finally(() => res.status(200).send('EVENT_RECEIVED'));
});
