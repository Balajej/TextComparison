from Parser import *

with open('fileA.dat') as f1:
    mylist1 = f1.read().splitlines()

with open('fileB.dat') as f2:
    mylist2 = f2.read().splitlines()

#differ = Parser(open('fileA.dat').readlines(), open('fileB.dat').readlines())
differ = Parser(mylist1, mylist2)

same_record_file = open('samerecords.txt', 'w')
unique_record_file = open('uniquerecords.txt', 'w')
different_record_file = open('differentrecords.txt', 'w')
for x in differ:
    print(x)
    if 0 in x.values():
        print('Same records are found')
        for value in x:
            if value == "Record":
                same_record_file.write('{}\n'.format(x.get('Record')))

    elif 1 in x.values():
        print('Unique Records are found')
        for value in x:
            if value == "Record":
                unique_record_file.write('{}\n'.format(x.get('Record')))

    elif 2 in x.values():
        print('Unique Records are found')
        for value in x:
            if value == "Record":
                unique_record_file.write('{}\n'.format(x.get('Record')))

    elif 3 in x.values():
        print('Different Records are found')
        for value in x:
            if value == "Record":
                different_record_file.write('{}\n'.format(x.get('Record')))
