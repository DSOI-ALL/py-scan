"""
    Usage:

        python py-scan.py -d [directory]
"""
import getopt
import sys
import os
import re


regexs = ['DEBUG *= *True']
DEBUG=True

def main(directory):
    exit_code = 0
    reg_lib = []
    for regex in regexs:
        reg_lib.append(re.compile(regex))

    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename[-3:] == ".py":
                filepath = os.path.join(dirname, filename)

                with open(filepath) as source_file:
                    source_line = source_file.readline()
                    line = 1

                    while source_line:
                        for reg in reg_lib:
                            result = reg.match(source_line)
                            
                            if result:
                                print "Issue Detected in %s line %s: %s"%(filepath, line, source_line.strip("\n"))
                                exit_code = 1

                        source_line = source_file.readline()
                        line = line + 1

    sys.exit(exit_code)

if __name__ == '__main__':
    

    try:
        opts, args = getopt.getopt(sys.argv[1:], "Hh:Dd:", ["help", "dir="])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    directory = ""
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        if o in ("-d", "-D", "--dir"):
            directory = a


    if directory == "":
        print __doc__
        sys.exit(1)

    main(directory)