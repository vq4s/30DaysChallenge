# Day 28
## Challenge: Pumpkin Spice

The PumpkinSpice web application contains a stored XSS vulnerability combined with a blind command injection that leads to remote code execution. 
User-supplied input in the `/add/address` endpoint is stored and rendered in addresses.html allowing arbitrary JavaScript execution. 
When malicious JavaScript is injected, it is executed by a Selenium-based bot running on localhost, bypassing IP restrictions on the /api/stats endpoint. 
This endpoint executes the command parameter directly with subprocess.check_output() and shell=True, enabling attackers to run arbitrary system commands. 
By chaining these issues, an attacker can retrieve sensitive files or fully compromise the server.
