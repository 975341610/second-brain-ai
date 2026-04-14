import http from 'http';
import { request } from 'https';

const options = {
  hostname: '1386dd63-a26f-40e1-bbbb-eabfbb2201b1-cube-kubestrato-online7.code-server.strato-https-proxy.bytedance.net',
  port: 443,
  path: '/api/ai/inline',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'text/event-stream'
  }
};

const req = request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`);
  console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
  
  res.on('data', (chunk) => {
    console.log(`BODY: ${chunk.toString()}`);
  });
  
  res.on('end', () => {
    console.log('No more data in response.');
  });
});

req.on('error', (e) => {
  console.error(`problem with request: ${e.message}`);
});

// Write data to request body
const postData = JSON.stringify({
    "action": "continue",
    "prompt": "续写，将字数扩充到2000字以上",
    "context": "测试测试测试"
});

req.write(postData);
req.end();
