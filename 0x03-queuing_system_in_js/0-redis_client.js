import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log('Redis client not connected to the server:',err.toString(error));
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
