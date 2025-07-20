# Day 20
## Challenge: Amidst us
The Amidst Us challenge involves a Remote Code Execution vulnerability in the Pillow image-processing library. 
The backend uses `ImageMath.eval()` to dynamically evaluate an expression that includes user-controlled RGB values.
These values are passed directly from the background JSON field without proper sanitization. 
By injecting Python code, such as `exec()`, into the RGB array, an attacker can execute arbitrary system commands on the server. 
For example, one can use this to copy the flag file into a web-accessible location. This vulnerability stems from insecure use of dynamic evaluation in Pillow version 8.4.0.
