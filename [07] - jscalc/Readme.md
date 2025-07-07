# Day 07 
## Challenge: jscalc
The application exposes a POST endpoint at `/api/calculate` that expects a JSON data with a formula field. Internally, the backend evaluates the value of formula using eval():
```
eval(`(function() { return ${ formula }; })()`)
```
The formula is not sanitized and validated, so we can inject arbitrary JavaScript code — leading to full remote code execution on the server.
