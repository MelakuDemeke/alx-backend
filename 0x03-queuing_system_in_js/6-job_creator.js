import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});
