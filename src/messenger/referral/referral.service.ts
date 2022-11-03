import { Referral } from './referral.interface';
import { store } from './store.service';

export const handleReferral = (message: Referral) =>
    Promise.all([store].map((service) => service(message)));
