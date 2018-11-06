#!/usr/bin/env python

# maven logs parser

from __future__ import print_function
import re
import fileinput


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

testResultPattern = re.compile(r"(^\[INFO]|\[ERROR]) Tests run: \b([0-9]+)\b, Failures: \b([0-9]+)\b, Errors: \b([0-9]+)\b, Skipped: \b([0-9]+)\b")
buildCompletedPattern = re.compile(r"^\[INFO] BUILD SUCCESS$");
buildModulePattern = re.compile(r"^\[INFO] Building (.*)$");
buildJarPattern = re.compile(r"^\[INFO] Building jar: (.*)$");
logPattern = re.compile("(.*)Some text to find(.*)");

log_file = fileinput.input()
line = log_file.readline()
while line:
    if buildModulePattern.match(line) and not buildJarPattern.match(line):
        print(BOLD + line + ENDC, end="")

    if buildCompletedPattern.match(line):
        print(OKGREEN + "\n!!! Build completed !!!" + ENDC)

    if logPattern.match(line):
        print(WARNING + line + ENDC, end="")

    if testResultPattern.match(line):
        res = testResultPattern.search(line)
        print(line, end="")
        if int(res.group(3)) > 0 or int(res.group(4)) > 0:
            print(FAIL + "------------------------------------------------------------------------------------------------\n" + ENDC)
            for i in range(0, 10):
                print(FAIL + log_file.readline() + ENDC, end="")

    line = log_file.readline()

log_file.close()
