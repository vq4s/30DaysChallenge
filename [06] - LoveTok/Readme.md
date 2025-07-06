# Day 05 - LoveTok
## Challenge: LoveTok

The vulnerability was caused by the unsafe use of PHP's eval() function on user input filtered only with addslashes(). 
This filtering could be bypassed using the ${} syntax, allowing remote code execution (RCE) via crafted GET parameters.
