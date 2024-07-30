import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    console.log(await promisify(client.get).bind(client)(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
