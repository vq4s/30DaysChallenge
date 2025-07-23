# Day 22
## Challenge: Jailbreak

The Jailbreak challenge is vulnerable to XML External Entity (XXE) injection. The /api/update endpoint accepts user-supplied XML without proper entity restrictions, allowing attackers to define external entities referencing local files. By crafting a malicious XML payload, it's possible to read sensitive files such as /flag.txt from the server. 
This leads to unauthorized disclosure of internal data. Proper XML parsing configuration should disable external entity resolution to mitigate this vulnerability.
