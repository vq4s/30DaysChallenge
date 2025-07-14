# Day 14
## Challenge: LazyBallot

The LazyBallot challenge demonstrates a classic NoSQL injection vulnerability in a login endpoint backed by CouchDB. 
The backend fails to validate input types, allowing an attacker to inject a query object using Mongo-style operators like "$ne" (not equal). 
By sending `{"username": "admin", "password": {"$ne": 1}}` to `/api/login`, an attacker can bypass authentication entirely. Once logged in, the attacker gains access to protected routes such as `/api/votes/list`, 
which leaks sensitive information (including the flag) stored in the database. This type of vulnerability highlights the risks of trusting user-supplied JSON objects directly in NoSQL queries without proper sanitization. 
It's a reminder that input validation and strict schema enforcement are just as important in NoSQL systems as in traditional SQL environments.
