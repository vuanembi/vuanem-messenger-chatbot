import { MessagingType } from '../messenger.interface';
import { Referral } from './referral.interface';

export const isReferral = (messaging: MessagingType): messaging is Referral =>
    'referral' in messaging;
