# Challenge: Juggling facts

Day 01 – Auth Bypass via Type Confusion

This challenge involved bypassing an IP-based access control check in a PHP backend.
By sending a boolean true as JSON instead of the expected string ("secrets"), the server skipped the access restriction logic and returned the protected data.
