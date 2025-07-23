# Day 23
## Challenge: Wild Goose Hunt

The Wild Goose Hunt challenge is vulnerable to NoSQL injection due to unsanitized input being passed directly to MongoDB queries. 
The login logic accepts nested query operators, allowing attackers to bypass authentication or perform regex-based brute-force attacks. 
Using the $regex operator on the password field, it is possible to extract the flag one character at a time by checking for known prefixes.  
