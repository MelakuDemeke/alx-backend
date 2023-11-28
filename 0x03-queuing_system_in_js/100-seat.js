import { createClient } from 'redis';
import { createQueue } from 'kue';

const client = createClient({ name: 'reserve_seat' });
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const queue = createQueue();

const reserveSeat = async (number) => {
  return promisify(client.SET).bind(client)('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return promisify(client.GET).bind(client)('available_seats');
};

