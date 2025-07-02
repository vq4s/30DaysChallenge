# Day 02 - NoSQL Injection
## Challenge: CandyVault

This challenge demonstrates a classic NoSQL Injection – Authentication Bypass in a Flask web application using MongoDB as the backend database.
The application accepts user credentials via JSON (application/json) and passes them directly into a find_one() MongoDB query without input sanitization or type enforcement.

Vulnerability:
```
user = users_collection.find_one({"email": email, "password": password})
```
This allows an attacker to supply a crafted payload with MongoDB operators (e.g., $ne) to bypass authentication logic:
```
{
  "email": { "$ne": 0 },
  "password": { "$ne": 0 }
}
```
