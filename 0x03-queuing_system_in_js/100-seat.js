import { createClient } from 'redis';

const client = createClient();
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;

const reserveSeat = async (number) => {
  return promisify(client.SET).bind(client)('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return promisify(client.GET).bind(client)('available_seats');
};

