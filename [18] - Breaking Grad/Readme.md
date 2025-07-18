# Day 18
## Challenge: Breaking Grad

This challenge is vulnerable to Prototype Pollution on the `/api/calculate` endpoint.
By injecting into constructor.prototype.env, we can poison environment variables for any newly spawned Node.js process.

Specifically, we set:
`NODE_OPTIONS=--require /proc/self/environ`
and inject arbitrary code into a fake variable like env.x, which gets executed when a new process spawns.

Then, by triggering a request to /debug/version, a new Node.js process is spawned, and our payload is executed server-side.
