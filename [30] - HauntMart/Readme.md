# Day 30
## Challenge: HauntMart

This challenge exploited a Server-Side Request Forgery (SSRF) vulnerability in the product manual upload feature. The application filtered requests to localhost using a blacklist but could be bypassed by using the address http://0:1337, which resolved to localhost. By sending a crafted request to the /addAdmin endpoint through SSRF, it was possible to escalate a normal user to an admin. Once the user was promoted, accessing /home revealed the hidden flag. This demonstrated how improper SSRF filtering can lead to privilege escalation and data exposure.
