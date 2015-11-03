# py-scan
Scans python source files for the presence of regex patterns of interest and exits 1 if they appear.  This is an example of how to conduct static  code analysis to look for security concerns in source code.  This script could be used within a continuous integration process to check for known source code patterns that should not be pushed to a production environment. 

# Adding Checks 

Modify py-scan.py and add regular expressions to the regexs list to add regular expressions that match code that is deemed "bad." 