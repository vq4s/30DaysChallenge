# Day 29
## Challenge: petpet rcbee

This challenge exploited CVE-2018-16509 in Ghostscript 9.23, used as a legacy dependency for image processing with Python Pillow. The vulnerability allowed command injection by uploading a malicious EPS file. The crafted PostScript payload executed a command to move and expose the flag file into a publicly accessible directory. The application ran inside a Docker container using Flask and processed user-submitted images. By leveraging this flaw, it was possible to achieve unauthorized file access and ultimately gain RCE to solve the challenge.
