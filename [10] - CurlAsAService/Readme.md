# Day 10
## Challenge: CurlAsAService

This challenge involves exploiting an argument injection vulnerability in a cURL wrapper. 
Although traditional command injection is mitigated using escapeshellcmd, 
it's still possible to pass additional curl arguments like --trace-ascii - or -T /flag via the ip parameter. By injecting 127.0.0.1 -T /flag -vv --trace-ascii -, we can leak the contents of the /flag file in the HTTP response.
The payload is sent to the /api/curl endpoint using a POST request.
