import { createQueue, Job } from 'kue';

const queue = createQueue();
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  let totalNotifications = 2;
  let pendingNotifications = 2;
  let sendInterval = setInterval(() => {
    if (totalNotifications - pendingNotifications <= totalNotifications / 2) {
      job.progress(totalNotifications - pendingNotifications, totalNotifications);
    }

    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }

  }, 1000);
}