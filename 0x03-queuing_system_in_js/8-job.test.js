import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const consoleSpy = sinon.spy(console);
  const notificationQ = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    notificationQ.testMode.enter(true);
  });
  
  after(() => {
    notificationQ.testMode.clear();
    notificationQ.testMode.exit();
  });
  
  
});
