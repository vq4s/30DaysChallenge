# Day 16
## Challenge: baby interdimensional internet

This challenge showcases a Python code injection vulnerability caused by unsafe usage of the `exec()` function. 
The web application accepts user input via POST parameters ingredient and measurements, which are directly concatenated into a Python assignment string and executed using `exec()`. 
This allows an attacker to inject arbitrary Python code, including importing modules and executing system commands. By injecting a payload such as `__import__('os').popen('cat flag').read()`, 
an attacker can read sensitive files from the server. The vulnerability demonstrates the critical danger of evaluating user input without proper sanitization.
