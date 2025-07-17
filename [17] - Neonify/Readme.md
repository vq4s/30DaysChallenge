# Day 17
## Challenge: Neonify
This challenge demonstrates a Server-Side Template Injection (SSTI) vulnerability in a Ruby-based application using the ERB templating engine. User input is passed directly into ERB.new(...).result(binding) after being checked against a regex pattern. However, 
the regular expression only validates the first line of input, allowing malicious payloads to be injected via a newline (\n) character. This bypass enables attackers to execute arbitrary Ruby code within the server context. In this case, 
it was possible to read sensitive files such as flag.txt using `<%= %x(cat flag.txt) %>`. The challenge highlights the risks of improperly filtered template rendering and insufficient input validation.
