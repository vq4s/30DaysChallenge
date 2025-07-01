# Challenge: Juggling facts

# Day 01 – Auth Bypass via Type Confusion

In this challenge, the goal was to access some hidden "secrets" that were only supposed to be available from localhost.
Instead of sending "secrets" as a string in JSON, I just sent true — and that was enough to bypass the IP check on the backend.
