# Day 11
## Challenge: wafwaf
This challenge demonstrates a time-based blind SQL injection vulnerability hidden behind a naive WAF that filters raw SQL keywords using regex. The application accepts JSON input via POST and uses unsanitized user input in a SQL query.
