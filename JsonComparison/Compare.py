from sys import stdin

import jq as jq
import os
import subprocess

from Parser import *
import re
import json
from jsondiff import diff
import tempfile
import pyjq
from deepdiff import DeepDiff  # For Deep Difference of 2 objects
from deepdiff import grep, DeepSearch  # For finding if item exists in an object
from deepdiff import DeepHash  # For hashing objects based on their contents

with open('fileA.dat') as f1:
    mylist1 = f1.read().splitlines()

with open('fileB.dat') as f2:
    mylist2 = f2.read().splitlines()

differ = Parser(mylist1, mylist2)
# Parser.__init_subclass__(

same_record_file = open('samerecords.txt', 'w')
unique_record_file = open('uniquerecords.txt', 'w')
different_record_file1 = open('differentrecords_file1.txt', 'w')
different_record_file2 = open('differentrecords_file2.txt', 'w')
for x in differ:
    print(x)
    if 0 in x.values():
        print('Same records are found')
        for value in x:
            if value == "Record":
                same_record_file.write('{}\n'.format(x.get('Record')))

    elif 1 in x.values() or 2 in x.values():
        print('Unique Records are found')
        for value in x:
            if value == "Record":
                unique_record_file.write('{}\n'.format(x.get('Record')))

    elif 3 in x.values():
        print('Different Records are found')
        for value in x:
            if value == "Record":
                different_record_file1.write('{}\n'.format(x.get('Record')))
            if value == "newline":
                different_record_file2.write('{}\n'.format(x.get('newline')))

different_record_file1.close()
different_record_file2.close()

with open('differentrecords_file1.txt') as f3:
    mylist3 = sorted(f3.read().splitlines())

with open('differentrecords_file2.txt') as f4:
    mylist4 = sorted(f4.read().splitlines())

mylist3_str = '\n '.join(mylist3)
mylist4_str = '\n '.join(mylist4)

print('mylist3_str is : ', mylist3_str)
print('mylist4_str is : ', mylist4_str)


def Diff(A, B):
   print("Difference of two lists ::>")
   return (list(set(A) - set(B)))


comparison_report = open('Comparison_Report.txt', 'w')
comparison_report.write("\t\t\t\t\t\t\t\t\t\tFileA\t\t\t\t\t\t\t\t\t\tFileB\n")
count = 0
print(type(mylist3))
for index, file1 in enumerate(mylist3):
    count += 1
    spl_word = re.search(r"(?<={\"CID\":\").*?(?=\")", file1)
    print(index, spl_word.group((0)))
    for index1, file2 in enumerate(mylist4):
        spl_word1 = re.search(r"(?<={\"CID\":\").*?(?=\")", file2)
        if str(spl_word) == str(spl_word1):
            print(index1, spl_word1.group((0)))
            with open('CID1.dat', 'w') as cid1:
                cid1.write(mylist4[index1])
                with open('CID2.dat', 'w') as cid2:
                    cid2.write(mylist3[index])
            p1 = subprocess.run('diff <(jq -S . CID1.dat) <(jq -S . CID2.dat) | grep \'<\' | sed \'s/<*//\'', stdout=subprocess.PIPE, text=True, check=True, shell=True)
            print(p1.args)


    comparison_report.write(spl_word.group(0))
    comparison_report.write("\n")
