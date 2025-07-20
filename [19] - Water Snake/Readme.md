# Day 19
## Challenge: Water Snake
The /update endpoint of the Watersnake application is vulnerable to YAML deserialization due to the unsafe use of SnakeYAML.load(). This allows attackers to instantiate arbitrary Java objects using custom YAML tags.
By supplying the tag !!com.lean.watersnake.GetWaterLevel, the attacker can trigger command execution during object construction. This works because the constructor calls a method that runs system commands via ProcessBuilder. 
Using this flaw, an attacker can execute commands like copying sensitive files into web-accessible locations. The issue is linked to CVE-2022-1471 and demonstrates the dangers of deserializing untrusted input without proper safeguards.
