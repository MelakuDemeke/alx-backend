import { createQueue, Job } from 'kue';

const queue = createQueue();
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];