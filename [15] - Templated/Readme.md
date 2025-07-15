# Day 15
## Challenge: Templated
The target application uses user-controlled input directly inside templates without sanitization. 
By injecting a Jinja2 payload such as `{{1+1}}`, we confirm that code is being evaluated server-side. 
From there, we navigate Python’s object model using `__class__.__mro__` and `__subclasses__()` to locate a class (e.g. warnings.catch_warnings) that allows access to the global namespace and, ultimately, the built-in `__import__ function`.
