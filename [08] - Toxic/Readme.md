# Day 08
## Challenge: Toxic
This exploit targets a PHP web application vulnerable to insecure deserialization combined with Local File Inclusion (LFI) and log poisoning.
The application unserializes user-controlled PHPSESSID cookies containing a serialized object with a file path. By poisoning the server logs with a PHP payload using the User-Agent header and pointing the LFI to the access log, 
it is possible to achieve Remote Code Execution (RCE).
