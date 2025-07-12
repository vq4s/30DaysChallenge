# Day 12
# Challenge: RenderQuest
The vulnerable Go web application allows remote template injection via the use_remote=true parameter and renders user-supplied templates using html/template.
By abusing the .FetchServerInfo method inherited in the request context, arbitrary shell commands can be executed.
