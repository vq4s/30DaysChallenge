# Day 15
## Challenge: Templated
The target application uses user-controlled input directly inside templates without sanitization. 
By injecting a Jinja2 payload such as `{{1+1}}`, we confirm that code is being evaluated server-side. 
To escalate this into remote code execution, I used python class hierarchy to access the object base class and list all subclasses with `__subclasses__()`.
