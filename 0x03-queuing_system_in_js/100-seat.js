import { createClient } from 'redis';
import { createQueue } from 'kue';
import express from 'express';

const app = express();
const queue = createQueue();
const client = createClient({ name: 'reserve_seat' });
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const PORT = 1245;

const reserveSeat = async (number) => {
  return promisify(client.SET).bind(client)('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return promisify(client.GET).bind(client)('available_seats');
};

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
