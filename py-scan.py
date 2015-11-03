"""
Copyright 2015 Carnegie Mellon University

This material is based upon work funded and supported by the Department of Defense under Contract No. FA8721-05-C-0003 with Carnegie Mellon University for the operation of the Software Engineering Institute, a federally funded research and development center.

Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the United States Department of Defense.

NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN “AS-IS” BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.

This material has been approved for public release and unlimited distribution.

DM-0002986

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