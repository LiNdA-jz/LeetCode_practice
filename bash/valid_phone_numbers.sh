# Read from the file file.txt and output all valid phone numbers to stdout.
# not sure how to write bash file
#import re
#
#with open("file.txt") as f:
#    while f.readline():
#        s = f.readline()
#        if re.match("^[\d]*3-[\d]*3-[\d]*4", s):
#            print(s)
# grep command is used to search for a pattern in a file or files
# -E option is used to enable extended regular expressions
# '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'
# -e: to include multiple regex
grep -e "^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$" -e "^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$" file.txt