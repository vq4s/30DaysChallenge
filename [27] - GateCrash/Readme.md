# Day 27
## Challenge: GateCrash

This challenge exploits a CRLF injection vulnerability in Nim's httpclient library (≤ v1.2.6), where the User-Agent header is improperly decoded and injected into a subsequent HTTP request. By injecting a payload with %0D%0A (CRLF), it's possible to append a second HTTP body containing malicious JSON. This bypasses a weak SQLi filter and triggers a second vulnerable request to a Go-based backend. The backend constructs SQL queries via string concatenation, allowing for classic SQL injection using the injected data. Combined, these issues lead to Remote Code Execution by forcing the backend to authenticate an attacker-controlled user and reveal the flag.
