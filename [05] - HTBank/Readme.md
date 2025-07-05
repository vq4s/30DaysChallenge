# Day 05
## Challenge: HTBank

This challenge exploits an HTTP Parameter Pollution vulnerability in the /api/withdraw endpoint.

The frontend Flask application reads only the first amount parameter, while the backend PHP service processes the last one. By sending two amount parameters (e.g., 0 and 1337), the Flask layer validates the request as safe, but PHP executes it using 1337, triggering the flag reveal.
