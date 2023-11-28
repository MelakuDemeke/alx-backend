import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const consoleSpy = sinon.spy(console);
  const pushNotificationQ = createpushNotificationQ({ name: 'push_notification_code_test' });
});
