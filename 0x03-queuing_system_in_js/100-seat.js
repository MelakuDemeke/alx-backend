import { createClient } from 'redis';

const client = createClient();

const reserveSeat = async (number) => {
  return promisify(client.SET).bind(client)('available_seats', number);
};
