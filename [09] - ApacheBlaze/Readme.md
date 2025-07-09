# Day 09
## Challenge: ApacheBlaze

ApacheBlaze is a Hack The Box web challenge based on CVE-2023-25690, a CRLF injection vulnerability in `Apache HTTP Server ≤ 2.4.55`. Due to improper input validation in a RewriteRule, 
it's possible to inject HTTP headers via the URL path. By crafting a payload X-Forwarded-Host header, an attacker can trick the backend into thinking the request comes from dev.apacheblaze.local. 
