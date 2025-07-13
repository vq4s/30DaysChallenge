# Day 13
## Challenge: ProxyAsASerive
The application exposes a proxy endpoint that takes a url parameter and appends it to `http://reddit.com` before making an HTTP request. It implements a basic blacklist to block internal IPs like `127.0.0.1`, but the validation is insufficient. By using the @ character in the payload, attacker can bypass the hostname restriction and force a request to localhost.
This allows access to an internal route `/debug/environment`, which is normally restricted to local connections. As a result, sensitive environment variables, including the flag, are leaked in the response.
