from Parser import *
from operator import itemgetter

differ = Parser(open('fileA.dat').readlines(), open('fileB.dat').readlines())

same_record_file = open('samerecords.txt', 'w')
unique_record_file = open('uniquerecords.txt', 'w')
different_record_file = open('differentrecords.txt', 'w')
for x in differ:
    print(x)
    if 0 in x.values():
        print('Same records are found')
        for value in x.values():
            same_record_file.write('{}'.format(value).strip())

    elif 1 in x.values():
        print('Unique Records are found')
        for value in x.values():
            unique_record_file.write('{}'.format(value).strip())

    elif 2 in x.values():
        print('Unique Records are found')
        for value in x.values():
            unique_record_file.write('{}'.format(value).strip())

    elif 3 in x.values():
        print('Different Records are found')
        for value in x.values():
            different_record_file.write('{}'.format(value).strip())
