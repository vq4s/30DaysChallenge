# Day 25
## Challenge: BlinkerFluids

This challenge exploits a known Remote Code Execution vulnerability in the `md-to-pdf` NPM package, specifically version 4.1.0. 
The vulnerability arises from the package's unsafe use of JavaScript code blocks (---js ... ---) in Markdown, which are directly evaluated during the PDF rendering process.
By injecting a JavaScript payload using the child_process module, we can execute arbitrary system commands on the server. In this case, 
the exploit copies the /flag.txt file to a accessible location, allowing to retrieve it via a simple HTTP GET request. 
