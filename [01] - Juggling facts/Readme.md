
#Day 01 – Auth Bypass via Type Confusion
## Challenge: Juggling facts

In this challenge, the goal was to access some hidden "secrets" that were only supposed to be available from localhost.
Instead of sending "secrets" as a string in JSON, I just sent true — and that was enough to bypass the IP check on the backend.

Vulnerable code:
```
if ($jsondata['type'] === 'secrets' && $_SERVER['REMOTE_ADDR'] !== '127.0.0.1') {
    return $router->jsonify(['message' => 'Currently this type can be only accessed through localhost!']);
}
```
