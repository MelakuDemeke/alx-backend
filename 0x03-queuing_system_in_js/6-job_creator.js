import { createQueue } from 'kue';

const queue = createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', {
  phoneNumber: '0102030405',
  message: 'Account registered',
});

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })