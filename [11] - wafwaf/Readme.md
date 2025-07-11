# Day 11
## Challenge: wafwaf
This challenge demonstrates a time-based blind SQL injection vulnerability hidden behind a naive WAF that filters SQL keywords using regular expressions. The application accepts JSON input via POST and directly uses unsanitized user input in a SQL query. Despite the WAF, we can bypass it using encoded payloads (charunicodeescape) and extract data via SLEEP() delays.
