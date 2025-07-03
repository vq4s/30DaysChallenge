# Day03 - Pin in javascript
# Challenge: Trapped Source

This challenge present a very simple web page with PIN input. The correct PIN in hardcoded in the JavaScript source code. By inspecting the HTML or using DevTools, you can extract PIN value and send to the backend to retrive the flag.

```
<script>
	window.CONFIG = window.CONFIG || {
		buildNumber: "v20190816",
		debug: false,
		modelName: "Valencia",
		correctPin: "7410",
	}
</script>
```
