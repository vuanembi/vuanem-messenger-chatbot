import { Router } from 'express';

import { Entry, Event, VerifyRequest } from './messenger.interface';
import { verifyService, webhookService } from './messenger.service';
import { storeService } from './store/store.service';

export const messengerController = Router();

messengerController.use(({ body }: { body: Event }, res, next) => {
    console.log('body', JSON.stringify(body));
    storeService(body.entry).finally(() => next());
});

messengerController.get('/', ({ query }, res) => {
    const response = verifyService(query as VerifyRequest);

    response ? res.send(response) : res.status(403).end();
});

messengerController.post('/', ({ body }, res) => {
    webhookService(body as Event)
        .catch((err) => {
            console.log(JSON.stringify(err));
            res.status(500).json({ err });
        })
        .finally(() => res.status(200).send('EVENT_RECEIVED'));
});
