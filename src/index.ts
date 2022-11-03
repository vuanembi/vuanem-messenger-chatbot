import { http } from '@google-cloud/functions-framework';
import express from 'express';
import cors from 'cors';

import { messengerController } from './messenger/messenger.controller';

const app = express();
app.use(cors());

app.get('/', (req, res) => {
    res.status(200).json({ ok: 200 });
});

app.use('/messenger', messengerController);

http('main', app);
