# Day 21
## Challenge: Emoji voting

The Emoji Voting application is vulnerable to a blind SQL injection via the order parameter in a POST request to /api/list. This input is directly embedded into an ORDER BY clause without sanitization, allowing for boolean-based payloads using CASE WHEN. An attacker can extract table names from sqlite_master and exfiltrate sensitive data, such as flags, character by character. The vulnerability can be fully automated using a simple Python script. The issue stems from unsafe SQL construction and lack of input validation. Proper parameterization should be implemented to prevent exploitation.
