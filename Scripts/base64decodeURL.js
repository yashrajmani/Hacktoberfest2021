const decode = base64 => base64.includes('=aHR') ? atob(base64) : "not a valid base64 url";
