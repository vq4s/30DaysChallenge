# Day 24
## Challenge: Slippy

The vulnerability is based on a Zip Slip flaw that occurs when .tar.gz archives are extracted without properly sanitizing file paths. The Flask application uses tarfile.extractall(), 
which allows archive entries containing ../ to write files outside the intended extraction directory. This makes it possible to overwrite critical application files, such as routes.py.
