import { Queue, Job } from 'kue';

export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const singleJob of jobs) {
    const job = queue.create('push_notification_code_3', singleJob);
  }
}
