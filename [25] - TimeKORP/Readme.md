# Day 25
## Challenge: TimeKORP

The application is vulnerable to command injection through the format query parameter. The server-side code improperly passes user input directly into a shell command without sanitization or validation. By injecting shell syntax like '; cat /flag || ', an attacker can break out of the expected input context and execute arbitrary system commands.
