# Day 04
## Challenge: Insomnia

The backend (written in PHP) accepted login credentials in JSON format. A logic flaw in the input validation condition allowed login without a password:
```
if (!count($json_data) == 2) { ... }
```
The ! operator was incorrectly applied to the count() result, causing the condition to always evaluate to false. This allowed login using only the username field.

By submitting only a username and reusing the issued JWT, it was possible to access the admin account and retrieve the flag.
