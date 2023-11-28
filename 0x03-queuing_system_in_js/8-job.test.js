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

  afterEach(() => {
    consoleSpy.log.resetHistory();
  });

  it('handles empty jobInfos array', () => {
    createPushNotificationsJobs([], notificationQ);
    expect(notificationQ.testMode.jobs.length).to.equal(0);
  });

  it('Appends tasks to the queue with the appropriate type', (done) => {
    expect(notificationQ.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: '01020304056',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '1011121314156',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, notificationQ);
    expect(notificationQ.testMode.jobs.length).to.equal(2);
    expect(notificationQ.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(notificationQ.testMode.jobs[0].type).to.equal('push_notification_code_3');
    notificationQ.process('push_notification_code_3', () => {
      expect(
        consoleSpy.log
          .calledWith('Notification job created:', notificationQ.testMode.jobs[0].id)
      ).to.be.true;
      done();
    });
  });

});
