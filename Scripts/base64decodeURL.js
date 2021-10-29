// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Awal Ariansyah
// GITHUB: https://github.com/snowfluke

const decode = base64 => base64.includes('=aHR') ? atob(base64) : "not a valid base64 url";
